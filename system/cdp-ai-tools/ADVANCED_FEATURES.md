# CDP AI Tools - 扩展功能指南

## CDP 能力范围

通过 Chrome DevTools Protocol (CDP)，我们可以：

### ✅ 已实现的功能

1. **发送消息** - 输入文本并发送
2. **连续对话** - 保持对话上下文
3. **清理对话** - 点击"新话题"按钮

### 🚀 可以实现的其他功能

#### 1. 对话管理

**查看对话历史**
```javascript
// 获取所有对话列表
let conversations = document.querySelectorAll('[class*="conversation"]');
conversations.forEach(conv => {
    console.log(conv.textContent);
});
```

**切换对话**
```javascript
// 点击特定对话
let targetConv = document.querySelector('[data-conversation-id="xxx"]');
targetConv.click();
```

**删除对话**
```javascript
// 找到删除按钮并点击
let deleteBtn = document.querySelector('[aria-label="删除对话"]');
deleteBtn.click();
```

**重命名对话**
```javascript
// 找到重命名输入框
let renameInput = document.querySelector('[class*="rename"]');
renameInput.value = "新名称";
renameInput.dispatchEvent(new Event('input', { bubbles: true }));
```

#### 2. 内容操作

**复制响应内容**
```javascript
// 获取最后一条AI响应
let lastResponse = document.querySelector('[class*="message"]:last-child');
navigator.clipboard.writeText(lastResponse.textContent);
```

**导出对话**
```javascript
// 获取完整对话内容
let messages = document.querySelectorAll('[class*="message"]');
let conversation = Array.from(messages).map(msg => msg.textContent).join('\n\n');
// 下载为文件
let blob = new Blob([conversation], { type: 'text/plain' });
let url = URL.createObjectURL(blob);
let a = document.createElement('a');
a.href = url;
a.download = 'conversation.txt';
a.click();
```

**搜索对话**
```javascript
// 在当前对话中搜索关键词
let keyword = "递归";
let messages = document.querySelectorAll('[class*="message"]');
let results = Array.from(messages).filter(msg =>
    msg.textContent.includes(keyword)
);
```

#### 3. 设置和配置

**切换模型**（如果应用支持）
```javascript
// 找到模型选择器
let modelSelector = document.querySelector('[class*="model-selector"]');
modelSelector.click();
// 选择特定模型
let targetModel = document.querySelector('[data-model="gpt-4"]');
targetModel.click();
```

**修改设置**
```javascript
// 打开设置面板
let settingsBtn = document.querySelector('[aria-label="设置"]');
settingsBtn.click();

// 修改某个设置
let option = document.querySelector('[data-setting="temperature"]');
option.value = "0.7";
```

#### 4. 文件操作

**上传文件**
```javascript
// 触发文件上传
let fileInput = document.querySelector('input[type="file"]');
// 需要通过CDP的文件上传API
```

**下载生成的文件**
```javascript
// 点击下载按钮
let downloadBtn = document.querySelector('[class*="download"]');
downloadBtn.click();
```

#### 5. 高级功能

**截图当前对话**
```javascript
// 使用CDP的截图功能
// 需要通过CDP API调用
```

**监听网络请求**
```javascript
// 拦截API请求和响应
// 可以获取实际的API调用数据
```

**注入自定义样式**
```javascript
// 修改页面样式
let style = document.createElement('style');
style.textContent = `
    .message { font-size: 16px; }
`;
document.head.appendChild(style);
```

## 实现示例

### 示例 1：获取对话历史列表

```python
async def get_conversation_list(self):
    """获取对话历史列表"""
    js = """
    (function() {
        let conversations = [];
        let convElements = document.querySelectorAll('[class*="conversation"]');

        convElements.forEach(conv => {
            conversations.push({
                title: conv.querySelector('[class*="title"]')?.textContent,
                time: conv.querySelector('[class*="time"]')?.textContent,
                id: conv.getAttribute('data-id')
            });
        });

        return conversations;
    })()
    """

    result = await self.execute_js(js)
    return result.get("result", {}).get("result", {}).get("value", [])
```

### 示例 2：复制最后一条响应

```python
async def copy_last_response(self):
    """复制最后一条AI响应到剪贴板"""
    js = """
    (function() {
        let messages = document.querySelectorAll('[class*="message"]');
        if (messages.length === 0) return { error: "没有消息" };

        let lastMessage = messages[messages.length - 1];
        let text = lastMessage.textContent.trim();

        navigator.clipboard.writeText(text);

        return { success: true, length: text.length };
    })()
    """

    result = await self.execute_js(js)
    return result.get("result", {}).get("result", {}).get("value", {})
```

