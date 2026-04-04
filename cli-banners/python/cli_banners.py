#!/usr/bin/env python3
"""
cli_banners.py - Professional ASCII art and banner generator
Generates high-quality CLI banners without external dependencies
"""

import sys
from typing import Optional, Dict, List, Tuple

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Standard colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'


# Font definitions (character matrices)
# Each character is represented as a list of strings (lines)

FONT_BLOCK = {
    'A': [
        '  █████╗ ',
        ' ██╔══██╗',
        ' ███████║',
        ' ██╔══██║',
        ' ██║  ██║',
        ' ╚═╝  ╚═╝'
    ],
    'B': [
        ' ██████╗ ',
        ' ██╔══██╗',
        ' ██████╔╝',
        ' ██╔══██╗',
        ' ██████╔╝',
        ' ╚═════╝ '
    ],
    'C': [
        '  ██████╗',
        ' ██╔════╝',
        ' ██║     ',
        ' ██║     ',
        ' ╚██████╗',
        '  ╚═════╝'
    ],
    'D': [
        ' ██████╗ ',
        ' ██╔══██╗',
        ' ██║  ██║',
        ' ██║  ██║',
        ' ██████╔╝',
        ' ╚═════╝ '
    ],
    'E': [
        ' ███████╗',
        ' ██╔════╝',
        ' █████╗  ',
        ' ██╔══╝  ',
        ' ███████╗',
        ' ╚══════╝'
    ],
    'F': [
        ' ███████╗',
        ' ██╔════╝',
        ' █████╗  ',
        ' ██╔══╝  ',
        ' ██║     ',
        ' ╚═╝     '
    ],
    'G': [
        '  ██████╗ ',
        ' ██╔════╝ ',
        ' ██║  ███╗',
        ' ██║   ██║',
        ' ╚██████╔╝',
        '  ╚═════╝ '
    ],
    'H': [
        ' ██╗  ██╗',
        ' ██║  ██║',
        ' ███████║',
        ' ██╔══██║',
        ' ██║  ██║',
        ' ╚═╝  ╚═╝'
    ],
    'I': [
        ' ██╗',
        ' ██║',
        ' ██║',
        ' ██║',
        ' ██║',
        ' ╚═╝'
    ],
    'J': [
        '      ██╗',
        '      ██║',
        '      ██║',
        ' ██   ██║',
        ' ╚█████╔╝',
        '  ╚════╝ '
    ],
    'K': [
        ' ██╗  ██╗',
        ' ██║ ██╔╝',
        ' █████╔╝ ',
        ' ██╔═██╗ ',
        ' ██║  ██╗',
        ' ╚═╝  ╚═╝'
    ],
    'L': [
        ' ██╗     ',
        ' ██║     ',
        ' ██║     ',
        ' ██║     ',
        ' ███████╗',
        ' ╚══════╝'
    ],
    'M': [
        ' ███╗   ███╗',
        ' ████╗ ████║',
        ' ██╔████╔██║',
        ' ██║╚██╔╝██║',
        ' ██║ ╚═╝ ██║',
        ' ╚═╝     ╚═╝'
    ],
    'N': [
        ' ███╗   ██╗',
        ' ████╗  ██║',
        ' ██╔██╗ ██║',
        ' ██║╚██╗██║',
        ' ██║ ╚████║',
        ' ╚═╝  ╚═══╝'
    ],
    'O': [
        '  ██████╗ ',
        ' ██╔═══██╗',
        ' ██║   ██║',
        ' ██║   ██║',
        ' ╚██████╔╝',
        '  ╚═════╝ '
    ],
    'P': [
        ' ██████╗ ',
        ' ██╔══██╗',
        ' ██████╔╝',
        ' ██╔═══╝ ',
        ' ██║     ',
        ' ╚═╝     '
    ],
    'Q': [
        '  ██████╗ ',
        ' ██╔═══██╗',
        ' ██║   ██║',
        ' ██║▄▄ ██║',
        ' ╚██████╔╝',
        '  ╚══▀▀═╝ '
    ],
    'R': [
        ' ██████╗ ',
        ' ██╔══██╗',
        ' ██████╔╝',
        ' ██╔══██╗',
        ' ██║  ██║',
        ' ╚═╝  ╚═╝'
    ],
    'S': [
        ' ███████╗',
        ' ██╔════╝',
        ' ███████╗',
        ' ╚════██║',
        ' ███████║',
        ' ╚══════╝'
    ],
    'T': [
        ' ████████╗',
        ' ╚══██╔══╝',
        '    ██║   ',
        '    ██║   ',
        '    ██║   ',
        '    ╚═╝   '
    ],
    'U': [
        ' ██╗   ██╗',
        ' ██║   ██║',
        ' ██║   ██║',
        ' ██║   ██║',
        ' ╚██████╔╝',
        '  ╚═════╝ '
    ],
    'V': [
        ' ██╗   ██╗',
        ' ██║   ██║',
        ' ██║   ██║',
        ' ╚██╗ ██╔╝',
        '  ╚████╔╝ ',
        '   ╚═══╝  '
    ],
    'W': [
        ' ██╗    ██╗',
        ' ██║    ██║',
        ' ██║ █╗ ██║',
        ' ██║███╗██║',
        ' ╚███╔███╔╝',
        '  ╚══╝╚══╝ '
    ],
    'X': [
        ' ██╗  ██╗',
        ' ╚██╗██╔╝',
        '  ╚███╔╝ ',
        '  ██╔██╗ ',
        ' ██╔╝ ██╗',
        ' ╚═╝  ╚═╝'
    ],
    'Y': [
        ' ██╗   ██╗',
        ' ╚██╗ ██╔╝',
        '  ╚████╔╝ ',
        '   ╚██╔╝  ',
        '    ██║   ',
        '    ╚═╝   '
    ],
    'Z': [
        ' ███████╗',
        ' ╚══███╔╝',
        '   ███╔╝ ',
        '  ███╔╝  ',
        ' ███████╗',
        ' ╚══════╝'
    ],
    '0': [
        '  ██████╗ ',
        ' ██╔══██╗',
        ' ██║  ██║',
        ' ██║  ██║',
        ' ╚█████╔╝',
        '  ╚════╝ '
    ],
    '1': [
        ' ██╗',
        '███║',
        '╚██║',
        ' ██║',
        ' ██║',
        ' ╚═╝'
    ],
    '2': [
        ' ██████╗ ',
        '██╔════╝ ',
        '███████╗ ',
        '╚════██║ ',
        '██████╔╝ ',
        '╚═════╝  '
    ],
    '3': [
        ' ██████╗ ',
        '██╔═══██╗',
        '╚════██╔╝',
        ' █████╔╝ ',
        ' ╚═══██╗ ',
        ' █████╔╝ ',
        ' ╚════╝  '
    ],
    ' ': [
        '   ',
        '   ',
        '   ',
        '   ',
        '   ',
        '   '
    ],
    '!': [
        ' ██╗',
        ' ██║',
        ' ██║',
        ' ╚═╝',
        ' ██╗',
        ' ╚═╝'
    ],
    '?': [
        ' ██████╗ ',
        '██╔═══██╗',
        '╚═══███╔╝',
        '   ███╔╝ ',
        '   ╚═╝   ',
        '   ██╗   ',
        '   ╚═╝   '
    ],
}

