---
name: proxy-manager
description: 管理本地代理架构（Proxifier + Clash Verge + Charles），诊断网络问题，按需抓包，确保 VPN 和抓包隔离共存
triggers:
  - proxy
  - 代理
  - vpn
  - 翻墙
  - 抓包
  - charles
  - clash
  - proxifier
  - 网络连不上
  - 无法上网
  - 连不上外网
---

# Proxy Manager Skill

本地代理三层架构管理工具，确保 VPN（Clash Verge）和抓包（Charles）隔离共存、互不干扰。

## 架构概览

```
所有应用 → Proxifier (系统级拦截) → Clash Verge (7897) → 外网
                                        ↑ 翻墙/VPN

Charles (8888) → 直连（独立，不影响网络）

排除直连：Charles / Clash / Proxifier 自身 / localhost
```

### 组件职责

| 组件 | 端口 | 职责 | 开关影响 |
|------|------|------|----------|
| **Proxifier** | 系统级 | 流量调度中心，决定每个应用走哪个代理 | 关闭后所有应用直连 |
| **Clash Verge** | 7897 | VPN/翻墙，处理 GFW 相关流量 | 关闭后无法访问被墙网站 |
| **Charles** | 8888 | HTTP 抓包调试 | 开关不影响网络 |

### 关键设计原则

1. **Charles 不设系统代理** — Proxy → macOS Proxy 必须取消勾选
2. **Proxifier 负责分流** — 默认走 Clash，抓包时按应用切到 Charles
3. **三者互相直连** — 避免循环依赖

## 配置文件位置

| 配置 | 路径 |
|------|------|
| Proxifier Profile | `~/Library/Containers/com.initex.proxifier.v3.macos/Data/Profiles/default.ppx` |
| Clash Verge Config | `~/Library/Application Support/io.github.clash-verge-rev.clash-verge-rev/clash-verge.yaml` |
| Charles Config | `~/Library/Preferences/com.xk72.charles.config` |
| Clash API Socket | `/tmp/verge/verge-mihomo.sock` |

## 诊断流程

当用户报告网络问题时，按以下顺序排查：

### Step 1: 快速连通性测试

```bash
# 直连测试（绕过所有代理）
curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 --noproxy '*' https://www.baidu.com

# 通过 Clash 测试（翻墙）
curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 -x http://127.0.0.1:7897 https://www.google.com

# 通过 Charles 测试（抓包）
curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 -x http://127.0.0.1:8888 https://www.baidu.com
```

### Step 2: 检查端口监听

```bash
# Clash 7897
lsof -i :7897 -sTCP:LISTEN 2>&1

# Charles 8888
lsof -i :8888 -sTCP:LISTEN 2>&1

# 注意：Proxifier 运行时 lsof 可能看不到 LISTEN，用 curl 测试更准确
```

### Step 3: 检查系统代理（应该全部关闭）

```bash
scutil --proxy
# 期望：HTTPEnable=0, HTTPSEnable=0, ProxyAutoConfigEnable=0
```

### Step 4: 检查进程状态

```bash
ps aux | grep -i "[C]harles"
ps aux | grep -i "[v]erge-mihomo"
ps aux | grep -i "[Pp]roxifier"
```

### Step 5: 检查 Shell 环境变量

```bash
echo "HTTP_PROXY=$HTTP_PROXY"
echo "HTTPS_PROXY=$HTTPS_PROXY"
```

## 常见问题及修复

### 问题 1: 所有网站都打不开

**可能原因**: Proxifier 指向了未运行的代理

**修复**:
```bash
# 1. 检查 Clash 是否运行
curl -s -x http://127.0.0.1:7897 --connect-timeout 3 https://www.baidu.com -o /dev/null -w "%{http_code}"

# 2. 如果 Clash 挂了，重启
killall clash-verge 2>/dev/null; sleep 2; open -a "Clash Verge"

# 3. 如果 Clash 正常但还是不通，检查 Proxifier 配置
cat ~/Library/Containers/com.initex.proxifier.v3.macos/Data/Profiles/default.ppx
```

