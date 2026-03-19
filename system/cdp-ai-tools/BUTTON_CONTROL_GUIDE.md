# 豆包聊天栏按钮操作指南

## 概述

通过 CDP 可以操作豆包聊天栏下面的所有按钮，包括：
- 发送按钮
- 快捷功能按钮（快速、编程、数据分析等）
- 工具按钮（附件、表情等）
- 其他功能按钮

## 发现的按钮

根据探索结果，豆包聊天栏附近有以下按钮：

### 输入框正下方（距离 < 50px）
1. **发送按钮** - 无文本，有 SVG 图标
2. **快速按钮** - 文本"快速"，快捷功能

### 输入框下方（距离 50-200px）
3. **编程按钮** - 文本"编程"
4. **数据分析按钮** - 文本"数据分析"
5. **帮我写作按钮** - 文本"帮我写作"
6. **其他工具按钮** - 各种 SVG 图标按钮

## 使用方法

### 1. 列出所有按钮

```bash
cd ~/.claude/skills/cdp-ai-tools
python3 button_controller.py doubao --list
```

输出示例：
```
找到 12 个按钮:

  [78] (无文本)
      类型: button, 有SVG: True, 距离: 16px
  [79] (无文本)
      类型: submit, 有SVG: True, 距离: 16px
  [81] 快速
      类型: button, 有SVG: True, 距离: 48px
  [82] 快速
      类型: submit, 有SVG: True, 距离: 48px
  [83] 编程
      类型: submit, 有SVG: True, 距离: 124px
```

### 2. 通过文本点击按钮

```bash
# 点击"快速"按钮
python3 button_controller.py doubao --click-text "快速"

# 点击"编程"按钮
python3 button_controller.py doubao --click-text "编程"

# 点击"数据分析"按钮
python3 button_controller.py doubao --click-text "数据分析"

# 点击"帮我写作"按钮
python3 button_controller.py doubao --click-text "帮我写作"
```

### 3. 通过索引点击按钮

```bash
# 点击按钮 #78（通常是发送按钮）
python3 button_controller.py doubao --click-index 78

# 点击按钮 #81（快速按钮）
python3 button_controller.py doubao --click-index 81
```

### 4. 点击输入框附近的按钮

```bash
# 点击输入框右侧的按钮
python3 button_controller.py doubao --click-near right

# 点击输入框左侧的按钮
python3 button_controller.py doubao --click-near left

# 点击输入框下方的按钮
python3 button_controller.py doubao --click-near below
```

## 实际应用场景

### 场景 1：快速切换功能模式

```bash
# 切换到"快速"模式
python3 button_controller.py doubao --click-text "快速"

# 切换到"编程"模式
python3 button_controller.py doubao --click-text "编程"

# 切换到"数据分析"模式
python3 button_controller.py doubao --click-text "数据分析"
```

### 场景 2：自动化工作流

```bash
#!/bin/bash
# 自动化脚本示例

# 1. 切换到编程模式
python3 button_controller.py doubao --click-text "编程"

# 2. 发送消息
ai-chat doubao "请帮我写一个排序算法"

# 3. 等待响应
sleep 10

# 4. 切换到数据分析模式
python3 button_controller.py doubao --click-text "数据分析"

# 5. 发送另一个消息
ai-chat doubao "请分析这个算法的时间复杂度"
```

### 场景 3：批量操作

```python
#!/usr/bin/env python3
"""
批量点击按钮示例
"""

import asyncio
from button_controller import ButtonController

async def batch_operations():
    controller = ButtonController(ai_type='doubao', auto_clear=False)
    await controller.connect()

    # 依次点击多个按钮
    buttons = ["快速", "编程", "数据分析", "帮我写作"]

    for btn_text in buttons:
        print(f"点击按钮: {btn_text}")
        result = await controller.click_button_by_text(btn_text)
        print(f"结果: {result}")
        await asyncio.sleep(2)  # 等待2秒

    await controller.close()

if __name__ == "__main__":
    asyncio.run(batch_operations())
```

## 集成到 ai-chat 命令

可以扩展 ai-chat 命令来支持按钮操作：

```bash
# 发送消息并点击"编程"按钮
ai-chat doubao --mode "编程" "请帮我写代码"

# 发送消息并点击"数据分析"按钮
ai-chat doubao --mode "数据分析" "请分析这些数据"
```

## 技术细节

### 按钮定位方法

1. **通过文本内容**
   ```javascript
   let buttons = document.querySelectorAll('button');
   buttons.forEach(btn => {
       if (btn.textContent.includes('快速')) {
           btn.click();
       }
   });
   ```

2. **通过位置关系**
   ```javascript
   let input = document.querySelector('textarea.semi-input-textarea');
   let inputRect = input.getBoundingClientRect();
   // 计算按钮与输入框的距离
   ```

3. **通过索引**
   ```javascript
   let buttons = document.querySelectorAll('button');
   buttons[78].click();
   ```

### 按钮类型

- **type="button"** - 普通按钮
- **type="submit"** - 提交按钮
- **有 SVG 图标** - 图标按钮
- **有文本** - 文字按钮

## 注意事项

1. **按钮索引可能变化**
   - 页面更新后按钮索引可能改变
   - 建议使用文本或位置来定位按钮

2. **按钮可见性**
   - 某些按钮可能在特定状态下才可见
   - 点击前可以先列出按钮确认

3. **点击效果**
   - 点击按钮后可能触发页面变化
   - 建议等待一段时间再进行下一步操作

4. **应用版本**
   - 不同版本的豆包可能有不同的按钮布局
   - 需要根据实际情况调整

## 扩展功能

### 添加新的按钮操作

在 `button_controller.py` 中添加新方法：

```python
async def click_attachment_button(self):
    """点击附件按钮"""
    js = """
    (function() {
        // 查找附件按钮（通常有特定的 aria-label 或图标）
        let buttons = document.querySelectorAll('button');
        let attachBtn = null;

        buttons.forEach(btn => {
            let ariaLabel = btn.getAttribute('aria-label');
            if (ariaLabel && ariaLabel.includes('附件')) {
                attachBtn = btn;
            }
        });

        if (!attachBtn) return { error: "未找到附件按钮" };

        attachBtn.click();
        return { success: true };
    })()
    """

    result = await self.execute_js(js)
    return result.get("result", {}).get("result", {}).get("value", {})
```

### 监听按钮状态

```python
async def watch_button_state(self, button_text: str):
    """监听按钮状态变化"""
    js = f"""
    (function() {{
        let buttons = document.querySelectorAll('button');
        let targetButton = null;

        buttons.forEach(btn => {{
            if (btn.textContent.includes({json.dumps(button_text)})) {{
                targetButton = btn;
            }}
        }});

        if (!targetButton) return {{ error: "未找到按钮" }};

        return {{
            text: targetButton.textContent.trim(),
            disabled: targetButton.disabled,
            visible: targetButton.offsetWidth > 0,
            className: targetButton.className
        }};
    }})()
    """

    result = await self.execute_js(js)
    return result.get("result", {}).get("result", {}).get("value", {})
```

## 总结

✅ **可以操作的按钮：**
- 发送按钮
- 快捷功能按钮（快速、编程、数据分析等）
- 工具按钮
- 所有可见的按钮

✅ **操作方式：**
- 通过文本点击
- 通过索引点击
- 通过位置点击

✅ **应用场景：**
- 切换功能模式
- 自动化工作流
- 批量操作
- 集成到其他工具

**理论上，页面上所有可见的按钮都可以通过 CDP 操作！**
