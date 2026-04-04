#!/usr/bin/env python3
"""
Demo: Uso práctico de Perfect Boxes Skill
Este script muestra cómo integrar la skill en una aplicación real.
"""

import sys
import time
from pathlib import Path

# Importar la skill (ajustar path relativo)
skill_path = Path(__file__).parent / "python"
sys.path.insert(0, str(skill_path))

from perfect_box import (
    print_perfect_box,
    print_fancy_banner,
    print_header
)

def simulate_app():
    """Simula una aplicación CLI usando la skill."""
    
    # Banner de bienvenida
    print_fancy_banner(
        "🚀 DIRTOPDF CLI - Demo",
        "Sistema de conversión de imágenes a PDF",
        width=70,
        color="cyan"
    )
    print()
    
    # Header de verificación
    print_header("📋 Verificando sistema", icon="🔍", color="yellow")
    time.sleep(0.5)
    print("  ✓ Python encontrado: 3.11.4")
    print("  ✓ Pillow instalado: 10.0.0")
    print("  ✓ PyPDF2 instalado: 3.0.1")
    print()
    
    # Cuadro de configuración
    print_perfect_box(
        title="⚙️ CONFIGURACIÓN",
        subtitle="Parámetros detectados",
        description="Carpeta: ./imagenes/ | Formato: PDF/A",
        width=65,
        color="blue"
    )
    print()
    
    # Header de procesamiento
    print_header("🔄 Procesando archivos", icon="⚡", color="cyan")
    time.sleep(0.5)
    
    archivos = [
        ("foto001.jpg", "✅"),
        ("foto002.png", "✅"),
        ("foto003.jpg", "✅"),
        ("documento.pdf", "⏭️"),  # Skipped
        ("foto004.jpg", "✅"),
    ]
    
    for archivo, status in archivos:
        print(f"  {status} {archivo}")
        time.sleep(0.3)
    
    print()
    
    # Cuadro de éxito
    print_perfect_box(
        title="✨ 🎉 ¡PROCESO COMPLETADO! 🎊",
        subtitle="Todos los archivos fueron procesados exitosamente",
        description="Archivo generado: output.pdf | Tamaño: 2.4 MB",
        width=70,
        color="green"
    )
    print()
    
    # Información adicional
    print_header("📊 Estadísticas", icon="📈", color="magenta")
    print("  • Archivos procesados: 4")
    print("  • Archivos omitidos: 1")
    print("  • Tiempo total: 1.8 segundos")
    print("  • Tasa de éxito: 100%")
    print()
    
    print("✅ Demo completada. La skill 'perfect-boxes' funciona perfectamente!")
    print()


if __name__ == "__main__":
    try:
        simulate_app()
    except KeyboardInterrupt:
        print("\n\n⚠️  Proceso interrumpido por el usuario")
        sys.exit(1)