### 问题 2: 国内网站正常，Google 等被墙网站打不开

**可能原因**: Clash 代理未正常工作

**修复**:
```bash
# 重载 Clash 配置
curl -s --unix-socket /tmp/verge/verge-mihomo.sock -X PUT \
  -H "Content-Type: application/json" \
  -d '{"path":"/Users/leo/Library/Application Support/io.github.clash-verge-rev.clash-verge-rev/clash-verge.yaml"}' \
  http://localhost/configs

# 如果不行，完全重启 Clash Verge
killall clash-verge 2>/dev/null; sleep 2; open -a "Clash Verge"
```

### 问题 3: Charles 开启后网络断了

**可能原因**: Charles 开启了 macOS Proxy，劫持了系统代理

**修复**:
```bash
# 关闭系统代理
networksetup -setwebproxystate Wi-Fi off
networksetup -setsecurewebproxystate Wi-Fi off

# 确认 Charles 的 macOS Proxy 已取消勾选
# Charles → Proxy → 取消 "macOS Proxy"
```

### 问题 4: 代理循环（所有流量卡死）

**可能原因**: Proxifier 把 Charles/Clash 的流量也转发了，形成循环

**修复**: 恢复 Proxifier 为全部直连，打破循环：
```bash
cat > ~/Library/Containers/com.initex.proxifier.v3.macos/Data/Profiles/default.ppx << 'PPXEOF'
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ProxifierProfile version="101" platform="MacOSX" product_id="2" product_minver="200">
    <Options>
        <Resolve>
            <AutoModeDetection enabled="true"/>
            <ViaProxy enabled="false"><TryLocalDnsFirst enabled="false"/></ViaProxy>
            <ExclusionList ExcludeSimpleHostnames="true" ExcludeLocalhost="true" ExcludeSelfHostname="true" ExcludeLocalDomain="true">localhost;%SimpleHostnames%;%ComputerName%;*.local;</ExclusionList>
        </Resolve>
        <Encryption mode="basic"/>
        <HttpProxiesSupport enabled="false"/>
        <HandleDirectConnections enabled="false"/>
        <ConnectionLoopDetection enabled="true"/>
        <ProcessServices enabled="true"/>
        <ProcessOtherUsers enabled="true"/>
        <BlockUDP443 enabled="false"/>
    </Options>
    <ProxyList/>
    <ChainList/>
    <RuleList>
        <Rule enabled="true"><Name>Default</Name><Action type="Direct"/></Rule>
    </RuleList>
</ProxifierProfile>
PPXEOF

# 重启 Proxifier 加载
osascript -e 'tell application "Proxifier" to quit'; sleep 2; open -a Proxifier
```

然后按正常流程重新配置。

## 操作手册

### 正常模式（日常上网 + VPN）

Proxifier 配置：所有流量 → Clash (7897)

```xml
<!-- default.ppx 核心部分 -->
<ProxyList>
    <Proxy id="101" type="HTTPS">
        <Address>127.0.0.1</Address>
        <Port>7897</Port>
        <Options>0</Options>
    </Proxy>
</ProxyList>
<RuleList>
    <Rule enabled="true">
        <Name>Proxy tools direct</Name>
        <Applications>Charles; verge-mihomo; clash-verge; Proxifier; com.initex.proxifier.v3.macos.ProxifierExtension; mitmdump</Applications>
        <Action type="Direct"/>
    </Rule>
    <Rule enabled="true">
        <Name>Localhost</Name>
        <Targets>localhost; 127.0.0.1; ::1; %ComputerName%</Targets>
        <Action type="Direct"/>
    </Rule>
    <Rule enabled="true">
        <Name>Default</Name>
        <Action type="Proxy">101</Action>
    </Rule>
</RuleList>
```

### 抓包模式（对特定应用抓包）

在正常模式基础上，给目标应用加一条规则走 Charles：

```xml
<!-- 在 ProxyList 中添加 Charles -->
<Proxy id="100" type="HTTPS">
    <Address>127.0.0.1</Address>
    <Port>8888</Port>
    <Options>0</Options>
</Proxy>

<!-- 在 RuleList 中，Default 之前添加 -->
<Rule enabled="true">
    <Name>Capture - Chrome</Name>
    <Applications>Google Chrome</Applications>
    <Action type="Proxy">100</Action>
</Rule>
```

