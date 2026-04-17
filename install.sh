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
CANONICAL_ONLY=0
TARGET_CATEGORY=""

# --- Counters ---
INSTALLED=0
SKIPPED=0
ALREADY_LINKED=0
REMOVED_STALE=0
SKIPPED_COMPAT=0

show_help() {
    echo -e "${BOLD}Claude Code Skills Installer${RESET}"
    echo ""
    echo "Usage:"
    echo "  ./install.sh              Install all skills"
    echo "  ./install.sh --canonical-only"
    echo "  ./install.sh <category>   Install one category"
    echo "  ./install.sh <category> --canonical-only"
    echo "  ./install.sh --list       List available categories and skill counts"
    echo "  ./install.sh --help       Show this help message"
    echo ""
    echo "Categories:"
    for cat in $CATEGORIES; do
        local count
        count=$(count_skill_dirs "$SCRIPT_DIR/$cat")
        printf "  %-25s %s skills\n" "$cat" "$count"
    done
    echo ""
    echo "Skills are symlinked into: $SKILLS_DIR"
    echo "Use --canonical-only to skip legacy compatibility wrappers."
}

show_list() {
    echo -e "${BOLD}Available Categories${RESET}"
    echo ""
    local total=0
    for cat in $CATEGORIES; do
        local count
        count=$(count_skill_dirs "$SCRIPT_DIR/$cat")
        total=$((total + count))
        printf "  ${CYAN}%-25s${RESET} %2s skills\n" "$cat" "$count"
    done
    echo ""
    echo -e "  ${BOLD}Total: ${total} skills${RESET}"
}

count_skill_dirs() {
    local cat_dir="$1"
    local count=0
    local skill_dir

    for skill_dir in "$cat_dir"/*/; do
        [ ! -d "$skill_dir" ] && continue
        [ -f "$skill_dir/SKILL.md" ] || continue
        count=$((count + 1))
    done

    echo "$count"
}

is_compat_skill() {
    local cat="$1"
    local name="$2"

    case "$cat:$name" in
        ai-collaboration:ask|ai-collaboration:cask|ai-collaboration:ccb-launcher|ai-collaboration:dask|ai-collaboration:dskask|ai-collaboration:gask|ai-collaboration:iask|ai-collaboration:kask|ai-collaboration:oask|ai-collaboration:pend|ai-collaboration:ping|ai-collaboration:qask)
            return 0
            ;;
        product-management:pm-analytics|product-management:pm-communication|product-management:pm-discovery|product-management:pm-execution|product-management:pm-growth|product-management:pm-leadership|product-management:pm-playbooks|product-management:pm-strategy|product-management:pm-team)
            return 0
            ;;
    esac

    return 1
}

install_category() {
    local cat="$1"
    local cat_dir="$SCRIPT_DIR/$cat"

    if [ ! -d "$cat_dir" ]; then
        echo -e "  ${RED}Category not found: $cat${RESET}"
        return 1
    fi

    local skill_count
    skill_count=$(count_skill_dirs "$cat_dir")
    echo -e "${BLUE}${BOLD}[$cat]${RESET} ${skill_count} skills"

    for skill_dir in "$cat_dir"/*/; do
        [ ! -d "$skill_dir" ] && continue
        [ -f "$skill_dir/SKILL.md" ] || continue
        local name
        name=$(basename "$skill_dir")
        local target="$SKILLS_DIR/$name"

        if [ "$CANONICAL_ONLY" -eq 1 ] && is_compat_skill "$cat" "$name"; then
            echo -e "  ${CYAN}>${RESET} $name (compatibility skill skipped)"
            SKIPPED_COMPAT=$((SKIPPED_COMPAT + 1))
            continue
        fi

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

prune_stale_links() {
    local target
    for target in "$SKILLS_DIR"/*; do
        [ ! -L "$target" ] && continue

        local source
        source=$(readlink "$target")

        case "$source" in
            "$SCRIPT_DIR"/*)
                if [ ! -e "$source" ]; then
                    rm "$target"
                    echo -e "  ${YELLOW}-${RESET} $(basename "$target") (removed stale link)"
                    REMOVED_STALE=$((REMOVED_STALE + 1))
                fi
                ;;
        esac
    done
}

# --- Main ---

while [ "$#" -gt 0 ]; do
    case "$1" in
        --help|-h)
            show_help
            exit 0
            ;;
        --list|-l)
            show_list
            exit 0
            ;;
        --canonical-only)
            CANONICAL_ONLY=1
            ;;
        *)
            if [ -n "$TARGET_CATEGORY" ]; then
                echo -e "${RED}Unexpected argument: $1${RESET}"
                echo ""
                show_help
                exit 1
            fi
            TARGET_CATEGORY="$1"
            ;;
    esac
    shift
done

mkdir -p "$SKILLS_DIR"

echo -e "${BOLD}Claude Code Skills Installer${RESET}"
echo -e "Target: ${CYAN}$SKILLS_DIR${RESET}"
if [ "$CANONICAL_ONLY" -eq 1 ]; then
    echo -e "Mode:   ${CYAN}canonical-only${RESET} (skip legacy compatibility wrappers)"
fi
echo ""

if [ -n "$TARGET_CATEGORY" ]; then
    install_category "$TARGET_CATEGORY"
else
    for cat in $CATEGORIES; do
        install_category "$cat"
    done
fi

prune_stale_links

echo ""
echo -e "${BOLD}Summary${RESET}"
echo -e "  ${GREEN}Installed:${RESET}      $INSTALLED"
echo -e "  ${YELLOW}Already linked:${RESET} $ALREADY_LINKED"
if [ "$SKIPPED_COMPAT" -gt 0 ]; then
    echo -e "  ${CYAN}Skipped compat:${RESET} $SKIPPED_COMPAT"
fi
if [ "$REMOVED_STALE" -gt 0 ]; then
    echo -e "  ${YELLOW}Removed stale:${RESET} $REMOVED_STALE"
fi
if [ "$SKIPPED" -gt 0 ]; then
    echo -e "  ${RED}Skipped:${RESET}        $SKIPPED (remove existing dirs to re-link)"
fi
echo -e "  ${CYAN}Total in target:${RESET} $(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 2>/dev/null | wc -l | tr -d ' ') skills"
echo ""
echo -e "${GREEN}Done!${RESET}"
