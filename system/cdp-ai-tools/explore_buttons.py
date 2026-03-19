#!/usr/bin/env python3
"""
探索豆包聊天栏下面的按钮
"""

import asyncio
import json
import websockets
import aiohttp


async def explore_buttons():
    """探索聊天栏按钮"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:9225/json") as resp:
                targets = await resp.json()

        # 找到聊天页面
        chat_target = None
        for target in targets:
            if "doubao-chat/chat" in target.get("url", ""):
                chat_target = target
                break

        if not chat_target:
            print("未找到聊天页面")
            return

        ws = await websockets.connect(chat_target["webSocketDebuggerUrl"])

        # 查找输入框附近的所有按钮
        js = """
        (function() {
            let input = document.querySelector('textarea.semi-input-textarea');
            if (!input) return { error: "未找到输入框" };

            let inputRect = input.getBoundingClientRect();
            let allButtons = document.querySelectorAll('button');
            let nearbyButtons = [];

            allButtons.forEach((btn, index) => {
                let btnRect = btn.getBoundingClientRect();

                // 计算按钮与输入框的距离
                let verticalDistance = Math.abs(btnRect.top - inputRect.bottom);
                let horizontalDistance = Math.abs(btnRect.left - inputRect.left);

                // 查找输入框下方和周围的按钮（距离小于150px）
                if (verticalDistance < 150 || horizontalDistance < 300) {
                    // 获取按钮的详细信息
                    let buttonInfo = {
                        index: index,
                        text: btn.textContent.trim().substring(0, 50),
                        type: btn.type || 'button',
                        className: btn.className.substring(0, 100),
                        ariaLabel: btn.getAttribute('aria-label'),
                        title: btn.title,
                        disabled: btn.disabled,
                        visible: btnRect.width > 0 && btnRect.height > 0,
                        position: {
                            top: Math.round(btnRect.top),
                            left: Math.round(btnRect.left),
                            width: Math.round(btnRect.width),
                            height: Math.round(btnRect.height)
                        },
                        verticalDistance: Math.round(verticalDistance),
                        horizontalDistance: Math.round(horizontalDistance),
                        hasSVG: !!btn.querySelector('svg'),
                        hasImage: !!btn.querySelector('img')
                    };

                    nearbyButtons.push(buttonInfo);
                }
            });

            // 按距离排序
            nearbyButtons.sort((a, b) => {
                let distA = Math.sqrt(a.verticalDistance ** 2 + a.horizontalDistance ** 2);
                let distB = Math.sqrt(b.verticalDistance ** 2 + b.horizontalDistance ** 2);
                return distA - distB;
            });

            return {
                inputPosition: {
                    top: Math.round(inputRect.top),
                    left: Math.round(inputRect.left),
                    width: Math.round(inputRect.width),
                    height: Math.round(inputRect.height)
                },
                totalButtons: nearbyButtons.length,
                buttons: nearbyButtons.slice(0, 20)  // 返回前20个最近的按钮
            };
        })()
        """

        msg = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": js,
                "returnByValue": True
            }
        }

        await ws.send(json.dumps(msg))
        resp = await ws.recv()
        data = json.loads(resp)

        if "result" in data and "result" in data["result"]:
            result = data["result"]["result"]["value"]

            if result.get("error"):
                print(f"错误: {result['error']}")
                return

            print("\n" + "=" * 80)
            print("豆包聊天栏按钮探索")
            print("=" * 80)

            print(f"\n输入框位置:")
            pos = result["inputPosition"]
            print(f"  位置: ({pos['left']}, {pos['top']})")
            print(f"  尺寸: {pos['width']} x {pos['height']}")

            print(f"\n找到 {result['totalButtons']} 个附近的按钮:\n")

            for i, btn in enumerate(result["buttons"], 1):
                print(f"[{i}] 按钮 #{btn['index']}")
                print(f"    文本: {btn['text'] if btn['text'] else '(无文本)'}")
                print(f"    类型: {btn['type']}")
                print(f"    aria-label: {btn['ariaLabel'] if btn['ariaLabel'] else '(无)'}")
                print(f"    title: {btn['title'] if btn['title'] else '(无)'}")
                print(f"    禁用: {btn['disabled']}")
                print(f"    可见: {btn['visible']}")
                print(f"    有SVG: {btn['hasSVG']}")
                print(f"    有图片: {btn['hasImage']}")
                print(f"    位置: ({btn['position']['left']}, {btn['position']['top']})")
                print(f"    尺寸: {btn['position']['width']} x {btn['position']['height']}")
                print(f"    距离输入框: 垂直 {btn['verticalDistance']}px, 水平 {btn['horizontalDistance']}px")
                print(f"    class: {btn['className'][:80]}...")
                print()

        await ws.close()

    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(explore_buttons())
