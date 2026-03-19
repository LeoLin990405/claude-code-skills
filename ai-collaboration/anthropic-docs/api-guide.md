# API 入门指南

## 前置条件
1. Anthropic Console 账户
2. API Key (从 platform.claude.com/settings/keys 获取)

## 快速开始

### 设置环境变量
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### cURL 调用示例
```bash
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user",
        "content": "Hello, Claude!"
      }
    ]
  }'
```

### Python SDK
```bash
pip install anthropic
```

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)
print(message.content)
```

### TypeScript SDK
```bash
npm install @anthropic-ai/sdk
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

async function main() {
  const anthropic = new Anthropic();

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    messages: [
      { role: "user", content: "Hello, Claude!" }
    ]
  });
  console.log(msg);
}

main().catch(console.error);
```

### Java SDK
```xml
<dependency>
  <groupId>com.anthropic</groupId>
  <artifactId>anthropic-java</artifactId>
  <version>1.0.0</version>
</dependency>
```

```java
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;

public class QuickStart {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-sonnet-4-5-20250929")
            .maxTokens(1000)
            .addUserMessage("Hello, Claude!")
            .build();

        Message message = client.messages().create(params);
        System.out.println(message.content());
    }
}
```

## API 响应格式

```json
{
  "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello! How can I help you today?"
    }
  ],
  "model": "claude-sonnet-4-5",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 10,
    "output_tokens": 15
  }
}
```

## 关键参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| model | string | 模型名称 |
| max_tokens | int | 最大输出 token 数 |
| messages | array | 对话消息列表 |
| system | string | 系统提示词 (可选) |
| temperature | float | 随机性 0-1 (可选) |
| stop_sequences | array | 停止序列 (可选) |

## Stop Reason 类型

| 值 | 说明 |
|----|------|
| end_turn | 正常结束 |
| max_tokens | 达到 token 限制 |
| stop_sequence | 遇到停止序列 |
| refusal | 安全拒绝 (Claude 4+) |
| model_context_window_exceeded | 上下文窗口超限 (4.5+) |

## 重要链接

- API 文档: https://platform.claude.com/docs
- API Console: https://platform.claude.com
- SDK 文档: https://platform.claude.com/docs/en/api/client-sdks
- Cookbook: https://platform.claude.com/cookbooks
