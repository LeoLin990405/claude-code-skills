#!/usr/bin/env python3
"""
操作豆包聊天栏按钮的工具
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


class ButtonController(UnifiedCDP):
    """按钮控制器"""

    async def click_button_by_text(self, button_text: str):
        """通过按钮文本点击按钮"""
        js = f"""
        (function() {{
            let buttons = document.querySelectorAll('button');
            let targetButton = null;

            buttons.forEach(btn => {{
                if (btn.textContent.trim().includes({json.dumps(button_text)})) {{
                    targetButton = btn;
                }}
            }});

            if (!targetButton) {{
                return {{ error: "未找到包含文本 '{button_text}' 的按钮" }};
            }}

            targetButton.click();

            return {{
                success: true,
                text: targetButton.textContent.trim(),
                type: targetButton.type
            }};
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def click_button_by_index(self, button_index: int):
        """通过索引点击按钮"""
        js = f"""
        (function() {{
            let buttons = document.querySelectorAll('button');
            if ({button_index} >= buttons.length) {{
                return {{ error: "按钮索引超出范围" }};
            }}

            let button = buttons[{button_index}];
            button.click();

            return {{
                success: true,
                text: button.textContent.trim(),
                type: button.type,
                index: {button_index}
            }};
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def click_button_near_input(self, position: str = "right"):
        """点击输入框附近的按钮"""
        js = f"""
        (function() {{
            let input = document.querySelector('textarea.semi-input-textarea');
            if (!input) return {{ error: "未找到输入框" }};

            let inputRect = input.getBoundingClientRect();
            let allButtons = document.querySelectorAll('button');
            let targetButton = null;
            let minDistance = 999999;

            allButtons.forEach(btn => {{
                let btnRect = btn.getBoundingClientRect();

                // 根据位置参数选择按钮
                let distance;
                if ({json.dumps(position)} === 'right') {{
                    // 输入框右侧的按钮
                    if (btnRect.left > inputRect.right && btnRect.top >= inputRect.top && btnRect.top <= inputRect.bottom) {{
                        distance = btnRect.left - inputRect.right;
                    }}
                }} else if ({json.dumps(position)} === 'left') {{
                    // 输入框左侧的按钮
                    if (btnRect.right < inputRect.left && btnRect.top >= inputRect.top && btnRect.top <= inputRect.bottom) {{
                        distance = inputRect.left - btnRect.right;
                    }}
                }} else if ({json.dumps(position)} === 'below') {{
                    // 输入框下方的按钮
                    if (btnRect.top > inputRect.bottom) {{
                        distance = Math.abs(btnRect.left - inputRect.left) + (btnRect.top - inputRect.bottom);
                    }}
                }}

                if (distance !== undefined && distance < minDistance && btnRect.width > 0 && btnRect.height > 0) {{
                    minDistance = distance;
                    targetButton = btn;
                }}
            }});

            if (!targetButton) {{
                return {{ error: "未找到输入框{position}的按钮" }};
            }}

            targetButton.click();

            return {{
                success: true,
                text: targetButton.textContent.trim(),
                type: targetButton.type,
                position: {json.dumps(position)},
                distance: Math.round(minDistance)
            }};
        }})()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})

    async def list_buttons_near_input(self):
        """列出输入框附近的按钮"""
        js = """
        (function() {
            let input = document.querySelector('textarea.semi-input-textarea');
            if (!input) return { error: "未找到输入框" };

            let inputRect = input.getBoundingClientRect();
            let allButtons = document.querySelectorAll('button');
            let nearbyButtons = [];

            allButtons.forEach((btn, index) => {
                let btnRect = btn.getBoundingClientRect();
                let distance = Math.sqrt(
                    Math.pow(btnRect.left - inputRect.left, 2) +
                    Math.pow(btnRect.top - inputRect.bottom, 2)
                );

                if (distance < 200 && btnRect.width > 0 && btnRect.height > 0) {
                    nearbyButtons.push({
                        index: index,
                        text: btn.textContent.trim().substring(0, 20),
                        type: btn.type,
                        hasSVG: !!btn.querySelector('svg'),
                        distance: Math.round(distance)
                    });
                }
            });

            nearbyButtons.sort((a, b) => a.distance - b.distance);

            return {
                count: nearbyButtons.length,
                buttons: nearbyButtons.slice(0, 10)
            };
        })()
        """

        result = await self.execute_js(js)
        return result.get("result", {}).get("result", {}).get("value", {})


async def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='豆包按钮控制工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 列出输入框附近的按钮
  python3 button_controller.py doubao --list

  # 通过文本点击按钮
  python3 button_controller.py doubao --click-text "快速"

  # 通过索引点击按钮
  python3 button_controller.py doubao --click-index 78

  # 点击输入框右侧的按钮
  python3 button_controller.py doubao --click-near right

  # 点击输入框下方的按钮
  python3 button_controller.py doubao --click-near below
        """
    )

    parser.add_argument('ai', choices=['doubao', 'stepfun'],
                        help='AI 应用标识符')
    parser.add_argument('--list', action='store_true',
                        help='列出输入框附近的按钮')
    parser.add_argument('--click-text', type=str,
                        help='通过文本点击按钮')
    parser.add_argument('--click-index', type=int,
                        help='通过索引点击按钮')
    parser.add_argument('--click-near', choices=['left', 'right', 'below'],
                        help='点击输入框附近的按钮')

    args = parser.parse_args()

    # 创建按钮控制器
    controller = ButtonController(ai_type=args.ai, auto_clear=False)

    if not await controller.connect():
        sys.exit(1)

    try:
        if args.list:
            print("📋 列出输入框附近的按钮...\n")
            result = await controller.list_buttons_near_input()

            if result.get('error'):
                print(f"✗ {result['error']}")
            else:
                print(f"找到 {result['count']} 个按钮:\n")
                for btn in result['buttons']:
                    print(f"  [{btn['index']}] {btn['text'] if btn['text'] else '(无文本)'}")
                    print(f"      类型: {btn['type']}, 有SVG: {btn['hasSVG']}, 距离: {btn['distance']}px")

        elif args.click_text:
            print(f"🖱️  点击包含文本 '{args.click_text}' 的按钮...\n")
            result = await controller.click_button_by_text(args.click_text)

            if result.get('error'):
                print(f"✗ {result['error']}")
            else:
                print(f"✓ 成功点击按钮")
                print(f"  文本: {result['text']}")
                print(f"  类型: {result['type']}")

        elif args.click_index is not None:
            print(f"🖱️  点击按钮 #{args.click_index}...\n")
            result = await controller.click_button_by_index(args.click_index)

            if result.get('error'):
                print(f"✗ {result['error']}")
            else:
                print(f"✓ 成功点击按钮")
                print(f"  索引: {result['index']}")
                print(f"  文本: {result['text']}")
                print(f"  类型: {result['type']}")

        elif args.click_near:
            print(f"🖱️  点击输入框{args.click_near}的按钮...\n")
            result = await controller.click_button_near_input(args.click_near)

            if result.get('error'):
                print(f"✗ {result['error']}")
            else:
                print(f"✓ 成功点击按钮")
                print(f"  位置: {result['position']}")
                print(f"  文本: {result['text']}")
                print(f"  类型: {result['type']}")
                print(f"  距离: {result['distance']}px")

        else:
            print("请指定一个操作选项，使用 --help 查看帮助")

    finally:
        await controller.close()


if __name__ == "__main__":
    asyncio.run(main())
