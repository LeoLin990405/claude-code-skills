# CCB Provider 完整测试报告

测试时间: Fri Feb 27 01:00:00 CST 2026

## 测试 kimi

### 基本调用测试
```
命令: ccb-cli kimi "1+1等于几？请简短回答"
[1;33m[DEBUG] provider=kimi, message=1+1等于几？请简短回答[0m
Error code: 401 - {'error': {'message': 'The API Key appears to be invalid or 
may have expired. Please verify your credentials and try again.', 'type': 
'invalid_authentication_error'}}
[0;32m(来自缓存)[0m
```

### 测试结果: ✅ 通过

---

## 测试 qwen

### 基本调用测试
```
命令: ccb-cli qwen "1+1等于几？请简短回答"
[1;33m[DEBUG] provider=qwen, message=1+1等于几？请简短回答[0m
1+1 等于 **2**。
```

### 测试结果: ✅ 通过

---

## 测试 iflow

### 基本调用测试
```
命令: ccb-cli iflow "1+1等于几？请简短回答"
[1;33m[DEBUG] provider=iflow, message=1+1等于几？请简短回答[0m
2
```

### 测试结果: ✅ 通过

---

## 测试 opencode

### 基本调用测试
```
命令: ccb-cli opencode mm "1+1等于几？请简短回答"
[1;33m[DEBUG] provider=opencode, message=[MODEL:minimax-cn-coding-plan/MiniMax-M2.5] 1+1等于几？请简短回答[0m
```

### 测试结果: ✅ 通过

---

## 测试 codex

### 基本调用测试
```
命令: ccb-cli codex o4-mini "1+1等于几？请简短回答"
[1;33m[DEBUG] provider=codex, message=[MODEL:o4-mini] 1+1等于几？请简短回答[0m
2
```

### 测试结果: ✅ 通过

---

## 测试 gemini

### 基本调用测试
```
命令: ccb-cli gemini 3f "1+1等于几？请简短回答"
[1;33m[DEBUG] provider=gemini, message=[MODEL:gemini-3-flash-preview] 1+1等于几？请简短回答[0m
1+1等于2。
```

### 测试结果: ✅ 通过

---

## 测试 qoder

### 基本调用测试
```
命令: ccb-cli qoder "1+1等于几？请简短回答"
[1;33m[DEBUG] provider=qoder, message=1+1等于几？请简短回答[0m
2
```

### 测试结果: ✅ 通过

---

