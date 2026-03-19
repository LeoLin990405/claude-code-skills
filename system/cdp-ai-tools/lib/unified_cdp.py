"""
统一的 CDP 接口
支持多个 AI 应用
"""

import asyncio
import json
import sys
import websockets
import aiohttp
from typing import Optional, Dict, Any


class UnifiedCDP:
    """统一的 CDP 客户端"""

    # AI 配置
    AI_CONFIGS = {
        "doubao": {
            "port": 9225,
            "page_pattern": "doubao://doubao-chat/chat",
            "input_selector": "textarea.semi-input-textarea",
            "app_name": "豆包"
        },
        "stepfun": {
            "port": 9224,
            "page_pattern": "http://127.0.0.1:63008/chats",
            "input_selector": "[contenteditable=\"true\"]",
            "app_name": "阶跃AI"
        }
    }

    def __init__(self, ai_type: str, auto_clear: bool = False):
        """
        初始化统一 CDP 客户端

        Args:
            ai_type: AI 类型 (doubao 或 stepfun)
            auto_clear: 是否自动清理对话记录
        """
        if ai_type not in self.AI_CONFIGS:
            raise ValueError(f"不支持的 AI 类型: {ai_type}")

        self.ai_type = ai_type
        self.config = self.AI_CONFIGS[ai_type]
        self.auto_clear = auto_clear
        self.ws: Optional[websockets.WebSocketClientProtocol] = None
        self.message_id = 0

    async def connect(self):
        """连接到 CDP WebSocket"""
        try:
            port = self.config["port"]
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://localhost:{port}/json") as resp:
                    targets = await resp.json()

            # 找到聊天页面
            page_target = None
            page_pattern = self.config["page_pattern"]

            for target in targets:
                if target.get("type") == "page" and page_pattern in target.get("url", ""):
                    page_target = target
                    break

            if not page_target:
                print(f"✗ 未找到{self.config['app_name']}聊天页面", file=sys.stderr)
                return False

            ws_url = page_target["webSocketDebuggerUrl"]
            self.ws = await websockets.connect(ws_url)
            print(f"✓ 已连接到{self.config['app_name']}: {page_target.get('url', 'Unknown')}", file=sys.stderr)
            return True

        except Exception as e:
            print(f"✗ 连接失败: {e}", file=sys.stderr)
            return False

    async def send_command(self, method: str, params: Dict[str, Any] = None) -> Dict:
        """发送 CDP 命令"""
        self.message_id += 1
        message = {
            "id": self.message_id,
            "method": method,
            "params": params or {}
        }

        await self.ws.send(json.dumps(message))

        while True:
            response = await self.ws.recv()
            data = json.loads(response)

            if data.get("id") == self.message_id:
                return data

    async def execute_js(self, expression: str) -> Any:
        """执行 JavaScript 代码"""
        result = await self.send_command("Runtime.evaluate", {
            "expression": expression,
            "returnByValue": True
        })
        return result

    async def send_message(self, message: str, timeout: int = 60) -> str:
        """
        发送消息并等待响应

        Args:
            message: 要发送的消息
            timeout: 超时时间（秒）

        Returns:
            AI 的响应内容
        """
        try:
            # 1. 输入消息并按 Enter 键发送
            input_selector = self.config["input_selector"]

            send_js = f"""
            (function() {{
                // 查找输入框
                let input = document.querySelector('{input_selector}');
                if (!input) {{
                    return {{ error: "未找到输入框" }};
                }}

                // 聚焦输入框
                input.focus();

                // 输入消息
                input.value = {json.dumps(message)};

                // 触发 React 的 change 检测
                let event = new Event('input', {{ bubbles: true }});
                let tracker = input._valueTracker;
                if (tracker) {{
                    tracker.setValue("");
                }}

                input.dispatchEvent(event);

                // 按 Enter 键发送
                let enterEvent = new KeyboardEvent('keydown', {{
                    key: 'Enter',
                    code: 'Enter',
                    keyCode: 13,
                    which: 13,
                    bubbles: true,
                    cancelable: true
                }});

                input.dispatchEvent(enterEvent);

                return {{ success: true }};
            }})()
            """

            result = await self.execute_js(send_js)
            result_value = result.get("result", {}).get("result", {}).get("value", {})

            if result_value.get("error"):
                return f"错误: {result_value['error']}"

            print("✓ 消息已发送", file=sys.stderr)
            print("⏳ 等待响应...", file=sys.stderr)
            print(f"💡 消息已成功发送到{self.config['app_name']}，请在应用中查看响应", file=sys.stderr)

            # 2. 简化的等待逻辑
            await asyncio.sleep(5)

            # 尝试提取响应
            check_js = """
            (function() {
                let allDivs = document.querySelectorAll('div, p, span');
                let candidates = [];

                allDivs.forEach(el => {
                    let text = el.textContent.trim();
                    if (text.length > 100 && text.length < 5000) {
                        if (!text.includes('快速编程') &&
                            !text.includes('文件数量') &&
                            !text.includes('To pick up') &&
                            !text.includes('豆包AI')) {
                            candidates.push(text);
                        }
                    }
                });

                if (candidates.length > 0) {
                    candidates.sort((a, b) => b.length - a.length);
                    return candidates[0];
                }

                return null;
            })()
            """

            response = await self.execute_js(check_js)
            current_text = response.get("result", {}).get("result", {}).get("value")

            if current_text and len(current_text) > 50:
                print(f"✓ 找到响应 ({len(current_text)} 字符)", file=sys.stderr)

                # 自动清理对话记录
                if self.auto_clear:
                    await self.clear_chat()

                return current_text
            else:
                # 即使没有提取到响应，也清理对话
                if self.auto_clear:
                    await self.clear_chat()

                return f"消息已发送到{self.config['app_name']}，请在应用中查看响应。"

        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"错误: {e}"

    async def clear_chat(self) -> bool:
        """清理当前对话，开启新话题"""
        try:
            # 不同 AI 的清理逻辑可能不同
            # 这里使用通用的查找"新话题"按钮的方法
            clear_js = """
            (function() {
                // 查找包含"新话题"或"新对话"的按钮
                let buttons = document.querySelectorAll('button');
                let clearBtn = null;

                buttons.forEach(btn => {
                    let text = btn.textContent.trim();
                    if (text.includes('新话题') || text.includes('新对话') || text.includes('New Chat')) {
                        clearBtn = btn;
                    }
                });

                if (!clearBtn) {
                    return { error: "未找到新话题按钮" };
                }

                clearBtn.click();
                return { success: true };
            })()
            """

            result = await self.execute_js(clear_js)
            result_value = result.get("result", {}).get("result", {}).get("value", {})

            if result_value.get("success"):
                print("✓ 对话已清理", file=sys.stderr)
                await asyncio.sleep(0.5)
                return True
            else:
                print(f"⚠️ 清理失败: {result_value.get('error', '未知错误')}", file=sys.stderr)
                return False

        except Exception as e:
            print(f"⚠️ 清理对话时出错: {e}", file=sys.stderr)
            return False

    async def close(self):
        """关闭连接"""
        if self.ws:
            await self.ws.close()