注意：抓包模式下 Charles 必须设置外部代理指向 Clash，否则被墙网站抓不到：
- Charles → Proxy → External Proxy Settings
- HTTP Proxy: 127.0.0.1:7897
- HTTPS Proxy: 127.0.0.1:7897

### 快速切换命令

```bash
# 开启抓包（以 Chrome 为例）
proxy-capture-on() {
    local app="${1:-Google Chrome}"
    # 读取当前配置，在 Default 规则前插入抓包规则
    # 需要 Charles 运行中
    echo "请在 Proxifier → Rules 中为 '$app' 添加规则 → 走 Charles (8888)"
    open -a Charles
    open -a Proxifier
}

# 关闭抓包（恢复正常模式）
proxy-capture-off() {
    # 删除抓包规则，恢复全部走 Clash
    echo "请在 Proxifier → Rules 中删除抓包规则"
    open -a Proxifier
}
```

## 完整正常模式配置文件

用于一键恢复正常状态：

```bash
# 写入正常模式配置
proxy-reset() {
    cat > ~/Library/Containers/com.initex.proxifier.v3.macos/Data/Profiles/default.ppx << 'PPXEOF'
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ProxifierProfile version="101" platform="MacOSX" product_id="2" product_minver="200">
    <Options>
        <Resolve>
            <AutoModeDetection enabled="true"/>
            <ViaProxy enabled="false"><TryLocalDnsFirst enabled="false"/></ViaProxy>
            <ExclusionList ExcludeSimpleHostnames="true" ExcludeLocalhost="true" ExcludeSelfHostname="true" ExcludeLocalDomain="true">localhost;%SimpleHostnames%;%ComputerName%;*.local;
</ExclusionList>
        </Resolve>
        <Encryption mode="basic"/>
        <HttpProxiesSupport enabled="false"/>
        <HandleDirectConnections enabled="false"/>
        <ConnectionLoopDetection enabled="true"/>
        <ProcessServices enabled="true"/>
        <ProcessOtherUsers enabled="true"/>
        <BlockUDP443 enabled="false"/>
    </Options>
    <ProxyList>
        <Proxy id="100" type="HTTPS">
            <Address>127.0.0.1</Address>
            <Port>8888</Port>
            <Options>0</Options>
        </Proxy>
        <Proxy id="101" type="HTTPS">
            <Address>127.0.0.1</Address>
            <Port>7897</Port>
            <Options>0</Options>
        </Proxy>
    </ProxyList>
    <ChainList/>
    <RuleList>
        <Rule enabled="true">
            <Name>Proxy tools direct</Name>
            <Applications>Charles; verge-mihomo; clash-verge; Proxifier; com.initex.proxifier.v3.macos.ProxifierExtension; mitmdump</Applications>
            <Action type="Direct"/>
        </Rule>
        <Rule enabled="true">
            <Name>Localhost</Name>
            <Targets>localhost; 127.0.0.1; ::1; %ComputerName%</Targets>
            <Action type="Direct"/>
        </Rule>
        <Rule enabled="true">
            <Name>Default</Name>
            <Action type="Proxy">101</Action>
        </Rule>
    </RuleList>
</ProxifierProfile>
PPXEOF

    # 关闭系统代理
    networksetup -setwebproxystate Wi-Fi off
    networksetup -setsecurewebproxystate Wi-Fi off

    # 重启 Proxifier
    osascript -e 'tell application "Proxifier" to quit' 2>/dev/null
    sleep 2
    open -a Proxifier

    echo "✓ 代理已恢复正常模式（所有流量 → Clash 7897）"
}
```

## 启动顺序（重要）

正确的启动顺序避免端口绑定问题：

1. **Clash Verge** — 先启动，绑定 7897
2. **Proxifier** — 再启动，拦截系统流量转发给 Clash
3. **Charles** — 按需启动，独立运行

