#!/bin/bash
# Check CCB environment status for 8 AI agents

echo "🔍 Checking CCB environment status (8 AI agents)..."
echo ""

ONLINE_COUNT=0
TOTAL_COUNT=7  # Excluding Claude (always online)

# Check Codex
echo -n "Codex: "
if cping 2>/dev/null | grep -qi "ok\|pong\|healthy"; then
    echo "✅ Online"
    CODEX_STATUS="online"
    ((ONLINE_COUNT++))
else
    echo "❌ Offline"
    CODEX_STATUS="offline"
fi

# Check Gemini
echo -n "Gemini: "
if gping 2>/dev/null | grep -qi "ok\|pong\|healthy"; then
    echo "✅ Online"
    GEMINI_STATUS="online"
    ((ONLINE_COUNT++))
else
    echo "❌ Offline"
    GEMINI_STATUS="offline"
fi

# Check OpenCode
echo -n "OpenCode: "
if oping 2>/dev/null | grep -qi "ok\|pong\|healthy"; then
    echo "✅ Online"
    OPENCODE_STATUS="online"
    ((ONLINE_COUNT++))
else
    echo "❌ Offline"
    OPENCODE_STATUS="offline"
fi

# Check iFlow
echo -n "iFlow: "
if iping 2>/dev/null | grep -qi "ok\|pong\|healthy"; then
    echo "✅ Online"
    IFLOW_STATUS="online"
    ((ONLINE_COUNT++))
else
    echo "❌ Offline"
    IFLOW_STATUS="offline"
fi

# Check Kimi
echo -n "Kimi: "
if kping 2>/dev/null | grep -qi "ok\|pong\|healthy"; then
    echo "✅ Online"
    KIMI_STATUS="online"
    ((ONLINE_COUNT++))
else
    echo "❌ Offline"
    KIMI_STATUS="offline"
fi

# Check Qwen
echo -n "Qwen: "
if qping 2>/dev/null | grep -qi "ok\|pong\|healthy"; then
    echo "✅ Online"
    QWEN_STATUS="online"
    ((ONLINE_COUNT++))
else
    echo "❌ Offline"
    QWEN_STATUS="offline"
fi

# Check DeepSeek
echo -n "DeepSeek: "
if dskping 2>/dev/null | grep -qi "ok\|pong\|healthy"; then
    echo "✅ Online"
    DEEPSEEK_STATUS="online"
    ((ONLINE_COUNT++))
else
    echo "❌ Offline"
    DEEPSEEK_STATUS="offline"
fi

echo ""
echo "Claude: ✅ Online (always available)"
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Online: $ONLINE_COUNT / $TOTAL_COUNT external AIs + Claude"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ "$ONLINE_COUNT" -eq "$TOTAL_COUNT" ]; then
    echo "✅ All 8 AI agents ready for distributed research!"
    exit 0
elif [ "$ONLINE_COUNT" -ge 4 ]; then
    echo "⚠️  Some AIs offline. Can continue with $((ONLINE_COUNT + 1)) agents."
    echo "   Claude will substitute for offline agents."
    exit 0
else
    echo "❌ Too few AIs online. Consider starting more agents."
    echo "   Minimum recommended: 4 AIs for meaningful distributed research."
    exit 1
fi
