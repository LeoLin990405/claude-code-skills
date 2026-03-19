#!/usr/bin/env python3
"""
SQL to Shell Script Converter (SOTA)
将 SQL 代码智能转换为 Doris ETL Shell 脚本

Features:
- 自动解析 SQL 文件中的多个代码块
- 智能识别 DDL/DML 语句并分组
- 自动提取表名作为脚本名
- 支持日期参数化 (周/日/月)
- 自动添加执行日志和耗时统计
- 支持临时表清理
"""

import re
import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

class DateGranularity(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

@dataclass
class SQLBlock:
    """SQL 代码块"""
    content: str
    comment: str = ""
    block_type: str = "dml"  # ddl, dml, cleanup

@dataclass
class ScriptConfig:
    """脚本配置"""
    table_name: str
    description: str
    granularity: DateGranularity
    date_var: str
    sql_blocks: List[SQLBlock]
    temp_tables: List[str]
    author: str = ""

class SQL2ShConverter:
    """SQL 转 Shell 脚本转换器"""

    # 日期变量模式
    DATE_PATTERNS = {
        DateGranularity.WEEKLY: {
            'var_name': 'WEEK_START',
            'default_expr': '$(date -d "last monday" +%Y-%m-%d)',
            'comment': '周起始日期'
        },
        DateGranularity.DAILY: {
            'var_name': 'YYYY_MM_DD',
            'default_expr': '$(date +%Y-%m-%d)',
            'comment': '执行日期'
        },
        DateGranularity.MONTHLY: {
            'var_name': 'MONTH_START',
            'default_expr': '$(date +%Y-%m-01)',
            'comment': '月起始日期'
        }
    }

    def __init__(self):
        self.temp_table_pattern = re.compile(r'(?:CREATE\s+TABLE|DROP\s+TABLE\s+IF\s+EXISTS)\s+(\w+\.tmp_\w+)', re.I)
        self.target_table_pattern = re.compile(r'(?:INSERT\s+INTO|DELETE\s+FROM|CREATE\s+TABLE)\s+(\w+\.\w+?)(?:\s|\(|;)', re.I)
        self.date_literal_pattern = re.compile(r"'(\d{4}-\d{2}-\d{2})'")
        self.dt_field_pattern = re.compile(r"STR_TO_DATE\s*\(\s*'(\d{4}-\d{2}-\d{2})'", re.I)

    def extract_sql_blocks(self, content: str) -> List[str]:
        """从 markdown 或纯文本中提取 SQL 代码块"""
        # 匹配 ```sql ... ``` 代码块
        md_pattern = re.compile(r'```sql\s*(.*?)```', re.DOTALL | re.I)
        blocks = md_pattern.findall(content)

        if blocks:
            # 过滤空块
            return [b.strip() for b in blocks if b.strip() and not b.strip().startswith('--')]

        # 如果没有 markdown 格式，直接返回整个内容
        return [content.strip()] if content.strip() else []

    def detect_granularity(self, sql: str) -> DateGranularity:
        """检测日期粒度"""
        sql_lower = sql.lower()
        if 'week' in sql_lower or 'weekly' in sql_lower or 'weekday' in sql_lower:
            return DateGranularity.WEEKLY
        elif 'month' in sql_lower or 'monthly' in sql_lower:
            return DateGranularity.MONTHLY
        return DateGranularity.DAILY

    def extract_table_name(self, sql: str) -> str:
        """提取目标表名"""
        # 优先匹配 INSERT INTO 或 CREATE TABLE (非临时表)
        for match in self.target_table_pattern.finditer(sql):
            table = match.group(1)
            if 'tmp_' not in table.lower():
                return table.split('.')[-1]
        return "unknown_table"

    def extract_temp_tables(self, sql: str) -> List[str]:
        """提取临时表名"""
        tables = set()
        for match in self.temp_table_pattern.finditer(sql):
            tables.add(match.group(1))
        return list(tables)

    def add_idempotent_delete(self, sql: str, table_name: str, var_name: str) -> str:
        """在 INSERT 语句前添加 DELETE 语句实现幂等性"""
        # 检查是否已经有 DELETE 语句
        if re.search(r'DELETE\s+FROM', sql, re.I):
            return sql

        # 检查是否有 INSERT INTO
        insert_match = re.search(r'(INSERT\s+INTO\s+\w+\.\w+)', sql, re.I)
        if not insert_match:
            return sql

        # 提取完整的表名
        full_table_name = insert_match.group(1).split()[-1]

        # 生成 DELETE 语句
        delete_stmt = f"DELETE FROM {full_table_name}\nWHERE dt = '${{{var_name}}}';\n\n"

        # 在 INSERT 前插入 DELETE
        result = sql.replace(insert_match.group(1), delete_stmt + insert_match.group(1))
        return result

    def parameterize_dates(self, sql: str, var_name: str) -> str:
        """智能参数化日期：仅参数化 dt 分区字段，保留数据过滤条件中的日期"""
        # 只参数化 STR_TO_DATE(...) 中的日期（通常是 dt 分区字段）
        def replace_dt_date(match):
            return f"STR_TO_DATE('${{{var_name}}}'"

        result = self.dt_field_pattern.sub(replace_dt_date, sql)
        return result

    def escape_sql_for_shell(self, sql: str) -> str:
        """转义 SQL 以便在 shell 中使用"""
        # 转义双引号内的特殊字符
        result = sql.replace('\\', '\\\\')
        result = result.replace('"', '\\"')
        # 保留 ${VAR} 变量引用
        return result

    def split_sql_statements(self, sql: str) -> List[Tuple[str, str]]:
        """将 SQL 分割为独立语句，返回 (语句, 注释) 列表"""
        statements = []
        current = []
        current_comment = ""

        for line in sql.split('\n'):
            stripped = line.strip()

            # 提取注释
            if stripped.startswith('--'):
                if not current:
                    current_comment = stripped[2:].strip()
                continue

            if not stripped:
                continue

            current.append(line)

            # 检测语句结束
            if stripped.endswith(';'):
                stmt = '\n'.join(current).strip()
                if stmt:
                    statements.append((stmt, current_comment))
                current = []
                current_comment = ""

        # 处理最后一个语句（可能没有分号）
        if current:
            stmt = '\n'.join(current).strip()
            if stmt:
                statements.append((stmt, current_comment))

        return statements

    def group_statements(self, statements: List[Tuple[str, str]]) -> List[SQLBlock]:
        """将语句分组为逻辑块"""
        blocks = []
        current_block = []
        current_comment = ""

        for stmt, comment in statements:
            stmt_upper = stmt.upper()

            # DDL 语句单独成块
            if any(kw in stmt_upper for kw in ['CREATE TABLE', 'DROP TABLE', 'ALTER TABLE']):
                if current_block:
                    blocks.append(SQLBlock(
                        content=';\n'.join(current_block) + ';',
                        comment=current_comment,
                        block_type='dml'
                    ))
                    current_block = []

                block_type = 'cleanup' if 'DROP TABLE' in stmt_upper and 'tmp_' in stmt.lower() else 'ddl'
                blocks.append(SQLBlock(content=stmt, comment=comment, block_type=block_type))
                current_comment = ""
            else:
                if not current_comment and comment:
                    current_comment = comment
                current_block.append(stmt.rstrip(';'))

        if current_block:
            blocks.append(SQLBlock(
                content=';\n'.join(current_block) + ';',
                comment=current_comment,
                block_type='dml'
            ))

        return blocks

    def generate_script(self, config: ScriptConfig) -> str:
        """生成完整的 shell 脚本"""
        date_config = self.DATE_PATTERNS[config.granularity]
        var_name = date_config['var_name']

        lines = [
            '#!/bin/bash',
            '##################################',
            f'### 脚本名：{config.table_name}.sh',
            f'### 作用：{config.description}',
            '##################################',
            'source /opt/common.sh',
            '',
            f'if [ $# -lt 1 ]; then',
            f'    {var_name}={date_config["default_expr"]}',
            'else',
            f'    {var_name}=$1',
            'fi',
            f'echo "{var_name}: ${{{var_name}}}"',
            ''
        ]

        # 生成 SQL 块
        for i, block in enumerate(config.sql_blocks, 1):
            # 添加幂等性处理（DELETE 语句）
            sql_with_delete = self.add_idempotent_delete(block.content, config.table_name, var_name)
            # 参数化日期
            sql_content = self.parameterize_dates(sql_with_delete, var_name)
            sql_escaped = self.escape_sql_for_shell(sql_content)

            # 确定块描述
            if block.comment:
                desc = block.comment
            elif block.block_type == 'ddl':
                desc = '建表/DDL'
            elif block.block_type == 'cleanup':
                desc = '清理临时表'
            else:
                desc = '数据处理'

            lines.extend([
                f'sql{i}="',
                f'{sql_escaped}',
                '"',
                f'echo "执行SQL{i}: {desc}"; start_time=$(date +%s); ExecuteDoris "${{sql{i}}}"; echo "耗时 $(($(date +%s) - start_time)) 秒"',
                ''
            ])

        lines.append(f'echo "######## {config.table_name} 完成 ########"')

        return '\n'.join(lines)

    def convert(self, input_content: str, description: str = "") -> str:
        """主转换函数"""
        # 提取 SQL 块
        sql_blocks = self.extract_sql_blocks(input_content)
        if not sql_blocks:
            raise ValueError("未找到有效的 SQL 代码")

        # 合并所有 SQL
        all_sql = '\n\n'.join(sql_blocks)

        # 检测配置
        granularity = self.detect_granularity(all_sql)
        table_name = self.extract_table_name(all_sql)
        temp_tables = self.extract_temp_tables(all_sql)

        # 分割和分组语句
        statements = self.split_sql_statements(all_sql)
        grouped_blocks = self.group_statements(statements)

        # 合并相邻的同类型块以减少 SQL 变量数量
        merged_blocks = self._merge_blocks(grouped_blocks)

        config = ScriptConfig(
            table_name=table_name,
            description=description or f"{table_name} ETL 脚本",
            granularity=granularity,
            date_var=self.DATE_PATTERNS[granularity]['var_name'],
            sql_blocks=merged_blocks,
            temp_tables=temp_tables
        )

        return self.generate_script(config)

    def _merge_blocks(self, blocks: List[SQLBlock], max_blocks: int = 5) -> List[SQLBlock]:
        """合并块以控制总数"""
        if len(blocks) <= max_blocks:
            return blocks

        # 按类型分组
        ddl_blocks = [b for b in blocks if b.block_type == 'ddl']
        dml_blocks = [b for b in blocks if b.block_type == 'dml']
        cleanup_blocks = [b for b in blocks if b.block_type == 'cleanup']

        result = []

        # DDL 合并为一个块
        if ddl_blocks:
            result.append(SQLBlock(
                content='\n'.join(b.content for b in ddl_blocks),
                comment='环境准备/建表',
                block_type='ddl'
            ))

        # DML 保持分开（最多3个）
        if len(dml_blocks) <= 3:
            result.extend(dml_blocks)
        else:
            # 合并为3个块
            chunk_size = len(dml_blocks) // 3 + 1
            for i in range(0, len(dml_blocks), chunk_size):
                chunk = dml_blocks[i:i+chunk_size]
                result.append(SQLBlock(
                    content='\n'.join(b.content for b in chunk),
                    comment=chunk[0].comment or f'数据处理 {i//chunk_size + 1}',
                    block_type='dml'
                ))

        # Cleanup 合并为一个块
        if cleanup_blocks:
            result.append(SQLBlock(
                content='\n'.join(b.content for b in cleanup_blocks),
                comment='清理临时表',
                block_type='cleanup'
            ))

        return result


def main():
    """CLI 入口"""
    if len(sys.argv) < 2:
        print("用法: sql2sh.py <input_file> [output_file] [description]")
        print("  input_file: SQL 文件或 Markdown 文件")
        print("  output_file: 输出的 shell 脚本 (可选，默认输出到 stdout)")
        print("  description: 脚本描述 (可选)")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    description = sys.argv[3] if len(sys.argv) > 3 else ""

    # 读取输入
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 转换
    converter = SQL2ShConverter()
    script = converter.convert(content, description)

    # 输出
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(script)
        os.chmod(output_file, 0o755)
        print(f"已生成: {output_file}")
    else:
        print(script)


if __name__ == "__main__":
    main()
