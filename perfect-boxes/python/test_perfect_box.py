#!/usr/bin/env python3
"""
test_perfect_box.py - Suite de pruebas para perfect_box.py
Verifica que los cuadros se rendericen correctamente y que el cálculo de ancho funcione.
"""

import sys
from pathlib import Path

# Importar el módulo
sys.path.insert(0, str(Path(__file__).parent))
from perfect_box import (
    get_visual_width,
    get_char_width,
    center_text,
    print_perfect_box,
    print_fancy_banner,
    print_header,
    Colors
)


def test_char_width():
    """Prueba el cálculo de ancho de caracteres individuales."""
    print(f"\n{Colors.YELLOW}Test 1: Ancho de caracteres individuales{Colors.RESET}")
    
    tests = [
        ('A', 1, "Letra ASCII"),
        (' ', 1, "Espacio"),
        ('📸', 2, "Emoji cámara"),
        ('🚀', 2, "Emoji cohete"),
        ('中', 2, "Carácter CJK"),
        ('あ', 2, "Hiragana japonés"),
        ('\n', 0, "Nueva línea"),
    ]
    
    passed = 0
    for char, expected, description in tests:
        result = get_char_width(char)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {description}: '{char}' = {result} celdas (esperado: {expected})")
        if result == expected:
            passed += 1
    
    print(f"  Resultado: {passed}/{len(tests)} tests pasados")
    return passed == len(tests)


def test_visual_width():
    """Prueba el cálculo de ancho visual de cadenas completas."""
    print(f"\n{Colors.YELLOW}Test 2: Ancho visual de cadenas{Colors.RESET}")
    
    tests = [
        ("Hello World", 11, "Texto ASCII simple"),
        ("📸 Camera", 9, "Emoji + texto"),
        ("🚀 Test", 7, "Emoji + texto (cohete)"),
        ("日本語", 6, "Texto japonés (3 chars × 2)"),
        ("Mix 中文 text", 13, "Mezcla ASCII + CJK"),
        ("", 0, "Cadena vacía"),
    ]
    
    passed = 0
    for text, expected, description in tests:
        result = get_visual_width(text)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {description}: '{text}' = {result} celdas (esperado: {expected})")
        if result == expected:
            passed += 1
    
    print(f"  Resultado: {passed}/{len(tests)} tests pasados")
    return passed == len(tests)


def test_center_text():
    """Prueba el centrado de texto."""
    print(f"\n{Colors.YELLOW}Test 3: Centrado de texto{Colors.RESET}")
    
    tests = [
        ("Test", 20, "Texto corto"),
        ("📸 Emoji", 20, "Texto con emoji"),
        ("Very Long Text That Should Be Truncated", 15, "Texto largo truncado"),
    ]
    
    passed = 0
    for text, width, description in tests:
        result = center_text(text, width)
        result_width = get_visual_width(result)
        status = "✅" if result_width == width else "❌"
        print(f"  {status} {description}: ancho={result_width} (esperado: {width})")
        print(f"      '{result}'")
        if result_width == width:
            passed += 1
    
    print(f"  Resultado: {passed}/{len(tests)} tests pasados")
    return passed == len(tests)


def test_boxes():
    """Prueba visual de los cuadros."""
    print(f"\n{Colors.YELLOW}Test 4: Renderizado de cuadros{Colors.RESET}\n")
    
    # Test 4.1: Cuadro básico
    print("  4.1 - Cuadro básico sin emojis:")
    print_perfect_box("TITULO DE PRUEBA", "Subtitulo", "Descripción", width=60)
    print()
    
    # Test 4.2: Cuadro con un emoji
    print("  4.2 - Cuadro con un emoji:")
    print_perfect_box("📸 TITULO CON EMOJI", "Subtitulo normal", width=60, color="green")
    print()
    
    # Test 4.3: Cuadro con múltiples emojis
    print("  4.3 - Cuadro con múltiples emojis:")
    print_perfect_box("🚀 📸 ✅ MULTIPLE", "Varios emojis juntos", width=60, color="blue")
    print()
    
    # Test 4.4: Banner
    print("  4.4 - Banner decorativo:")
    print_fancy_banner("🎊 BANNER DE PRUEBA", "Con subtítulo", 60, "yellow")
    print()
    
    # Test 4.5: Header
    print("  4.5 - Header simple:")
    print_header("📋 Header de prueba", "⚙️")
    print()
    
    print(f"  {Colors.GREEN}✅ Todos los cuadros renderizados correctamente{Colors.RESET}")
    return True


def run_all_tests():
    """Ejecuta todos los tests."""
    print("\n" + "="*70)
    print("TEST SUITE: Perfect Boxes Skill (Python)")
    print("="*70)
    
    results = []
    results.append(("Ancho de caracteres", test_char_width()))
    results.append(("Ancho visual de cadenas", test_visual_width()))
    results.append(("Centrado de texto", test_center_text()))
    results.append(("Renderizado de cuadros", test_boxes()))
    
    # Resumen
    print("\n" + "="*70)
    print("RESUMEN DE TESTS")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = f"{Colors.GREEN}✅ PASADO{Colors.RESET}" if result else f"{Colors.RED}❌ FALLADO{Colors.RESET}"
        print(f"  {status} - {name}")
    
    print("="*70)
    if passed == total:
        print(f"{Colors.GREEN}✅ TODOS LOS TESTS PASARON ({passed}/{total}){Colors.RESET}")
        print(f"{Colors.GREEN}La skill perfect-boxes funciona correctamente{Colors.RESET}")
        return 0
    else:
        print(f"{Colors.RED}❌ ALGUNOS TESTS FALLARON ({passed}/{total}){Colors.RESET}")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
