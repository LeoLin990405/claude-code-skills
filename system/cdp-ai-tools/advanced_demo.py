#!/usr/bin/env python3
"""
CDP AI Tools - 扩展功能示例
演示如何实现对话管理、内容操作等高级功能
"""

import asyncio
import json
import sys
from pathlib import Path

# 导入统一 CDP 模块
SCRIPT_PATH = Path(__file__).resolve()
SKILL_DIR = SCRIPT_PATH.parent
LIB_DIR = SKILL_DIR / "lib"

import importlib.util
spec = importlib.util.spec_from_file_location("unified_cdp", LIB_DIR / "unified_cdp.py")
unified_cdp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(unified_cdp)
UnifiedCDP = unified_cdp.UnifiedCDP


class ExtendedCDP(UnifiedCDP):
    """扩展的 CDP 客户端，包含更多功能"""

    async def get_conversation_list(self):
        """获取对话历史列表"""
        js = """
        (function() {
            let conversations = [];

            // 尝试多种可能的选择器
            let selectors = [
                '[class*="conversation"]',
                '[class*="chat-item"]',
                '[class*="history-item"]',
                '[role="listitem"]'
            ];

            for (let selector of selectors) {
                let items = document.querySelectorAll(selector);
                if (items.length > 0) {
                    items.forEach((item, index) => {
                        let title = item.querySelector('[class*="title"]')?.textContent ||
                                   item.textContent.substring(0, 50);
                        conversations.push({
                            index: index,
                            title: title.trim(),
                            element: selector
                        });
                    });
                    break;
                }
            }

            return {
                count: conversations.length,
                conversations: conversations.slice(0, 20)  // 返回前20个
            };
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def copy_last_response(self):
        """复制最后一条AI响应到剪贴板"""
        js = """
        (function() {
            // 尝试多种选择器找到消息
            let selectors = [
                '[class*="message"]',
                '[class*="response"]',
                '[class*="answer"]',
                '[role="article"]'
            ];

            for (let selector of selectors) {
                let messages = document.querySelectorAll(selector);
                if (messages.length > 0) {
                    let lastMessage = messages[messages.length - 1];
                    let text = lastMessage.textContent.trim();

                    // 复制到剪贴板
                    navigator.clipboard.writeText(text);

                    return {
                        success: true,
                        length: text.length,
                        preview: text.substring(0, 100)
                    };
                }
            }

            return { error: "未找到消息" };
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def search_in_conversation(self, keyword: str):
        """在当前对话中搜索关键词"""
        js = f"""
        (function() {{
            let keyword = {json.dumps(keyword)};
            let results = [];

            // 查找所有可能包含文本的元素
            let elements = document.querySelectorAll('div, p, span');

            elements.forEach((el, index) => {{
                let text = el.textContent.trim();
                if (text.length > 20 && text.includes(keyword)) {{
                    // 避免重复（检查是否是子元素的文本）
                    let isUnique = true;
                    results.forEach(r => {{
                        if (r.text.includes(text) || text.includes(r.text)) {{
                            isUnique = false;
                        }}
                    }});

                    if (isUnique) {{
                        results.push({{
                            index: results.length,
                            preview: text.substring(0, 150),
                            length: text.length
                        }});
                    }}
                }}
            }});

            return {{
                keyword: keyword,
                count: results.length,
                results: results.slice(0, 10)  // 返回前10个结果
            }};
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def export_conversation(self):
        """导出当前对话内容"""
        js = """
        (function() {
            let messages = [];

            // 尝试多种选择器
            let selectors = [
                '[class*="message"]',
                '[class*="chat-message"]',
                '[role="article"]'
            ];

            for (let selector of selectors) {
                let elements = document.querySelectorAll(selector);
                if (elements.length > 0) {
                    elements.forEach((el, index) => {
                        let text = el.textContent.trim();
                        if (text.length > 10) {
                            messages.push({
                                index: index,
                                text: text
                            });
                        }
                    });
                    break;
                }
            }

            // 格式化为文本
            let content = messages.map(msg =>
                `[消息 ${msg.index + 1}]\\n${msg.text}\\n`
            ).join('\\n');

            return {
                messageCount: messages.length,
                content: content,
                length: content.length
            };
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def get_page_info(self):
        """获取页面基本信息"""
        js = """
        (function() {
            return {
                title: document.title,
                url: window.location.href,
                readyState: document.readyState,
                elementCount: document.querySelectorAll('*').length,
                textLength: document.body.textContent.length
            };
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})


async def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='CDP AI Tools - 扩展功能演示',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
功能演示:
  python3 advanced_demo.py doubao --list-conversations
  python3 advanced_demo.py doubao --copy-last
  python3 advanced_demo.py doubao --search "递归"
  python3 advanced_demo.py doubao --export
  python3 advanced_demo.py doubao --info
        """
    )

    parser.add_argument('ai', choices=['doubao', 'stepfun'],
                        help='AI 应用标识符')
    parser.add_argument('--list-conversations', action='store_true',
                        help='列出对话历史')
    parser.add_argument('--copy-last', action='store_true',
                        help='复制最后一条响应')
    parser.add_argument('--search', type=str,
                        help='搜索关键词')
    parser.add_argument('--export', action='store_true',
                        help='导出当前对话')
    parser.add_argument('--info', action='store_true',
                        help='获取页面信息')

    args = parser.parse_args()

    # 创建扩展 CDP 实例
    cdp = ExtendedCDP(ai_type=args.ai, auto_clear=False)

    if not await cdp.connect():
        sys.exit(1)

    try:
        if args.list_conversations:
            print("📋 获取对话历史列表...\n")
            result = await cdp.get_conversation_list()
            print(f"找到 {result.get('count', 0)} 个对话:\n")
            for conv in result.get('conversations', []):
                print(f"  [{conv['index']}] {conv['title']}")

        elif args.copy_last:
            print("📋 复制最后一条响应...\n")
            result = await cdp.copy_last_response()
            if result.get('success'):
                print(f"✓ 已复制 {result['length']} 字符到剪贴板")
                print(f"预览: {result['preview']}...")
            else:
                print(f"✗ {result.get('error', '未知错误')}")

        elif args.search:
            print(f"🔍 搜索关键词: {args.search}\n")
            result = await cdp.search_in_conversation(args.search)
            print(f"找到 {result.get('count', 0)} 个结果:\n")
            for item in result.get('results', []):
                print(f"  [{item['index']}] ({item['length']}字符)")
                print(f"      {item['preview']}...")
                print()

        elif args.export:
            print("📤 导出当前对话...\n")
            result = await cdp.export_conversation()
            print(f"✓ 导出 {result.get('messageCount', 0)} 条消息")
            print(f"总长度: {result.get('length', 0)} 字符\n")

            # 保存到文件
            filename = f"conversation_{args.ai}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result.get('content', ''))
            print(f"✓ 已保存到: {filename}")

        elif args.info:
            print("ℹ️  获取页面信息...\n")
            result = await cdp.get_page_info()
            print(f"标题: {result.get('title', 'N/A')}")
            print(f"URL: {result.get('url', 'N/A')}")
            print(f"状态: {result.get('readyState', 'N/A')}")
            print(f"元素数量: {result.get('elementCount', 0)}")
            print(f"文本长度: {result.get('textLength', 0)} 字符")

        else:
            print("请指定一个操作选项，使用 --help 查看帮助")

    finally:
        await cdp.close()


if __name__ == "__main__":
    asyncio.run(main())
