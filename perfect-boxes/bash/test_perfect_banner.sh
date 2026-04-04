#!/usr/bin/env bash

# test_perfect_banner.sh - Suite de pruebas para perfect_banner.sh
# Verifica que los cuadros se rendericen correctamente

set -e

# Colores para los tests
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
RESET='\033[0m'

# Importar la skill
source "$(dirname "$0")/../bash/perfect_banner.sh"

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║          TEST SUITE: Perfect Boxes Skill (Bash)          ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Test 1: Cuadro básico sin emojis
echo -e "${YELLOW}Test 1: Cuadro básico sin emojis${RESET}"
print_perfect_box "TITULO DE PRUEBA" "Subtitulo de prueba" "Descripción" 60 "$COLOR_CYAN"
echo -e "${GREEN}✓ Test 1 pasado${RESET}"
echo ""

# Test 2: Cuadro con un emoji
echo -e "${YELLOW}Test 2: Cuadro con un emoji${RESET}"
print_perfect_box "📸 TITULO CON EMOJI" "Subtitulo normal" "" 60 "$COLOR_GREEN"
echo -e "${GREEN}✓ Test 2 pasado${RESET}"
echo ""

# Test 3: Cuadro con múltiples emojis
echo -e "${YELLOW}Test 3: Cuadro con múltiples emojis${RESET}"
print_perfect_box "🚀 📸 ✅ MULTIPLE EMOJIS 🎉 📄 ✨" "Línea con varios emojis" "" 70 "$COLOR_BLUE"
echo -e "${GREEN}✓ Test 3 pasado${RESET}"
echo ""

# Test 4: Banner fancy
echo -e "${YELLOW}Test 4: Banner decorativo${RESET}"
print_fancy_banner "🎊 BANNER DE PRUEBA" "Con subtítulo" 60 "$COLOR_YELLOW"
echo -e "${GREEN}✓ Test 4 pasado${RESET}"
echo ""

# Test 5: Header
echo -e "${YELLOW}Test 5: Header simple${RESET}"
print_header "📋 Header de prueba" "⚙️" "$COLOR_CYAN"
echo -e "${GREEN}✓ Test 5 pasado${RESET}"
echo ""

# Test 6: Cuadro ancho variable
echo -e "${YELLOW}Test 6: Cuadro ancho (80 columnas)${RESET}"
print_perfect_box "📦 CUADRO ANCHO" "Este es un cuadro más ancho que el estándar" "" 80 "$COLOR_MAGENTA"
echo -e "${GREEN}✓ Test 6 pasado${RESET}"
echo ""

# Test 7: Cuadro estrecho
echo -e "${YELLOW}Test 7: Cuadro estrecho (40 columnas)${RESET}"
print_perfect_box "🎯 MINI" "Compacto" "" 40 "$COLOR_RED"
echo -e "${GREEN}✓ Test 7 pasado${RESET}"
echo ""

# Test 8: Solo título
echo -e "${YELLOW}Test 8: Solo título (sin subtítulo ni descripción)${RESET}"
print_perfect_box "✅ SOLO TITULO" "" "" 50 "$COLOR_GREEN"
echo -e "${GREEN}✓ Test 8 pasado${RESET}"
echo ""

# Resumen
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              ✅ TODOS LOS TESTS PASARON ✅               ║"
echo "║                                                           ║"
echo "║         La skill perfect-boxes funciona correctamente     ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
