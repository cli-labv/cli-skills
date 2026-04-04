"""
CLI Banners Skill - Professional ASCII art and banner generator

Main exports:
    - generate_text: Generate ASCII text with various styles
    - generate_shape: Generate ASCII shapes and symbols
    - animate_typewriter: Typewriter animation effect
    - animate_fade_in: Fade-in animation line by line
    - animate_bounce: Bounce animation effect
    - animate_spinner_loading: Spinner loading animation
    - interactive_banner: Interactive banner with style/color/animation selection
    - get_available_styles: List available text styles
    - get_available_shapes: List available shapes
    - colorize: Apply ANSI color codes
"""

try:
    from .python.cli_banners import (
        generate_text,
        generate_shape,
        animate_typewriter,
        animate_fade_in,
        animate_bounce,
        animate_spinner_loading,
        interactive_banner,
        get_available_styles,
        get_available_shapes,
        get_available_characters,
        colorize,
    )
except ImportError:
    from python.cli_banners import (
        generate_text,
        generate_shape,
        animate_typewriter,
        animate_fade_in,
        animate_bounce,
        animate_spinner_loading,
        interactive_banner,
        get_available_styles,
        get_available_shapes,
        get_available_characters,
        colorize,
    )

__all__ = [
    'generate_text',
    'generate_shape',
    'animate_typewriter',
    'animate_fade_in',
    'animate_bounce',
    'animate_spinner_loading',
    'interactive_banner',
    'get_available_styles',
    'get_available_shapes',
    'get_available_characters',
    'colorize',
]

__version__ = '1.1.0'
__description__ = 'Professional ASCII art and banner generator with animations'
