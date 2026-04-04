#!/usr/bin/env python3
"""
cli_banners.py - Professional ASCII art and banner generator
Generates high-quality CLI banners without external dependencies

For complete alphabet with multiple styles, see: alphabet.py
    - BLOCK: Bold block letters (6 lines)
    - SLIM: Thinner letters (5 lines)
    - MINI: Compact letters (3 lines)
    - SIMPLE: Pure ASCII (no unicode)

Usage:
    from cli_banners import generate_text, generate_shape
    
    # Using built-in fonts
    banner = generate_text("HELLO", style="block", color="cyan")
    
    # Using extended alphabet (more styles)
    from alphabet import render_text, ALPHABET
    banner = render_text("HELLO WORLD", style="mini", color="green")
"""

import sys
import time
from typing import Optional, Dict, List, Tuple, Callable

# Try to import extended alphabet
try:
    from .alphabet import ALPHABET, render_text as render_extended, STYLE_INFO
    HAS_EXTENDED = True
except ImportError:
    try:
        from alphabet import ALPHABET, render_text as render_extended, STYLE_INFO
        HAS_EXTENDED = True
    except ImportError:
        HAS_EXTENDED = False

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


# =============================================================================
# FONTS - Now use alphabet.py for complete character sets
# Minimal fallback fonts kept for backwards compatibility when alphabet.py unavailable
# =============================================================================

