#!/usr/bin/env python3
"""
perfect_box.py - Funciones para dibujar cuadros perfectos en terminal
Soluciona el problema de desalineación con emojis (caracteres de ancho doble)

Implementa el algoritmo wcwidth (UAX #11) para calcular el ancho visual exacto.
"""

import re
import sys
from typing import Optional

# Colores ANSI
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    CYAN = '\033[0;36m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'

# Implementación simple de wcwidth (width calculation for wide characters)
def get_char_width(char: str) -> int:
    """
    Calcula el ancho visual de un carácter individual.
    
    Retorna:
    - 0: Caracteres de control, combinatorios
    - 1: ASCII normal, la mayoría de caracteres
    - 2: Emojis, caracteres de ancho doble (CJK, etc.)
    """
    if not char:
        return 0
    
    code_point = ord(char)
    
    # Caracteres de control (0x00-0x1F, 0x7F-0x9F)
    if code_point < 0x20 or (0x7F <= code_point < 0xA0):
        return 0
    
    # ASCII básico (0x20-0x7E)
    if 0x20 <= code_point <= 0x7E:
        return 1
    
    # Rangos de caracteres de ancho doble (East Asian Width)
    # Basado en Unicode UAX #11
    
    # Emojis comunes (ancho doble)
    if 0x1F000 <= code_point <= 0x1F9FF:  # Emojis, símbolos
        return 2
    
    # Más rangos de emojis
    if code_point in range(0x1F300, 0x1F5FF + 1):  # Símbolos diversos
        return 2
    if code_point in range(0x1F600, 0x1F64F + 1):  # Emoticonos
        return 2
    if code_point in range(0x1F680, 0x1F6FF + 1):  # Símbolos de transporte
        return 2
    if code_point in range(0x1F900, 0x1F9FF + 1):  # Símbolos suplementarios
        return 2
    if code_point in range(0x2600, 0x26FF + 1):    # Símbolos diversos
        return 2
    if code_point in range(0x2700, 0x27BF + 1):    # Dingbats
        return 2
    
    # Caracteres CJK (Chino, Japonés, Coreano) - ancho doble
    if 0x1100 <= code_point <= 0x115F:   # Hangul Jamo
        return 2
    if 0x2E80 <= code_point <= 0x2EFF:   # CJK Radicals
        return 2
    if 0x3000 <= code_point <= 0x303F:   # CJK Symbols
        return 2
    if 0x3040 <= code_point <= 0x309F:   # Hiragana
        return 2
    if 0x30A0 <= code_point <= 0x30FF:   # Katakana
        return 2
    if 0x3100 <= code_point <= 0x312F:   # Bopomofo
        return 2
    if 0x3130 <= code_point <= 0x318F:   # Hangul Compatibility Jamo
        return 2
    if 0x3190 <= code_point <= 0x319F:   # Kanbun
        return 2
    if 0x31A0 <= code_point <= 0x31BF:   # Bopomofo Extended
        return 2
    if 0x31C0 <= code_point <= 0x31EF:   # CJK Strokes
        return 2
    if 0x3200 <= code_point <= 0x32FF:   # Enclosed CJK
        return 2
    if 0x3300 <= code_point <= 0x33FF:   # CJK Compatibility
        return 2
    if 0x3400 <= code_point <= 0x4DBF:   # CJK Unified Ideographs Extension A
        return 2
    if 0x4E00 <= code_point <= 0x9FFF:   # CJK Unified Ideographs
        return 2
    if 0xA960 <= code_point <= 0xA97F:   # Hangul Jamo Extended-A
        return 2
    if 0xAC00 <= code_point <= 0xD7AF:   # Hangul Syllables
        return 2
    if 0xF900 <= code_point <= 0xFAFF:   # CJK Compatibility Ideographs
        return 2
    if 0xFE10 <= code_point <= 0xFE19:   # Vertical forms
        return 2
    if 0xFE30 <= code_point <= 0xFE6F:   # CJK Compatibility Forms
        return 2
    if 0xFF00 <= code_point <= 0xFF60:   # Fullwidth Forms
        return 2
    if 0xFFE0 <= code_point <= 0xFFE6:   # Fullwidth Forms
        return 2
    if 0x20000 <= code_point <= 0x2FFFD: # CJK Extension B-F
        return 2
    if 0x30000 <= code_point <= 0x3FFFD: # CJK Extension G
        return 2
    
    # Por defecto, ancho 1
    return 1


