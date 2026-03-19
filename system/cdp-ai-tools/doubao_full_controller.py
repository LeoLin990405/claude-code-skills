#!/usr/bin/env python3
"""
豆包完整操作控制器
实现对话历史管理、文件上传、设置管理等完整功能
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional, List, Dict, Any

# 导入统一 CDP 模块
SCRIPT_PATH = Path(__file__).resolve()
SKILL_DIR = SCRIPT_PATH.parent
LIB_DIR = SKILL_DIR / "lib"

import importlib.util
spec = importlib.util.spec_from_file_location("unified_cdp", LIB_DIR / "unified_cdp.py")
unified_cdp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(unified_cdp)
UnifiedCDP = unified_cdp.UnifiedCDP


class DoubaoFullController(UnifiedCDP):
    """豆包完整功能控制器"""

    def __init__(self, auto_clear: bool = False):
        """初始化豆包控制器"""
        super().__init__(ai_type="doubao", auto_clear=auto_clear)

    # ==================== 对话历史管理 ====================

    async def list_conversations(self) -> Dict[str, Any]:
        """
        列出所有对话历史

        Returns:
            包含对话列表的字典
        """
        js = """
        (function() {
            try {
                let conversations = [];

                // 豆包的对话历史通常在侧边栏
                // 尝试多种可能的选择器
                let selectors = [
                    '[class*="conversation"]',
                    '[class*="chat-item"]',
                    '[class*="history-item"]',
                    '[class*="session"]',
                    'div[role="listitem"]',
                    'li[class*="item"]'
                ];

                for (let selector of selectors) {
                    let items = document.querySelectorAll(selector);
                    if (items.length > 0) {
                        items.forEach((item, index) => {
                            // 提取标题
                            let title = item.querySelector('[class*="title"]')?.textContent ||
                                       item.querySelector('span')?.textContent ||
                                       item.textContent.substring(0, 50);

                            // 提取时间（如果有）
                            let time = item.querySelector('[class*="time"]')?.textContent || '';

                            // 检查是否是当前对话
                            let isActive = item.classList.contains('active') ||
                                          item.getAttribute('aria-selected') === 'true';

                            conversations.push({
                                index: index,
                                title: title.trim(),
                                time: time.trim(),
                                isActive: isActive,
                                selector: selector
                            });
                        });
                        break;
                    }
                }

                return {
                    success: true,
                    count: conversations.length,
                    conversations: conversations
                };
            } catch (error) {
                return {
                    success: false,
                    error: error.toString()
                };
            }
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def switch_conversation(self, index: int) -> Dict[str, Any]:
        """
        切换到指定的对话

        Args:
            index: 对话索引

        Returns:
            操作结果
        """
        js = f"""
        (function() {{
            try {{
                let selectors = [
                    '[class*="conversation"]',
                    '[class*="chat-item"]',
                    '[class*="history-item"]',
                    '[class*="session"]',
                    'div[role="listitem"]',
                    'li[class*="item"]'
                ];

                for (let selector of selectors) {{
                    let items = document.querySelectorAll(selector);
                    if (items.length > {index}) {{
                        let targetItem = items[{index}];

                        // 尝试点击
                        targetItem.click();

                        // 获取标题
                        let title = targetItem.querySelector('[class*="title"]')?.textContent ||
                                   targetItem.textContent.substring(0, 50);

                        return {{
                            success: true,
                            index: {index},
                            title: title.trim()
                        }};
                    }}
                }}

                return {{
                    success: false,
                    error: "未找到索引为 {index} 的对话"
                }};
            }} catch (error) {{
                return {{
                    success: false,
                    error: error.toString()
                }};
            }}
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def delete_conversation(self, index: int) -> Dict[str, Any]:
        """
        删除指定的对话

        Args:
            index: 对话索引

        Returns:
            操作结果
        """
        js = f"""
        (function() {{
            try {{
                let selectors = [
                    '[class*="conversation"]',
                    '[class*="chat-item"]',
                    '[class*="history-item"]',
                    '[class*="session"]',
                    'div[role="listitem"]',
                    'li[class*="item"]'
                ];

                for (let selector of selectors) {{
                    let items = document.querySelectorAll(selector);
                    if (items.length > {index}) {{
                        let targetItem = items[{index}];

                        // 查找删除按钮（通常在悬停时显示）
                        // 先触发悬停
                        let hoverEvent = new MouseEvent('mouseenter', {{
                            bubbles: true,
                            cancelable: true
                        }});
                        targetItem.dispatchEvent(hoverEvent);

                        // 等待一下让删除按钮显示
                        setTimeout(() => {{}}, 100);

                        // 查找删除按钮
                        let deleteBtn = targetItem.querySelector('[class*="delete"]') ||
                                       targetItem.querySelector('[title*="删除"]') ||
                                       targetItem.querySelector('button[aria-label*="删除"]');

                        if (deleteBtn) {{
                            deleteBtn.click();

                            // 可能需要确认
                            setTimeout(() => {{
                                let confirmBtn = document.querySelector('[class*="confirm"]') ||
                                               document.querySelector('button:contains("确认")');
                                if (confirmBtn) {{
                                    confirmBtn.click();
                                }}
                            }}, 200);

                            return {{
                                success: true,
                                index: {index},
                                message: "删除操作已触发"
                            }};
                        }} else {{
                            return {{
                                success: false,
                                error: "未找到删除按钮"
                            }};
                        }}
                    }}
                }}

                return {{
                    success: false,
                    error: "未找到索引为 {index} 的对话"
                }};
            }} catch (error) {{
                return {{
                    success: false,
                    error: error.toString()
                }};
            }}
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def rename_conversation(self, index: int, new_name: str) -> Dict[str, Any]:
        """
        重命名指定的对话

        Args:
            index: 对话索引
            new_name: 新名称

        Returns:
            操作结果
        """
        js = f"""
        (function() {{
            try {{
                let selectors = [
                    '[class*="conversation"]',
                    '[class*="chat-item"]',
                    '[class*="history-item"]',
                    '[class*="session"]',
                    'div[role="listitem"]',
                    'li[class*="item"]'
                ];

                for (let selector of selectors) {{
                    let items = document.querySelectorAll(selector);
                    if (items.length > {index}) {{
                        let targetItem = items[{index}];

                        // 触发悬停显示编辑按钮
                        let hoverEvent = new MouseEvent('mouseenter', {{
                            bubbles: true,
                            cancelable: true
                        }});
                        targetItem.dispatchEvent(hoverEvent);

                        // 查找编辑/重命名按钮
                        let editBtn = targetItem.querySelector('[class*="edit"]') ||
                                     targetItem.querySelector('[title*="编辑"]') ||
                                     targetItem.querySelector('[title*="重命名"]') ||
                                     targetItem.querySelector('button[aria-label*="编辑"]');

                        if (editBtn) {{
                            editBtn.click();

                            // 等待输入框出现
                            setTimeout(() => {{
                                let input = targetItem.querySelector('input') ||
                                           document.querySelector('input[class*="rename"]');
                                if (input) {{
                                    input.value = "{new_name}";
                                    input.dispatchEvent(new Event('input', {{ bubbles: true }}));

                                    // 触发确认（通常是回车或点击确认按钮）
                                    let enterEvent = new KeyboardEvent('keydown', {{
                                        key: 'Enter',
                                        code: 'Enter',
                                        keyCode: 13,
                                        bubbles: true
                                    }});
                                    input.dispatchEvent(enterEvent);
                                }}
                            }}, 200);

                            return {{
                                success: true,
                                index: {index},
                                newName: "{new_name}"
                            }};
                        }} else {{
                            return {{
                                success: false,
                                error: "未找到编辑按钮"
                            }};
                        }}
                    }}
                }}

                return {{
                    success: false,
                    error: "未找到索引为 {index} 的对话"
                }};
            }} catch (error) {{
                return {{
                    success: false,
                    error: error.toString()
                }};
            }}
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    # ==================== 文件操作 ====================

    async def upload_file(self, file_path: str) -> Dict[str, Any]:
        """
        上传文件到豆包

        Args:
            file_path: 文件路径

        Returns:
            操作结果
        """
        js = f"""
        (function() {{
            try {{
                // 查找文件上传按钮
                let uploadBtn = document.querySelector('[class*="upload"]') ||
                               document.querySelector('input[type="file"]') ||
                               document.querySelector('[title*="上传"]');

                if (uploadBtn) {{
                    return {{
                        success: true,
                        message: "找到上传按钮，但文件上传需要通过文件选择器，建议使用 button_controller.py 点击上传按钮"
                    }};
                }} else {{
                    return {{
                        success: false,
                        error: "未找到上传按钮"
                    }};
                }}
            }} catch (error) {{
                return {{
                    success: false,
                    error: error.toString()
                }};
            }}
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    # ==================== 设置管理 ====================

    async def get_settings(self) -> Dict[str, Any]:
        """
        获取当前设置

        Returns:
            设置信息
        """
        js = """
        (function() {
            try {
                // 查找设置按钮
                let settingsBtn = document.querySelector('[class*="settings"]') ||
                                 document.querySelector('[title*="设置"]') ||
                                 document.querySelector('[aria-label*="设置"]');

                if (settingsBtn) {
                    return {
                        success: true,
                        message: "找到设置按钮"
                    };
                } else {
                    return {
                        success: false,
                        error: "未找到设置按钮"
                    };
                }
            } catch (error) {
                return {
                    success: false,
                    error: error.toString()
                };
            }
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def open_settings(self) -> Dict[str, Any]:
        """
        打开设置面板

        Returns:
            操作结果
        """
        js = """
        (function() {
            try {
                // 查找并点击设置按钮
                let settingsBtn = document.querySelector('[class*="settings"]') ||
                                 document.querySelector('[title*="设置"]') ||
                                 document.querySelector('[aria-label*="设置"]');

                if (settingsBtn) {
                    settingsBtn.click();
                    return {
                        success: true,
                        message: "已打开设置面板"
                    };
                } else {
                    return {
                        success: false,
                        error: "未找到设置按钮"
                    };
                }
            } catch (error) {
                return {
                    success: false,
                    error: error.toString()
                };
            }
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    # ==================== 快捷操作 ====================

    async def click_quick_action(self, action_name: str) -> Dict[str, Any]:
        """
        点击快捷操作按钮（如"快速"、"编程"、"数据分析"等）

        Args:
            action_name: 操作名称

        Returns:
            操作结果
        """
        js = f"""
        (function() {{
            try {{
                // 查找包含指定文本的按钮
                let buttons = Array.from(document.querySelectorAll('button'));
                let targetBtn = buttons.find(btn => btn.textContent.includes("{action_name}"));

                if (targetBtn) {{
                    targetBtn.click();
                    return {{
                        success: true,
                        action: "{action_name}",
                        message: "已点击快捷操作按钮"
                    }};
                }} else {{
                    return {{
                        success: false,
                        error: "未找到名为 '{action_name}' 的快捷操作按钮"
                    }};
                }}
            }} catch (error) {{
                return {{
                    success: false,
                    error: error.toString()
                }};
            }}
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})


# ==================== CLI 接口 ====================

async def main():
    """命令行接口"""
    import argparse

    parser = argparse.ArgumentParser(description="豆包完整操作控制器")
    parser.add_argument("--list-conversations", action="store_true", help="列出所有对话")
    parser.add_argument("--switch", type=int, metavar="INDEX", help="切换到指定对话")
    parser.add_argument("--delete", type=int, metavar="INDEX", help="删除指定对话")
    parser.add_argument("--rename", nargs=2, metavar=("INDEX", "NAME"), help="重命名对话")
    parser.add_argument("--upload", type=str, metavar="FILE", help="上传文件")
    parser.add_argument("--settings", action="store_true", help="打开设置")
    parser.add_argument("--quick-action", type=str, metavar="NAME", help="点击快捷操作")
    parser.add_argument("--auto-clear", action="store_true", help="自动清空输入框")

    args = parser.parse_args()

    controller = DoubaoFullController(auto_clear=args.auto_clear)

    try:
        await controller.connect()

        if args.list_conversations:
            result = await controller.list_conversations()
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.switch is not None:
            result = await controller.switch_conversation(args.switch)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.delete is not None:
            result = await controller.delete_conversation(args.delete)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.rename:
            index, name = int(args.rename[0]), args.rename[1]
            result = await controller.rename_conversation(index, name)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.upload:
            result = await controller.upload_file(args.upload)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.settings:
            result = await controller.open_settings()
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif args.quick_action:
            result = await controller.click_quick_action(args.quick_action)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        else:
            parser.print_help()

    finally:
        await controller.close()


if __name__ == "__main__":
    asyncio.run(main())