```bash
proxy-start-all() {
    echo "1. 启动 Clash Verge..."
    open -a "Clash Verge"
    sleep 5

    echo "2. 验证 Clash..."
    if curl -s -x http://127.0.0.1:7897 --connect-timeout 3 https://www.baidu.com -o /dev/null -w "%{http_code}" | grep -q 200; then
        echo "   ✓ Clash 7897 正常"
    else
        echo "   ✗ Clash 7897 异常，请检查"
        return 1
    fi

    echo "3. 启动 Proxifier..."
    open -a Proxifier
    sleep 3
    echo "   ✓ Proxifier 已启动"

    echo "✓ 代理架构就绪"
}
```

## Claude.ai / Anthropic 访问

### 问题：VPN 节点被 Cloudflare 封禁

Anthropic 使用 Cloudflare 防护，会封锁已知数据中心 IP。大多数 VPN 节点（包括 GPT 专用节点）都会返回 403。

### 自动寻找可用节点

通过 Clash API 遍历节点测试 claude.ai 可达性：

```bash
# 切换节点（通过 Clash Unix Socket API）
curl -s --unix-socket /tmp/verge/verge-mihomo.sock \
  -X PUT -H "Content-Type: application/json" \
  -d '{"name":"节点名"}' http://localhost/proxies/GLOBAL

# 测试 claude.ai
curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 \
  -x http://127.0.0.1:7897 https://claude.ai
# 200/301/302 = 可用, 403 = 被封
```

### 已知可用节点（2026-03-12 测试）

- **V1-479|香港|x0.1** — IP: 38.76.140.195 ✅

### TUN 模式（重要）

**浏览器访问 claude.ai 必须开启 Clash Verge 的 TUN 模式**，否则浏览器流量不走 Clash：
- Clash Verge → Settings → TUN Mode → 开启
- TUN 模式在系统层面拦截所有流量，比 HTTP 代理更彻底
- 开启 TUN 后，Proxifier 可以不用（TUN 已经全局接管）

### TUN vs Proxifier 的选择

| 方案 | 优点 | 缺点 |
|------|------|------|
| **TUN 模式** | 全局接管，浏览器直接生效 | 与 Proxifier 可能冲突 |
| **Proxifier** | 可按应用精细分流 | 浏览器可能绕过 |
| **TUN + 关闭 Proxifier** | 最简单稳定 | 无法按应用分流 |

**推荐**：日常用 TUN 模式，需要按应用分流抓包时再开 Proxifier。

## Clash API 常用操作

```bash
SOCKET="/tmp/verge/verge-mihomo.sock"

# 查看当前配置
curl -s --unix-socket $SOCKET http://localhost/configs | python3 -m json.tool

# 切换模式 (rule/global/direct)
curl -s --unix-socket $SOCKET -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"mode":"rule"}' http://localhost/configs

# 列出所有代理组
curl -s --unix-socket $SOCKET http://localhost/proxies

# 切换节点
curl -s --unix-socket $SOCKET -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name":"V1-479|香港|x0.1"}' http://localhost/proxies/GLOBAL

# 重载配置
curl -s --unix-socket $SOCKET -X PUT \
  -H "Content-Type: application/json" \
  -d '{"path":"/Users/leo/Library/Application Support/io.github.clash-verge-rev.clash-verge-rev/clash-verge.yaml"}' \
  http://localhost/configs
```

## 注意事项

- **永远不要**让 Charles 设置系统代理（macOS Proxy）
- **永远不要**在 Proxifier 中用代理链把 Charles 和 Clash 串联（会循环）
- Proxifier 系统扩展是 root 权限运行的，无法通过 kill 停止，只能通过 App 自身退出
- Clash Verge 的 mihomo 核心也是 root 权限，重启需要通过 App 或 API
- Shell 环境变量 `HTTP_PROXY`/`HTTPS_PROXY` 只影响终端应用，GUI 应用走 Proxifier 或 TUN
- **TUN 模式和 Proxifier 同时开启可能冲突**，建议二选一
- 访问 claude.ai 时优先选择低倍率(x0.1)香港节点，被封概率较低