def get_visual_width(text: str) -> int:
    """
    Calcula el ancho visual total de una cadena.
    Considera emojis y caracteres de ancho doble correctamente.
    
    Args:
        text: Cadena a medir
        
    Returns:
        Ancho visual en celdas de terminal
    """
    # Remover códigos de escape ANSI (colores)
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    clean_text = ansi_escape.sub('', text)
    
    # Sumar el ancho de cada carácter
    return sum(get_char_width(char) for char in clean_text)


def truncate_text(text: str, max_width: int) -> str:
    """
    Trunca texto respetando el ancho visual.
    
    Args:
        text: Texto a truncar
        max_width: Ancho máximo en celdas
        
    Returns:
        Texto truncado con '...' si es necesario
    """
    if get_visual_width(text) <= max_width:
        return text
    
    result = ""
    width = 0
    
    for char in text:
        char_width = get_char_width(char)
        if width + char_width > max_width - 3:  # Dejar espacio para '...'
            return result + "..."
        result += char
        width += char_width
    
    return result


def center_text(text: str, total_width: int) -> str:
    """
    Centra texto respetando el ancho visual de emojis.
    
    Args:
        text: Texto a centrar
        total_width: Ancho total disponible
        
    Returns:
        Texto con padding para centrarlo
    """
    visual_width = get_visual_width(text)
    
    if visual_width >= total_width:
        return truncate_text(text, total_width)
    
    padding_left = (total_width - visual_width) // 2
    padding_right = total_width - visual_width - padding_left
    
    return ' ' * padding_left + text + ' ' * padding_right


def print_perfect_box(
    title: str,
    subtitle: str = "",
    description: str = "",
    icon: str = "",
    width: int = 60,
    color: str = "cyan"
) -> None:
    """
    Imprime un cuadro perfecto con bordes Unicode.
    
    Args:
        title: Título principal (obligatorio)
        subtitle: Subtítulo opcional
        description: Descripción adicional opcional
        icon: Emoji decorativo opcional
        width: Ancho total del cuadro en celdas (default: 60)
        color: Color del cuadro (cyan, green, yellow, red, blue, magenta)
    """
    # Mapeo de colores
    color_map = {
        'cyan': Colors.CYAN,
        'green': Colors.GREEN,
        'yellow': Colors.YELLOW,
        'red': Colors.RED,
        'blue': Colors.BLUE,
        'magenta': Colors.MAGENTA,
    }
    
    color_code = color_map.get(color.lower(), Colors.CYAN)
    
    # Caracteres del cuadro
    top_left = "╔"
    top_right = "╗"
    bottom_left = "╚"
    bottom_right = "╝"
    horizontal = "═"
    vertical = "║"
    
    # Ancho interno (sin bordes)
    inner_width = width - 2
    
    # Línea superior
    print(f"{color_code}{top_left}{horizontal * inner_width}{top_right}{Colors.RESET}")
    
    # Línea vacía
    print(f"{color_code}{vertical}{' ' * inner_width}{vertical}{Colors.RESET}")
    
    # Título con icono
    title_text = f"{icon} {title}".strip() if icon else title
    centered_title = center_text(title_text, inner_width)
    print(f"{color_code}{vertical}{Colors.BOLD}{centered_title}{Colors.RESET}{color_code}{vertical}{Colors.RESET}")
    
    # Subtítulo
    if subtitle:
        print(f"{color_code}{vertical}{' ' * inner_width}{vertical}{Colors.RESET}")
        centered_subtitle = center_text(subtitle, inner_width)
        print(f"{color_code}{vertical}{centered_subtitle}{vertical}{Colors.RESET}")
    
    # Descripción
    if description:
        print(f"{color_code}{vertical}{' ' * inner_width}{vertical}{Colors.RESET}")
        centered_desc = center_text(description, inner_width)
        print(f"{color_code}{vertical}{centered_desc}{vertical}{Colors.RESET}")
    
    # Línea vacía
    print(f"{color_code}{vertical}{' ' * inner_width}{vertical}{Colors.RESET}")
    
    # Línea inferior
    print(f"{color_code}{bottom_left}{horizontal * inner_width}{bottom_right}{Colors.RESET}")


