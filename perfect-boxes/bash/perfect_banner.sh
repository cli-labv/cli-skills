#!/usr/bin/env bash

# perfect_banner.sh - Funciones para dibujar cuadros perfectos en terminal
# Soluciona el problema de desalineación con emojis (caracteres de ancho doble)

# Colores ANSI
readonly COLOR_RESET='\033[0m'
readonly COLOR_CYAN='\033[0;36m'
readonly COLOR_GREEN='\033[0;32m'
readonly COLOR_YELLOW='\033[1;33m'
readonly COLOR_RED='\033[0;31m'
readonly COLOR_BOLD='\033[1m'

# Función auxiliar: Calcula el ancho visual real de una cadena
# Los emojis ocupan 2 celdas, los caracteres ASCII ocupan 1
get_visual_width() {
    local text="$1"
    local width=0
    
    # Remover códigos de color ANSI para cálculo correcto
    local clean_text=$(echo -e "$text" | sed 's/\x1b\[[0-9;]*m//g')
    
    # Contar caracteres considerando emojis como ancho doble
    # Esta es una aproximación: detecta rangos comunes de emojis
    for (( i=0; i<${#clean_text}; i++ )); do
        char="${clean_text:$i:1}"
        
        # Obtener el código del carácter
        if [[ "$char" =~ [[:print:]] ]]; then
            # Para caracteres imprimibles ASCII
            if [[ "$char" =~ [[:ascii:]] ]]; then
                width=$((width + 1))
            else
                # Para caracteres no-ASCII, asumimos que emojis = 2 celdas
                # Este es un heurístico: caracteres Unicode > U+1F000 suelen ser emojis
                # En bash puro, no podemos hacer mejor sin herramientas externas
                local byte_length=${#char}
                if [[ $byte_length -ge 4 ]]; then
                    # Probablemente un emoji (4 bytes en UTF-8)
                    width=$((width + 2))
                else
                    width=$((width + 1))
                fi
            fi
        fi
    done
    
    echo "$width"
}

# Función mejorada: Repite un carácter N veces
repeat_char() {
    local char="$1"
    local count="$2"
    printf '%*s' "$count" '' | tr ' ' "$char"
}

# Función principal: Imprime un cuadro perfecto con título y contenido
print_perfect_box() {
    local title="$1"
    local subtitle="${2:-}"
    local description="${3:-}"
    local width="${4:-60}"
    local color="${5:-$COLOR_CYAN}"
    
    # Caracteres del cuadro
    local top_left="╔"
    local top_right="╗"
    local bottom_left="╚"
    local bottom_right="╝"
    local horizontal="═"
    local vertical="║"
    
    # Ancho interno (sin bordes)
    local inner_width=$((width - 2))
    
    # Línea superior
    echo -e "${color}${top_left}$(repeat_char "$horizontal" $inner_width)${top_right}${COLOR_RESET}"
    
    # Línea vacía
    echo -e "${color}${vertical}$(repeat_char ' ' $inner_width)${vertical}${COLOR_RESET}"
    
    # Título (centrado con compensación de emojis)
    if [[ -n "$title" ]]; then
        local title_visual_width=$(get_visual_width "$title")
        local title_padding=$(( (inner_width - title_visual_width) / 2 ))
        local title_padding_right=$(( inner_width - title_visual_width - title_padding ))
        
        echo -e "${color}${vertical}$(repeat_char ' ' $title_padding)${COLOR_BOLD}${title}${COLOR_RESET}${color}$(repeat_char ' ' $title_padding_right)${vertical}${COLOR_RESET}"
    fi
    
    # Subtítulo (centrado)
    if [[ -n "$subtitle" ]]; then
        echo -e "${color}${vertical}$(repeat_char ' ' $inner_width)${vertical}${COLOR_RESET}"
        
        local subtitle_visual_width=$(get_visual_width "$subtitle")
        local subtitle_padding=$(( (inner_width - subtitle_visual_width) / 2 ))
        local subtitle_padding_right=$(( inner_width - subtitle_visual_width - subtitle_padding ))
        
        echo -e "${color}${vertical}$(repeat_char ' ' $subtitle_padding)${subtitle}$(repeat_char ' ' $subtitle_padding_right)${vertical}${COLOR_RESET}"
    fi
    
    # Descripción (centrada)
    if [[ -n "$description" ]]; then
        echo -e "${color}${vertical}$(repeat_char ' ' $inner_width)${vertical}${COLOR_RESET}"
        
        local desc_visual_width=$(get_visual_width "$description")
        local desc_padding=$(( (inner_width - desc_visual_width) / 2 ))
        local desc_padding_right=$(( inner_width - desc_visual_width - desc_padding ))
        
        echo -e "${color}${vertical}$(repeat_char ' ' $desc_padding)${description}$(repeat_char ' ' $desc_padding_right)${vertical}${COLOR_RESET}"
    fi
    
    # Línea vacía
    echo -e "${color}${vertical}$(repeat_char ' ' $inner_width)${vertical}${COLOR_RESET}"
    
    # Línea inferior
    echo -e "${color}${bottom_left}$(repeat_char "$horizontal" $inner_width)${bottom_right}${COLOR_RESET}"
}

# Banner decorativo (solo bordes superior e inferior)
print_fancy_banner() {
    local title="$1"
    local subtitle="${2:-}"
    local width="${3:-60}"
    local color="${4:-$COLOR_CYAN}"
    
    local horizontal="═"
    local inner_width=$((width - 2))
    
    # Línea superior
    echo -e "${color}$(repeat_char "$horizontal" $width)${COLOR_RESET}"
    
    # Título
    if [[ -n "$title" ]]; then
        local title_visual_width=$(get_visual_width "$title")
        local title_padding=$(( (width - title_visual_width) / 2 ))
        local title_padding_right=$(( width - title_visual_width - title_padding ))
        
        echo -e "$(repeat_char ' ' $title_padding)${COLOR_BOLD}${title}${COLOR_RESET}$(repeat_char ' ' $title_padding_right)"
    fi
    
    # Subtítulo
    if [[ -n "$subtitle" ]]; then
        local subtitle_visual_width=$(get_visual_width "$subtitle")
        local subtitle_padding=$(( (width - subtitle_visual_width) / 2 ))
        local subtitle_padding_right=$(( width - subtitle_visual_width - subtitle_padding ))
        
        echo -e "$(repeat_char ' ' $subtitle_padding)${color}${subtitle}${COLOR_RESET}$(repeat_char ' ' $subtitle_padding_right)"
    fi
    
    # Línea inferior
    echo -e "${color}$(repeat_char "$horizontal" $width)${COLOR_RESET}"
}

# Header simple para secciones
print_header() {
    local text="$1"
    local icon="${2:-🚀}"
    local color="${3:-$COLOR_CYAN}"
    
    echo ""
    echo -e "${color}${icon}  ${COLOR_BOLD}${text}${COLOR_RESET}"
    echo -e "${color}$(repeat_char '─' 50)${COLOR_RESET}"
}

# Función de demostración (para testing)
demo_perfect_boxes() {
    echo ""
    print_perfect_box "📸 DIRTOPDF CLI 📄" "Convierte Carpetas de Imágenes en PDFs" "Versión 1.0.0" 62
    echo ""
    
    print_fancy_banner "🚀 PROYECTO INICIADO" "Ejecutando tareas..." 60
    echo ""
    
    print_header "📋 Paso 1: Preparación" "⚙️"
    echo ""
    
    print_header "✅ Paso 2: Completado" "✨"
    echo ""
}

# Si se ejecuta directamente, muestra la demo
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    demo_perfect_boxes
fi
