#!/usr/bin/env bash

# banner_generator.sh - ASCII banner generator for Bash scripts
# Simplified version with predefined templates

# Colors
readonly COLOR_RESET='\033[0m'
readonly COLOR_RED='\033[31m'
readonly COLOR_GREEN='\033[32m'
readonly COLOR_YELLOW='\033[33m'
readonly COLOR_BLUE='\033[34m'
readonly COLOR_MAGENTA='\033[35m'
readonly COLOR_CYAN='\033[36m'

# Generate simple banner with block style
generate_banner() {
    local text="$1"
    local style="${2:-block}"
    
    echo "$text" | figlet 2>/dev/null || generate_banner_fallback "$text"
}

# Fallback banner generator (ASCII art style)
generate_banner_fallback() {
    local text="$1"
    local len=${#text}
    local border=$(printf '=%.0s' $(seq 1 $((len + 4))))
    
    echo "$border"
    echo "  $text"
    echo "$border"
}

# Generate colored banner
generate_colored_banner() {
    local text="$1"
    local color="$2"
    
    case "$color" in
        red) echo -e "${COLOR_RED}" ;;
        green) echo -e "${COLOR_GREEN}" ;;
        yellow) echo -e "${COLOR_YELLOW}" ;;
        blue) echo -e "${COLOR_BLUE}" ;;
        magenta) echo -e "${COLOR_MAGENTA}" ;;
        cyan) echo -e "${COLOR_CYAN}" ;;
    esac
    
    generate_banner_fallback "$text"
    echo -e "${COLOR_RESET}"
}

# Generate ASCII shapes
generate_arrow() {
    local direction="$1"
    local style="${2:-block}"
    
    case "$direction" in
        right|r)
            case "$style" in
                minimal) echo "→" ;;
                block|*) echo "▶" ;;
            esac
            ;;
        left|l)
            case "$style" in
                minimal) echo "←" ;;
                block|*) echo "◀" ;;
            esac
            ;;
        up|u)
            case "$style" in
                minimal) echo "↑" ;;
                block|*) echo "▲" ;;
            esac
            ;;
        down|d)
            case "$style" in
                minimal) echo "↓" ;;
                block|*) echo "▼" ;;
            esac
            ;;
    esac
}

# Generate checkmark
generate_check() {
    local style="${1:-block}"
    
    case "$style" in
        minimal) echo "✓" ;;
        detailed) echo "✅" ;;
        block|*) echo "✔" ;;
    esac
}

# Generate cross
generate_cross() {
    local style="${1:-block}"
    
    case "$style" in
        minimal) echo "✗" ;;
        detailed) echo "❌" ;;
        block|*) echo "✘" ;;
    esac
}

# Generate star
generate_star() {
    local style="${1:-block}"
    
    case "$style" in
        minimal) echo "☆" ;;
        block|*) echo "★" ;;
    esac
}

# Generate simple box banner
generate_box_banner() {
    local text="$1"
    local color="${2:-}"
    local len=${#text}
    local top="╔$(printf '═%.0s' $(seq 1 $((len + 2))))╗"
    local bottom="╚$(printf '═%.0s' $(seq 1 $((len + 2))))╝"
    
    if [[ -n "$color" ]]; then
        case "$color" in
            red) echo -e "${COLOR_RED}" ;;
            green) echo -e "${COLOR_GREEN}" ;;
            yellow) echo -e "${COLOR_YELLOW}" ;;
            blue) echo -e "${COLOR_BLUE}" ;;
            magenta) echo -e "${COLOR_MAGENTA}" ;;
            cyan) echo -e "${COLOR_CYAN}" ;;
        esac
    fi
    
    echo "$top"
    echo "║ $text ║"
    echo "$bottom"
    
    if [[ -n "$color" ]]; then
        echo -e "${COLOR_RESET}"
    fi
}

# Generate horizontal separator
generate_separator() {
    local width="${1:-60}"
    local char="${2:-═}"
    
    printf "$char%.0s" $(seq 1 $width)
    echo ""
}

# Demo function
demo_banner_generator() {
    echo ""
    generate_colored_banner "CLI BANNERS" "cyan"
    echo ""
    
    echo "Arrows:"
    echo "  Right: $(generate_arrow right)"
    echo "  Left: $(generate_arrow left)"
    echo "  Up: $(generate_arrow up)"
    echo "  Down: $(generate_arrow down)"
    echo ""
    
    echo "Status symbols:"
    echo "  $(generate_check detailed) Check"
    echo "  $(generate_cross detailed) Cross"
    echo "  $(generate_star) Star"
    echo ""
    
    echo "Box banner:"
    generate_box_banner "HELLO WORLD" "green"
    echo ""
    
    echo "Separator:"
    generate_separator 50 "─"
}

# Run demo if executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    demo_banner_generator
fi