def print_fancy_banner(title: str, subtitle: str = "", width: int = 60, color: str = "cyan") -> None:
    """
    Imprime un banner decorativo con solo bordes superior e inferior.
    
    Args:
        title: Título principal
        subtitle: Subtítulo opcional
        width: Ancho total del banner
        color: Color del banner
    """
    color_map = {
        'cyan': Colors.CYAN,
        'green': Colors.GREEN,
        'yellow': Colors.YELLOW,
        'red': Colors.RED,
        'blue': Colors.BLUE,
        'magenta': Colors.MAGENTA,
    }
    
    color_code = color_map.get(color.lower(), Colors.CYAN)
    horizontal = "═"
    
    # Línea superior
    print(f"{color_code}{horizontal * width}{Colors.RESET}")
    
    # Título centrado
    centered_title = center_text(title, width)
    print(f"{Colors.BOLD}{centered_title}{Colors.RESET}")
    
    # Subtítulo centrado
    if subtitle:
        centered_subtitle = center_text(subtitle, width)
        print(f"{color_code}{centered_subtitle}{Colors.RESET}")
    
    # Línea inferior
    print(f"{color_code}{horizontal * width}{Colors.RESET}")


def print_header(text: str, icon: str = "🚀", color: str = "cyan") -> None:
    """
    Imprime un encabezado de sección simple.
    
    Args:
        text: Texto del encabezado
        icon: Emoji decorativo
        color: Color del encabezado
    """
    color_map = {
        'cyan': Colors.CYAN,
        'green': Colors.GREEN,
        'yellow': Colors.YELLOW,
        'red': Colors.RED,
        'blue': Colors.BLUE,
        'magenta': Colors.MAGENTA,
    }
    
    color_code = color_map.get(color.lower(), Colors.CYAN)
    
    print()
    print(f"{color_code}{icon}  {Colors.BOLD}{text}{Colors.RESET}")
    print(f"{color_code}{'─' * 50}{Colors.RESET}")


def demo():
    """Función de demostración mostrando todos los casos de uso."""
    print("\n" + "="*70)
    print("DEMO: Perfect Boxes Skill")
    print("="*70 + "\n")
    
    # Ejemplo 1: Cuadro completo con emojis
    print("Ejemplo 1: Cuadro completo con emojis")
    print_perfect_box(
        title="📸 DIRTOPDF CLI 📄",
        subtitle="Convierte Carpetas de Imágenes en PDFs",
        description="Versión 1.0.0",
        width=62,
        color="cyan"
    )
    print()
    
    # Ejemplo 2: Banner simple
    print("Ejemplo 2: Banner decorativo")
    print_fancy_banner("🚀 PROYECTO INICIADO", "Ejecutando tareas...", 60, "green")
    print()
    
    # Ejemplo 3: Headers de sección
    print("Ejemplo 3: Headers de sección")
    print_header("📋 Paso 1: Preparación", icon="⚙️", color="yellow")
    print("  - Verificando archivos...")
    print("  - Cargando configuración...")
    print()
    
    print_header("✅ Paso 2: Completado", icon="✨", color="green")
    print("  - Todos los archivos procesados")
    print()
    
    # Ejemplo 4: Múltiples emojis
    print("Ejemplo 4: Cuadro con múltiples emojis")
    print_perfect_box(
        title="✨ 🎉 🚀 ¡ÉXITO! 🎊 🎈 ✅",
        subtitle="Proceso completado sin errores",
        width=60,
        color="green"
    )
    print()
    
    # Ejemplo 5: Sin emojis (solo ASCII)
    print("Ejemplo 5: Cuadro sin emojis (solo ASCII)")
    print_perfect_box(
        title="SISTEMA DE BACKUP",
        subtitle="Copia de seguridad automatica",
        description="Server: production-01",
        width=60,
        color="blue"
    )
    print()


if __name__ == "__main__":
    demo()
