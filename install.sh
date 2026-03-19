#!/bin/bash
# Install Claude Code skills by symlinking to ~/.claude/skills/
# Usage: ./install.sh [category]  (no args = install all)

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"
CATEGORIES="productivity development documents research ai-collaboration product-management security design system"

mkdir -p "$SKILLS_DIR"

install_category() {
    local cat="$1"
    local cat_dir="$SCRIPT_DIR/$cat"
    [ ! -d "$cat_dir" ] && return

    echo "📦 Installing $cat..."
    for skill_dir in "$cat_dir"/*/; do
        [ ! -d "$skill_dir" ] && continue
        local name=$(basename "$skill_dir")
        local target="$SKILLS_DIR/$name"

        if [ -L "$target" ]; then
            echo "  ↺ $name (already linked)"
        elif [ -d "$target" ]; then
            echo "  ⚠ $name (exists, skipping — remove manually to re-link)"
        else
            ln -s "$skill_dir" "$target"
            echo "  ✓ $name"
        fi
    done
}

if [ -n "$1" ]; then
    install_category "$1"
else
    for cat in $CATEGORIES; do
        install_category "$cat"
    done
fi

echo ""
echo "Done! Skills installed to $SKILLS_DIR"
echo "Total skills: $(ls -d "$SKILLS_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ')"
