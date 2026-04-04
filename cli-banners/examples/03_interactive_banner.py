#!/usr/bin/env python3
"""
Interactive Banner Generator with Animations

This example demonstrates the interactive banner generation feature
with style, color, and animation selection.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python'))

from cli_banners import (
    interactive_banner,
    animate_typewriter,
    animate_fade_in,
    animate_bounce,
    animate_spinner_loading,
    generate_text,
    generate_shape
)


def example_1_simple_interactive():
    """Example 1: Simple interactive banner"""
    print("\n" + "="*70)
    print("Example 1: Interactive Banner")
    print("="*70)
    
    interactive_banner("WELCOME")


def example_2_animations():
    """Example 2: Show all animation types"""
    print("\n" + "="*70)
    print("Example 2: Animation Types")
    print("="*70)
    
    text = "BANNER"
    
    # Generate banner
    banner = generate_text(text, style="block", color="cyan")
    
    print("\n1️⃣  No Animation (instant):")
    print(banner)
    
    print("\n2️⃣  Typewriter Effect:")
    animate_typewriter(banner, delay=0.02)
    
    print("\n3️⃣  Fade In (line by line):")
    animate_fade_in(banner, line_delay=0.15)
    
    print("\n4️⃣  Bounce Effect:")
    animate_bounce(banner, bounce_count=2, delay=0.2)
    
    print("\n5️⃣  Spinner Loading:")
    animate_spinner_loading("Preparing banner", duration=1.5, color="yellow")
    print(banner)


def example_3_styled_banners():
    """Example 3: Different styles with animations"""
    print("\n" + "="*70)
    print("Example 3: Styled Banners with Animations")
    print("="*70)
    
    styles = ['block', 'slim', 'mini', 'simple']
    colors = ['cyan', 'green', 'yellow', 'magenta']
    
    for style, color in zip(styles, colors):
        banner = generate_text("TEST", style=style, color=color)
        print(f"\n✨ Style: {style.upper()} | Color: {color.upper()}")
        animate_fade_in(banner, line_delay=0.05)


def example_4_status_messages():
    """Example 4: Status messages with animations"""
    print("\n" + "="*70)
    print("Example 4: Status Messages with Animations")
    print("="*70)
    
    statuses = [
        ("LOADING", "cyan"),
        ("SUCCESS", "green"),
        ("WARNING", "yellow"),
        ("ERROR", "red"),
    ]
    
    for text, color in statuses:
        banner = generate_text(text, style="mini", color=color)
        print(f"\n{color.upper()}:")
        animate_typewriter(banner, delay=0.02)


def example_5_custom_animations():
    """Example 5: Custom animation combinations"""
    print("\n" + "="*70)
    print("Example 5: Custom Animation Combinations")
    print("="*70)
    
    # Spinner + banner
    print("\n1️⃣  Spinner followed by banner:")
    animate_spinner_loading("Generating ASCII art", duration=1.0, color="cyan")
    banner = generate_text("READY", style="block", color="green")
    print(banner)
    
    # Typewriter + shape
    print("\n2️⃣  Typewriter text with shape:")
    animate_typewriter("✅ Operation successful!", delay=0.05, color="green")
    
    # Fade in multiple lines
    print("\n3️⃣  Multi-section fade in:")
    header = generate_text("REPORT", style="minimal", color="cyan")
    animate_fade_in(header, line_delay=0.1)
    
    items = [
        "✓ Tests passed: 245/245",
        "✓ Coverage: 98.5%",
        "✓ Performance: OK",
    ]
    for item in items:
        animate_typewriter(item, delay=0.03, color="green")


def example_6_demo_menu():
    """Example 6: Interactive demo menu"""
    print("\n" + "="*70)
    print("Example 6: Interactive Demo Menu")
    print("="*70)
    
    try:
        import questionary
        
        print("\nChoose an example to run:")
        choice = questionary.select(
            "Select demo:",
            choices=[
                "1. Simple Interactive Banner",
                "2. All Animations",
                "3. Styled Banners",
                "4. Status Messages",
                "5. Custom Combinations",
                "6. Exit"
            ]
        ).ask()
        
        demos = {
            "1. Simple Interactive Banner": example_1_simple_interactive,
            "2. All Animations": example_2_animations,
            "3. Styled Banners": example_3_styled_banners,
            "4. Status Messages": example_4_status_messages,
            "5. Custom Combinations": example_5_custom_animations,
        }
        
        if choice and choice in demos:
            demos[choice]()
    
    except ImportError:
        print("questionary not available, running all examples...")
        example_1_simple_interactive()
        example_2_animations()
        example_3_styled_banners()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Interactive Banner Examples")
    parser.add_argument("--example", type=int, choices=[1, 2, 3, 4, 5, 6],
                        help="Run specific example")
    parser.add_argument("--text", default="HELLO",
                        help="Custom text for banner")
    parser.add_argument("--interactive", action="store_true",
                        help="Run interactive mode")
    
    args = parser.parse_args()
    
    examples = {
        1: example_1_simple_interactive,
        2: example_2_animations,
        3: example_3_styled_banners,
        4: example_4_status_messages,
        5: example_5_custom_animations,
        6: example_6_demo_menu,
    }
    
    if args.interactive or args.example is None:
        example_6_demo_menu()
    elif args.example in examples:
        examples[args.example]()
    else:
        print("Running all examples...")
        for func in examples.values():
            func()