FONT_MINIMAL = {
    'A': ['┌─┐', '├─┤', '┴ ┴'],
    'B': ['┌┐ ', '├┴┐', '└─┘'],
    'C': ['┌─┐', '│  ', '└─┘'],
    'D': ['┌┬┐', ' ││', '─┴┘'],
    'E': ['┌─┐', '├┤ ', '└─┘'],
    'F': ['┌─┐', '├┤ ', '└  '],
    'G': ['┌─┐', '│ ┬', '└─┘'],
    'H': ['┬ ┬', '├─┤', '┴ ┴'],
    'I': ['┬', '│', '┴'],
    'J': ['  ┬', '  │', '└─┘'],
    'K': ['┬┌─', '├┴┐', '┴ ┴'],
    'L': ['┬  ', '│  ', '┴─┘'],
    'M': ['┌┬┐', '│││', '┴ ┴'],
    'N': ['┌┐┌', '│││', '┘└┘'],
    'O': ['┌─┐', '│ │', '└─┘'],
    'P': ['┌─┐', '├─┘', '┴  '],
    'Q': ['┌─┐', '│ │', '└─└'],
    'R': ['┬─┐', '├┬┘', '┴└─'],
    'S': ['┌─┐', '└─┐', '└─┘'],
    'T': ['┌┬┐', ' │ ', ' ┴ '],
    'U': ['┬ ┬', '│ │', '└─┘'],
    'V': ['┬  ┬', '└┐┌┘', ' └┘ '],
    'W': ['┬ ┬', '│││', '└┴┘'],
    'X': ['─┐ ┬', '┌┴┬┘', '┴ └─'],
    'Y': ['┬ ┬', '└┬┘', ' ┴ '],
    'Z': ['┌─┐', '┌─┘', '└─┘'],
    ' ': ['   ', '   ', '   '],
    '0': ['┌─┐', '│ │', '└─┘'],
    '1': ['╷', '│', '╵'],
    '!': ['╷', '│', '·'],
}

