#!/usr/bin/env python3
"""
Example 3: Spinner Styles

Demonstrates all available spinner animation styles.
"""

import time
from skills.cli_progress import Spinner


def main():
    print("=" * 50)
    print("  Spinner Styles Gallery")
    print("=" * 50)
    print()
    
    styles = [
        ("dots", "Default dots animation"),
        ("line", "Rotating line"),
        ("pipe", "Pipe animation"),
        ("star", "Star animation"),
        ("moon", "Moon phases"),
        ("clock", "Clock"),
        ("earth", "Earth rotation"),
        ("hearts", "Hearts"),
        ("bounce", "Bouncing ball"),
        ("runner", "Running person"),
    ]
    
    for style_name, description in styles:
        print(f"{style_name}: {description}")
        
        with Spinner(f"Loading with {style_name}...", style=style_name) as s:
            time.sleep(2)
            s.succeed(f"{style_name} complete!")
        
        print()
    
    # Different colors
    print("=" * 50)
    print("  Color Variations")
    print("=" * 50)
    print()
    
    colors = ["cyan", "green", "yellow", "red", "magenta", "blue"]
    
    for color in colors:
        with Spinner(f"Loading in {color}...", style="dots", color=color) as s:
            time.sleep(1)
            s.succeed(f"{color} done!")
        print()
    
    print("✅ Style gallery complete!")


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Install with: pip install rich")
