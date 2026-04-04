#!/usr/bin/env python3
"""
showcase.py - Demostración visual completa de la skill Perfect Boxes
Muestra todos los casos de uso y capacidades de manera atractiva.
"""

import sys
import time
from pathlib import Path

# Importar la skill
skill_path = Path(__file__).parent / "python"
sys.path.insert(0, str(skill_path))

from perfect_box import (
    print_perfect_box,
    print_fancy_banner,
    print_header,
    Colors
)

def pause(seconds=1.5):
    """Pausa para mejor visualización."""
    time.sleep(seconds)

def showcase():
    """Muestra todas las capacidades de la skill."""
    
    # Intro
    print("\n" * 2)
    print_fancy_banner(
        "✨ PERFECT BOXES SKILL ✨",
        "Cuadros Unicode perfectos con soporte completo de emojis",
        width=75,
        color="cyan"
    )
    pause()
    
    # Sección 1: El Problema
    print("\n")
    print_header("❌ EL PROBLEMA", icon="⚠️", color="red")
    print()
    print("  Los emojis ocupan 2 celdas en terminal, pero len() retorna 1:")
    print()
    print("    >>> len('📸 Text')")
    print("    6  ❌ Incorrecto (el emoji ocupa 2 celdas)")
    print()
    print("  Esto causa desalineación en cuadros Unicode:")
    print()
    print("    ╔════════════════════════════════════╗")
    print("    ║  📸 MI APP                          ║  ← ¡Desalineado!")
    print("    ╚════════════════════════════════════╝")
    pause(2)
    
    # Sección 2: La Solución
    print("\n")
    print_header("✅ LA SOLUCIÓN", icon="💡", color="green")
    print()
    print("  La skill calcula el ancho VISUAL real:")
    print()
    print("    >>> get_visual_width('📸 Text')")
    print("    7  ✅ Correcto (2 + 1 + 4 = 7 celdas)")
    print()
    print("  Resultado: cuadros perfectamente alineados:")
    print()
    
    print_perfect_box(
        title="📸 MI APP",
        subtitle="¡Perfectamente alineado!",
        width=50,
        color="green"
    )
    pause(2)
    
    # Sección 3: Ejemplos
    print("\n")
    print_header("🎨 GALERÍA DE EJEMPLOS", icon="🖼️", color="magenta")
    pause()
    
    # Ejemplo 1
    print("\n  📦 Cuadro básico sin emojis:")
    print_perfect_box(
        title="SISTEMA DE BACKUP",
        subtitle="Respaldo automatico diario",
        description="Server: production-01",
        width=60,
        color="blue"
    )
    pause()
    
    # Ejemplo 2
    print("\n  🎯 Cuadro con un emoji:")
    print_perfect_box(
        title="🚀 DEPLOY EXITOSO",
        subtitle="Aplicación desplegada en producción",
        description="Build #142 - Commit a3b9c12",
        width=65,
        color="green"
    )
    pause()
    
    # Ejemplo 3
    print("\n  🎊 Cuadro con múltiples emojis:")
    print_perfect_box(
        title="✨ 🎉 🎊 ¡FELICIDADES! 🎈 🎁 ✅",
        subtitle="Has completado todos los logros",
        description="Nivel desbloqueado: Maestro",
        width=70,
        color="yellow"
    )
    pause()
    
    # Ejemplo 4
    print("\n  🌐 Banner decorativo:")
    print_fancy_banner(
        "📸 DIRTOPDF CLI 📄",
        "Convierte imágenes a PDF con calidad profesional",
        width=70,
        color="cyan"
    )
    pause()
    
    # Ejemplo 5
    print("\n  📋 Headers de sección:")
    print_header("⚙️ Configuración inicial", color="yellow")
    print("    • Cargando preferencias...")
    print("    • Verificando permisos...")
    print("    • Inicializando módulos...")
    pause()
    
    # Sección 4: Características
    print("\n")
    print_header("🎯 CARACTERÍSTICAS", icon="⭐", color="cyan")
    print()
    
    features = [
        ("✅", "Cálculo de ancho visual preciso (algoritmo wcwidth)"),
        ("✅", "Soporte completo de emojis modernos"),
        ("✅", "Caracteres CJK (chino, japonés, coreano)"),
        ("✅", "Colores configurables (6 opciones)"),
        ("✅", "Ancho de cuadro variable (30-100+ columnas)"),
        ("✅", "Centrado automático inteligente"),
        ("✅", "Sin dependencias externas"),
        ("✅", "Implementado en Python y Bash"),
    ]
    
    for icon, feature in features:
        print(f"    {icon} {feature}")
        time.sleep(0.3)
    
    pause()
    
    # Sección 5: Casos de Uso
    print("\n")
    print_header("💼 CASOS DE USO", icon="📂", color="blue")
    print()
    
    use_cases = [
        ("🚀", "Scripts de deployment", "Mensajes de status profesionales"),
        ("📦", "Instaladores CLI", "Banners de bienvenida atractivos"),
        ("🔧", "Herramientas DevOps", "Reportes de estado claros"),
        ("📊", "Dashboards en terminal", "Visualización de datos estructurada"),
        ("🎮", "Aplicaciones interactivas", "Menús y diálogos elegantes"),
        ("📝", "Generadores de reportes", "Encabezados y secciones definidas"),
    ]
    
    for emoji, title, description in use_cases:
        print(f"    {emoji} {Colors.BOLD}{title}{Colors.RESET}")
        print(f"       {description}")
        time.sleep(0.4)
    
    pause()
    
    # Sección 6: Comparación
    print("\n")
    print_header("📊 ANTES vs DESPUÉS", icon="🔄", color="yellow")
    print()
    
    print(f"  {Colors.RED}❌ ANTES (función estándar):{Colors.RESET}")
    print("     def print_title(text):")
    print("         width = 50")
    print("         padding = (width - len(text)) // 2")
    print("         print(' ' * padding + text)")
    print()
    print("     print_title('📸 MI APP')")
    print("     # Resultado: desalineado ❌")
    print()
    
    print(f"  {Colors.GREEN}✅ DESPUÉS (perfect-boxes skill):{Colors.RESET}")
    print("     from perfect_box import print_fancy_banner")
    print()
    print("     print_fancy_banner('📸 MI APP', width=50)")
    print("     # Resultado: perfecto ✅")
    print()
    
    pause(2)
    
    # Sección 7: Instalación
    print("\n")
    print_header("📥 CÓMO USAR", icon="💻", color="cyan")
    print()
    print(f"  {Colors.BOLD}Python:{Colors.RESET}")
    print("    from skills.perfect_boxes.python.perfect_box import print_perfect_box")
    print("    print_perfect_box('Mi título', 'Subtítulo', width=60)")
    print()
    print(f"  {Colors.BOLD}Bash:{Colors.RESET}")
    print("    source skills/perfect-boxes/bash/perfect_banner.sh")
    print("    print_perfect_box 'Mi título' 'Subtítulo'")
    print()
    
    pause()
    
    # Final
    print("\n")
    print_perfect_box(
        title="✨ 🎉 ¡GRACIAS POR VER LA DEMO! 🎊 ✨",
        subtitle="La skill perfect-boxes está lista para usar",
        description="Lee el README.md para más información",
        width=75,
        color="green"
    )
    
    print("\n")
    print(f"  📚 Documentación: {Colors.CYAN}skills/perfect-boxes/README.md{Colors.RESET}")
    print(f"  🔧 Integración: {Colors.CYAN}skills/perfect-boxes/INTEGRATION.md{Colors.RESET}")
    print(f"  🧪 Tests: {Colors.CYAN}python3 skills/perfect-boxes/python/test_perfect_box.py{Colors.RESET}")
    print(f"  📦 Ejemplos: {Colors.CYAN}skills/perfect-boxes/examples/{Colors.RESET}")
    print("\n")


if __name__ == "__main__":
    try:
        showcase()
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrumpida\n")
        sys.exit(0)