### 示例 3：搜索对话内容

```python
async def search_in_conversation(self, keyword: str):
    """在当前对话中搜索关键词"""
    js = f"""
    (function() {{
        let keyword = {json.dumps(keyword)};
        let messages = document.querySelectorAll('[class*="message"]');
        let results = [];

        messages.forEach((msg, index) => {{
            let text = msg.textContent.trim();
            if (text.includes(keyword)) {{
                results.push({{
                    index: index,
                    preview: text.substring(0, 100),
                    length: text.length
                }});
            }}
        }});

        return results;
    }})()
    """

    result = await self.execute_js(js)
    return result.get("result", {}).get("result", {}).get("value", [])
```

### 示例 4：导出对话为文本

```python
async def export_conversation(self, filename: str = "conversation.txt"):
    """导出当前对话为文本文件"""
    js = """
    (function() {
        let messages = document.querySelectorAll('[class*="message"]');
        let conversation = [];

        messages.forEach(msg => {
            let role = msg.getAttribute('data-role') || 'unknown';
            let text = msg.textContent.trim();
            conversation.push(`[${role}]: ${text}`);
        });

        let content = conversation.join('\\n\\n');

        // 创建下载链接
        let blob = new Blob([content], { type: 'text/plain' });
        let url = URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = 'conversation.txt';
        a.click();

        return { success: true, messageCount: messages.length };
    })()
    """

    result = await self.execute_js(js)
    return result.get("result", {}).get("result", {}).get("value", {})
```

## 限制和注意事项

### ⚠️ 技术限制

1. **DOM 结构依赖**
   - 功能实现依赖于应用的DOM结构
   - 应用更新可能导致选择器失效
   - 需要定期维护和更新

2. **异步操作**
   - 某些操作需要等待页面响应
   - 可能需要轮询或监听事件

3. **权限限制**
   - 某些操作可能需要用户确认
   - 文件上传需要特殊处理

4. **应用特定**
   - 不同应用的UI结构不同
   - 需要为每个应用单独适配

### ✅ 最佳实践

1. **先检查元素是否存在**
   ```javascript
   let element = document.querySelector('...');
   if (!element) return { error: "元素不存在" };
   ```

2. **使用容错机制**
   ```javascript
   try {
       // 操作代码
   } catch(e) {
       return { error: e.message };
   }
   ```

3. **提供详细反馈**
   ```javascript
   return {
       success: true,
       details: "操作完成",
       data: result
   };
   ```

## 扩展建议

### 优先级高的功能

1. **对话管理**
   - ✅ 列出所有对话
   - ✅ 切换对话
   - ✅ 删除对话
   - ✅ 重命名对话

2. **内容操作**
   - ✅ 复制响应
   - ✅ 导出对话
   - ✅ 搜索内容

3. **批量操作**
   - ✅ 批量删除对话
   - ✅ 批量导出对话

### 实现路线图

**Phase 1: 基础功能（已完成）**
- ✅ 发送消息
- ✅ 连续对话
- ✅ 清理对话

**Phase 2: 对话管理**
- 📋 列出对话历史
- 📋 切换对话
- 📋 删除对话
- 📋 重命名对话

**Phase 3: 内容操作**
- 📋 复制响应
- 📋 导出对话
- 📋 搜索内容

**Phase 4: 高级功能**
- 📋 文件上传
- 📋 截图
- 📋 自定义样式

## 如何添加新功能

### 步骤 1：探索 DOM 结构

```bash
# 使用 inspect_dom.py 查看页面结构
cd ~/.local/bin/doubao-cli
python3 inspect_dom.py
```

### 步骤 2：编写 JavaScript 代码

```javascript
// 在浏览器控制台测试
let element = document.querySelector('...');
element.click();
```

### 步骤 3：集成到 Python 代码

```python
async def new_feature(self):
    js = """
    (function() {
        // 你的JavaScript代码
        return { success: true };
    })()
    """

    result = await self.execute_js(js)
    return result
```

### 步骤 4：添加到命令行工具

```python
parser.add_argument('--new-feature', action='store_true',
                    help='使用新功能')

if args.new_feature:
    result = await cdp.new_feature()
    print(result)
```

## 总结

CDP 提供了强大的能力来操作浏览器应用，理论上可以实现：

- ✅ 所有用户可以手动完成的操作
- ✅ 自动化重复性任务
- ✅ 批量处理
- ✅ 数据提取和分析
- ✅ 自定义工作流

关键是找到正确的 DOM 选择器和触发方式。如果你有特定的功能需求，我可以帮你实现！