# Shapes definitions
SHAPES = {
    'arrow_right': {
        'minimal': ['→'],
        'block': ['▶'],
        'shaded': ['▸'],
        'detailed': ['⟹']
    },
    'arrow_left': {
        'minimal': ['←'],
        'block': ['◀'],
        'shaded': ['◂'],
        'detailed': ['⟸']
    },
    'arrow_up': {
        'minimal': ['↑'],
        'block': ['▲'],
        'shaded': ['△'],
        'detailed': ['⬆']
    },
    'arrow_down': {
        'minimal': ['↓'],
        'block': ['▼'],
        'shaded': ['▽'],
        'detailed': ['⬇']
    },
    'check': {
        'minimal': ['✓'],
        'block': ['✔'],
        'shaded': ['☑'],
        'detailed': ['✅']
    },
    'cross': {
        'minimal': ['✗'],
        'block': ['✘'],
        'shaded': ['☒'],
        'detailed': ['❌']
    },
    'star': {
        'minimal': ['☆'],
        'block': ['★'],
        'shaded': ['✦'],
        'detailed': ['⭐']
    },
    'heart': {
        'minimal': ['♡'],
        'block': ['♥'],
        'shaded': ['❤'],
        'detailed': ['💖']
    },
    'loading': {
        'minimal': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
        'block': ['◐', '◓', '◑', '◒'],
        'detailed': ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    },
}


def colorize(text: str, color: Optional[str] = None) -> str:
    """Apply ANSI color to text."""
    if not color:
        return text
    
    color_map = {
        'red': Colors.RED,
        'green': Colors.GREEN,
        'yellow': Colors.YELLOW,
        'blue': Colors.BLUE,
        'magenta': Colors.MAGENTA,
        'cyan': Colors.CYAN,
        'white': Colors.WHITE,
        'bright_red': Colors.BRIGHT_RED,
        'bright_green': Colors.BRIGHT_GREEN,
        'bright_yellow': Colors.BRIGHT_YELLOW,
        'bright_blue': Colors.BRIGHT_BLUE,
        'bright_magenta': Colors.BRIGHT_MAGENTA,
        'bright_cyan': Colors.BRIGHT_CYAN,
        'bright_white': Colors.BRIGHT_WHITE,
    }
    
    color_code = color_map.get(color.lower(), '')
    if not color_code:
        return text
    
    return f"{color_code}{text}{Colors.RESET}"


