# CDP AI Tools 完整测试报告

测试时间: $(date)

## 测试 1: ai-chat 帮助信息
```
usage: ai-chat [-h] [--clear] [--timeout TIMEOUT] [--list-conversations]
               [--switch INDEX] [--delete INDEX] [--rename INDEX NAME]
               [--quick-action NAME] [--settings] [--model MODEL]
               [--list-models] [--show-model NAME] [--pull NAME]
               [--generate MODEL PROMPT] [--stream] [--base-url BASE_URL]
               {doubao,stepfun,ollama} [message ...]

CDP AI Tools - 本地 AI 应用交互工具

positional arguments:
  {doubao,stepfun,ollama}
                        AI 应用标识符
  message               要发送的消息

optional arguments:
  -h, --help            show this help message and exit
  --clear               对话结束后清理记录（默认保留对话）
  --timeout TIMEOUT     超时时间（秒），默认60秒
  --list-conversations  列出所有对话
  --switch INDEX        切换到指定对话
  --delete INDEX        删除指定对话
  --rename INDEX NAME   重命名对话
  --quick-action NAME   点击快捷操作按钮
  --settings            打开设置面板
  --model MODEL         Ollama 模型名称（默认: qwen2.5:7b）
  --list-models         [Ollama] 列出所有模型
  --show-model NAME     [Ollama] 显示模型详情
  --pull NAME           [Ollama] 拉取模型
  --generate MODEL PROMPT
                        [Ollama] 生成响应
```
### 测试结果: ✅ 通过

---

## 测试 2: 豆包 - 列出对话
```
{
  "success": true,
  "count": 0,
  "conversations": []
}
```
### 测试结果: ✅ 通过

---

## 测试 3: 阶跃AI - 列出对话
```
{
  "success": true,
  "count": 0,
  "conversations": []
}
```
### 测试结果: ✅ 通过

---

## 测试 4: Ollama - 列出模型
```
✓ 已连接到 Ollama: http://localhost:11434
{
  "success": true,
  "models": [
    {
      "name": "deepseek-v3.1:671b-cloud",
      "model": "deepseek-v3.1:671b-cloud",
      "remote_model": "deepseek-v3.1:671b",
      "remote_host": "https://ollama.com:443",
      "modified_at": "2026-02-07T09:27:22.346234577+08:00",
      "size": 405,
      "digest": "d3749919e45f955731da7a7e76849e20f7ed310725d3b8b52822e811f55d0a90",
      "details": {
        "parent_model": "",
        "format": "",
        "family": "deepseek2",
        "families": [
          "deepseek2"
        ],
        "parameter_size": "671.0B",
        "quantization_level": "FP8_E4M3"
      }
    },
    {
      "name": "qwen2.5:7b",
      "model": "qwen2.5:7b",
      "modified_at": "2026-02-06T18:26:26.994125748+08:00",
      "size": 4683087332,
      "digest": "845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "qwen2",
        "families": [
          "qwen2"
        ],
        "parameter_size": "7.6B",
        "quantization_level": "Q4_K_M"
      }
    }
  ]
}
```
### 测试结果: ✅ 通过