# Minimal fallback font (only used when alphabet.py is not available)
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
        style: Font style:
            - "block": Bold block letters (6 lines) - default
            - "minimal": Minimal box-drawing (3 lines) - fallback
            - "slim": Thinner block letters (5 lines) - requires alphabet.py
            - "mini": Compact letters (3 lines) - requires alphabet.py
            - "simple": Pure ASCII (5 lines) - requires alphabet.py
        color: Optional ANSI color name (red, green, yellow, blue, cyan, etc.)
        width: Optional max width (not yet implemented)
        
    Returns:
        ASCII art as string
    
    Example:
        >>> print(generate_text("HELLO", style="block", color="cyan"))
    """
    # Use extended alphabet for all styles when available
    if HAS_EXTENDED:
        if style in ('slim', 'mini', 'simple', 'block'):
            return render_extended(text, style=style, color=color)
    
    text = text.upper()
    
    # Fallback to minimal font when alphabet.py not available
    font = FONT_MINIMAL
    height = 3
    
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
    styles = ['block', 'minimal']
    if HAS_EXTENDED:
        styles.extend(['slim', 'mini', 'simple'])
    return styles


def get_available_characters(style: str = 'block') -> List[str]:
    """Return list of available characters for a style."""
    if HAS_EXTENDED and style in ALPHABET:
        return sorted(ALPHABET[style].keys())
    
    # Fallback to minimal font
    return sorted(FONT_MINIMAL.keys())


def get_available_shapes() -> List[str]:
    """Return list of available shapes."""
    return list(SHAPES.keys())


# =============================================================================
# ANIMATION FUNCTIONS
# =============================================================================

def animate_typewriter(
    text: str,
    delay: float = 0.05,
    color: Optional[str] = None
) -> None:
    """
    Animate text with typewriter effect (character by character).
    
    Args:
        text: Text to animate
        delay: Delay between characters in seconds
        color: Optional color to apply
    
    Example:
        >>> animate_typewriter("Loading...", delay=0.1)
    """
    if color:
        text = colorize(text, color)
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    print()  # New line after animation


def animate_fade_in(
    text: str,
    line_delay: float = 0.1,
    color: Optional[str] = None
) -> None:
    """
    Animate banner with fade-in effect (line by line).
    
    Args:
        text: Multi-line text/banner to animate
        line_delay: Delay between lines in seconds
        color: Optional color to apply
    
    Example:
        >>> banner = generate_text("HELLO", style="block")
        >>> animate_fade_in(banner, line_delay=0.2)
    """
    lines = text.split('\n')
    
    for line in lines:
        if color:
            line = colorize(line, color)
        print(line)
        time.sleep(line_delay)


def animate_bounce(
    text: str,
    bounce_count: int = 2,
    delay: float = 0.1,
    color: Optional[str] = None
) -> None:
    """
    Animate banner with bounce effect.
    
    Args:
        text: Text to animate
        bounce_count: Number of bounces
        delay: Delay between bounces
        color: Optional color
    
    Example:
        >>> banner = generate_text("SUCCESS", style="block")
        >>> animate_bounce(banner, bounce_count=3)
    """
    lines = text.split('\n')
    
    for bounce in range(bounce_count):
        # Clear previous lines on bounce (except first)
        if bounce > 0:
            for _ in lines:
                sys.stdout.write('\033[A\033[K')  # Move up and clear
        
        # Print with color
        output = text
        if color:
            output = colorize(output, color)
        print(output)
        
        time.sleep(delay)


def animate_spinner_loading(
    text: str = "Loading",
    frames: Optional[List[str]] = None,
    duration: float = 2.0,
    color: Optional[str] = None
) -> None:
    """
    Animate text with spinning cursor.
    
    Args:
        text: Text to display
        frames: Custom spinner frames (default: ◐ ◓ ◑ ◒)
        duration: Total animation duration in seconds
        color: Optional color
    
    Example:
        >>> animate_spinner_loading("Processing", duration=3.0, color="cyan")
    """
    if frames is None:
        frames = ['◐', '◓', '◑', '◒']
    
    start_time = time.time()
    frame_idx = 0
    
    while time.time() - start_time < duration:
        frame = frames[frame_idx % len(frames)]
        output = f"{frame} {text}"
        
        if color:
            output = colorize(output, color)
        
        sys.stdout.write(f'\r{output}')
        sys.stdout.flush()
        
        time.sleep(0.1)
        frame_idx += 1
    
    # Clear the line
    sys.stdout.write('\r' + ' ' * (len(text) + 4) + '\r')
    sys.stdout.flush()


# =============================================================================
# INTERACTIVE BANNER GENERATOR
# =============================================================================

def interactive_banner(
    text: str,
    use_questionary: bool = True
) -> None:
    """
    Create banner interactively with style and animation selection.
    
    Args:
        text: Text to display in banner
        use_questionary: Use questionary for prompts (requires cli-prompts skill)
    
    Example:
        >>> interactive_banner("WELCOME")
    """
    
    # Try to use questionary for better UX
    if use_questionary:
        try:
            import questionary
            
            # Ask for style
            style = questionary.select(
                "🎨 Select banner style:",
                choices=get_available_styles(),
                default='block'
            ).ask()
            
            # Ask for color
            colors_list = [
                'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
                'bright_red', 'bright_green', 'bright_yellow', 'bright_blue',
                'bright_magenta', 'bright_cyan', 'bright_white', 'none'
            ]
            color = questionary.select(
                "🎨 Select color:",
                choices=colors_list,
                default='cyan'
            ).ask()
            
            if color == 'none':
                color = None
            
            # Ask for animation
            animations = [
                ('none', 'No animation - instant display'),
                ('typewriter', 'Typewriter effect'),
                ('fade_in', 'Fade in line by line'),
                ('bounce', 'Bounce effect'),
                ('spinner', 'Spinner loading animation')
            ]
            
            animation = questionary.select(
                "✨ Select animation:",
                choices=[f"{name}: {desc}" for name, desc in animations],
                default='none'
            ).ask()
            
            # Extract animation name
            animation = animation.split(':')[0].strip()
            
        except ImportError:
            print("⚠️  questionary not available, using simple prompts")
            use_questionary = False
    
    # Fallback to simple input
    if not use_questionary:
        print("\n🎨 Available Styles:", ", ".join(get_available_styles()))
        style = input("Select style [block]: ").strip() or 'block'
        
        print("\n🎨 Available Colors: red, green, yellow, blue, cyan, white, none")
        color_input = input("Select color [cyan]: ").strip() or 'cyan'
        color = None if color_input == 'none' else color_input
        
        print("\n✨ Available Animations: none, typewriter, fade_in, bounce, spinner")
        animation = input("Select animation [none]: ").strip() or 'none'
    
    # Generate banner
    banner = generate_text(text, style=style, color=color)
    
    # Apply animation
    print()  # Spacing
    
    if animation == 'none':
        print(banner)
    elif animation == 'typewriter':
        animate_typewriter(banner, delay=0.02, color=None)  # Color already in banner
    elif animation == 'fade_in':
        animate_fade_in(banner, line_delay=0.1, color=None)
    elif animation == 'bounce':
        animate_bounce(banner, bounce_count=2, delay=0.15, color=None)
    elif animation == 'spinner':
        # Show spinner while displaying
        animate_spinner_loading(f"Generating {text}", duration=1.5)
        print(banner)
    
    print()  # Final spacing


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
    
    # Demo 6: Extended alphabet styles (if available)
    if HAS_EXTENDED:
        print("6. Extended Alphabet Styles:")
        print("\n   SLIM style:")
        print(generate_text("ABC", style="slim", color="yellow"))
        print("\n   MINI style:")
        print(generate_text("XYZ", style="mini", color="magenta"))
        print("\n   SIMPLE style (pure ASCII):")
        print(generate_text("123", style="simple"))
        print()
        
        print("7. Available styles:", get_available_styles())
        print()
    
    # Demo: Available characters
    print("8. Available characters in 'block' style:")
    chars = get_available_characters('block')
    print(f"   {' '.join(chars[:26])}")
    print(f"   {' '.join(chars[26:])}")


if __name__ == "__main__":
    demo()