def generate_text(
    text: str,
    style: str = 'block',
    color: Optional[str] = None,
    width: Optional[int] = None
) -> str:
    """
    Generate ASCII art text.
    
    Args:
        text: Text to convert
        style: "block" or "minimal"
        color: Optional ANSI color name
        width: Optional max width (not yet implemented)
        
    Returns:
        ASCII art as string
    """
    text = text.upper()
    
    # Select font
    if style == 'minimal':
        font = FONT_MINIMAL
        height = 3
    else:  # block
        font = FONT_BLOCK
        height = 6
    
    # Build the output
    lines = ['' for _ in range(height)]
    
    for char in text:
        if char not in font:
            # Use space for unknown characters
            char = ' '
        
        char_lines = font[char]
        for i, line in enumerate(char_lines):
            if i < height:
                lines[i] += line + ' '
    
    # Join lines
    result = '\n'.join(lines)
    
    # Apply color
    if color:
        result = colorize(result, color)
    
    return result


def generate_shape(
    shape_type: str,
    style: str = 'block',
    size: str = 'medium',
    color: Optional[str] = None
) -> str:
    """
    Generate ASCII shape or symbol.
    
    Args:
        shape_type: Type of shape (e.g., "arrow_right", "check")
        style: "minimal", "block", "shaded", or "detailed"
        size: "small", "medium", "large" (affects spacing, not all shapes)
        color: Optional ANSI color
        
    Returns:
        ASCII shape as string
    """
    if shape_type not in SHAPES:
        return f"[Unknown shape: {shape_type}]"
    
    shape_styles = SHAPES[shape_type]
    
    # Get the shape for the requested style
    if style in shape_styles:
        shape_lines = shape_styles[style]
    elif 'block' in shape_styles:
        shape_lines = shape_styles['block']
    else:
        shape_lines = list(shape_styles.values())[0]
    
    # For loading shapes, return first frame
    if isinstance(shape_lines, list) and len(shape_lines) > 1 and shape_type == 'loading':
        result = shape_lines[0]
    else:
        result = '\n'.join(shape_lines) if isinstance(shape_lines, list) else shape_lines[0]
    
    # Apply color
    if color:
        result = colorize(result, color)
    
    return result


def get_available_styles() -> List[str]:
    """Return list of available text styles."""
    return ['block', 'minimal']


def get_available_shapes() -> List[str]:
    """Return list of available shapes."""
    return list(SHAPES.keys())


def demo():
    """Demonstration of cli_banners functionality."""
    print("\n" + "="*70)
    print("CLI BANNERS - ASCII Art Generator")
    print("="*70 + "\n")
    
    # Demo 1: Block style text
    print("1. Block Style Text:")
    print(generate_text("HELLO", style="block", color="cyan"))
    print()
    
    # Demo 2: Minimal style text
    print("2. Minimal Style Text:")
    print(generate_text("WORLD", style="minimal", color="green"))
    print()
    
    # Demo 3: Shapes
    print("3. Shapes:")
    print(f"  Arrow Right: {generate_shape('arrow_right', style='block', color='yellow')}")
    print(f"  Check: {generate_shape('check', style='detailed', color='green')}")
    print(f"  Cross: {generate_shape('cross', style='detailed', color='red')}")
    print(f"  Star: {generate_shape('star', style='block', color='bright_yellow')}")
    print()
    
    # Demo 4: Use case
    print("4. Use Case - Status Messages:")
    check = generate_shape('check', style='detailed', color='green')
    cross = generate_shape('cross', style='detailed', color='red')
    print(f"  {check} Build successful")
    print(f"  {check} Tests passed")
    print(f"  {cross} Deployment failed")
    print()
    
    # Demo 5: Available shapes
    print("5. Available Shapes:")
    for shape in get_available_shapes():
        symbol = generate_shape(shape, style='block')
        print(f"  • {shape}: {symbol}")
    print()


if __name__ == "__main__":
    demo()
