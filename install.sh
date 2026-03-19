#!/bin/bash
# Claude Code Skills Installer
# Symlinks skill directories into ~/.claude/skills/
#
# Usage:
#   ./install.sh              Install all skills
#   ./install.sh <category>   Install one category
#   ./install.sh --list       List available categories and skill counts
#   ./install.sh --help       Show this help message

set -e

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
RESET='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"
CATEGORIES="productivity development documents research ai-collaboration product-management security design system"

# --- Counters ---
INSTALLED=0
SKIPPED=0
ALREADY_LINKED=0

show_help() {
    echo -e "${BOLD}Claude Code Skills Installer${RESET}"
    echo ""
    echo "Usage:"
    echo "  ./install.sh              Install all skills"
    echo "  ./install.sh <category>   Install one category"
    echo "  ./install.sh --list       List available categories and skill counts"
    echo "  ./install.sh --help       Show this help message"
    echo ""
    echo "Categories:"
    for cat in $CATEGORIES; do
        local count
        count=$(find "$SCRIPT_DIR/$cat" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
        printf "  %-25s %s skills\n" "$cat" "$count"
    done
    echo ""
    echo "Skills are symlinked into: $SKILLS_DIR"
}

show_list() {
    echo -e "${BOLD}Available Categories${RESET}"
    echo ""
    local total=0
    for cat in $CATEGORIES; do
        local count
        count=$(find "$SCRIPT_DIR/$cat" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
        total=$((total + count))
        printf "  ${CYAN}%-25s${RESET} %2s skills\n" "$cat" "$count"
    done
    echo ""
    echo -e "  ${BOLD}Total: ${total} skills${RESET}"
}

install_category() {
    local cat="$1"
    local cat_dir="$SCRIPT_DIR/$cat"

    if [ ! -d "$cat_dir" ]; then
        echo -e "  ${RED}Category not found: $cat${RESET}"
        return 1
    fi

    local skill_count
    skill_count=$(find "$cat_dir" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l | tr -d ' ')
    echo -e "${BLUE}${BOLD}[$cat]${RESET} ${skill_count} skills"

    for skill_dir in "$cat_dir"/*/; do
        [ ! -d "$skill_dir" ] && continue
        local name
        name=$(basename "$skill_dir")
        local target="$SKILLS_DIR/$name"

        if [ -L "$target" ]; then
            echo -e "  ${YELLOW}~${RESET} $name (already linked)"
            ALREADY_LINKED=$((ALREADY_LINKED + 1))
        elif [ -d "$target" ]; then
            echo -e "  ${RED}!${RESET} $name (directory exists, skipping)"
            SKIPPED=$((SKIPPED + 1))
        else
            ln -s "$skill_dir" "$target"
            echo -e "  ${GREEN}+${RESET} $name"
            INSTALLED=$((INSTALLED + 1))
        fi
    done
}

# --- Main ---

case "${1:-}" in
    --help|-h)
        show_help
        exit 0
        ;;
    --list|-l)
        show_list
        exit 0
        ;;
esac

mkdir -p "$SKILLS_DIR"

echo -e "${BOLD}Claude Code Skills Installer${RESET}"
echo -e "Target: ${CYAN}$SKILLS_DIR${RESET}"
echo ""

if [ -n "${1:-}" ]; then
    install_category "$1"
else
    for cat in $CATEGORIES; do
        install_category "$cat"
    done
fi

echo ""
echo -e "${BOLD}Summary${RESET}"
echo -e "  ${GREEN}Installed:${RESET}      $INSTALLED"
echo -e "  ${YELLOW}Already linked:${RESET} $ALREADY_LINKED"
if [ "$SKIPPED" -gt 0 ]; then
    echo -e "  ${RED}Skipped:${RESET}        $SKIPPED (remove existing dirs to re-link)"
fi
echo -e "  ${CYAN}Total in target:${RESET} $(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 2>/dev/null | wc -l | tr -d ' ') skills"
echo ""
echo -e "${GREEN}Done!${RESET}"
