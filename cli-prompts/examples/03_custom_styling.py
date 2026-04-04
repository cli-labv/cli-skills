#!/usr/bin/env python3
"""
Example 3: Custom Styling

Demonstrates how to customize the look of prompts:
- Custom color schemes
- Different styles for different contexts
"""

from skills.cli_prompts import (
    confirm,
    text,
    select,
    checkbox,
    PromptStyle,
    set_default_style,
    PromptAbortedError,
)


# Define custom styles
DARK_STYLE = PromptStyle(
    question_mark="#FF6B6B bold",   # Red
    question="bold",
    answer="#4ECDC4 bold",          # Teal
    pointer="#FF6B6B bold",         # Red
    highlighted="#FF6B6B",          # Red
    selected="#4ECDC4",             # Teal
    instruction="#888888",
    separator="#888888",
)

MINIMAL_STYLE = PromptStyle(
    question_mark="#888888",
    question="",
    answer="#FFFFFF bold",
    pointer="#FFFFFF",
    highlighted="#CCCCCC",
    selected="#FFFFFF",
    instruction="#666666",
    separator="#666666",
)

VIBRANT_STYLE = PromptStyle(
    question_mark="#FF00FF bold",   # Magenta
    question="bold",
    answer="#00FF00 bold",          # Bright green
    pointer="#FF00FF bold",         # Magenta
    highlighted="#FFFF00",          # Yellow
    selected="#00FF00",             # Bright green
    instruction="#00FFFF",          # Cyan
    separator="#FF00FF",            # Magenta
)


def demo_with_style(style: PromptStyle, style_name: str):
    """Run a demo with a specific style."""
    print(f"\n{'=' * 50}")
    print(f"  {style_name} Style")
    print(f"{'=' * 50}\n")
    
    # Using style parameter directly
    name = text(
        "What's your name?",
        default="User",
        style=style,
    )
    
    lang = select(
        "Preferred language:",
        choices=["Python", "JavaScript", "Go", "Rust"],
        style=style,
    )
    
    features = checkbox(
        "Select options:",
        choices=["Option A", "Option B", "Option C"],
        style=style,
    )
    
    confirm_result = confirm(
        "Confirm selection?",
        style=style,
    )
    
    print(f"\n  Results: {name}, {lang}, {features}, confirmed={confirm_result}")


def main():
    """Run styling demo."""
    print("=" * 50)
    print("  Custom Styling Demo")
    print("=" * 50)
    
    try:
        # Let user choose a style
        style_choice = select(
            "Select a style to preview:",
            choices=[
                {"name": "🌙 Dark Theme", "value": "dark"},
                {"name": "⚪ Minimal Theme", "value": "minimal"},
                {"name": "🌈 Vibrant Theme", "value": "vibrant"},
                {"name": "📋 All Themes", "value": "all"},
            ],
        )
        
        styles = {
            "dark": (DARK_STYLE, "Dark"),
            "minimal": (MINIMAL_STYLE, "Minimal"),
            "vibrant": (VIBRANT_STYLE, "Vibrant"),
        }
        
        if style_choice == "all":
            for style, name in styles.values():
                demo_with_style(style, name)
        else:
            style, name = styles[style_choice]
            demo_with_style(style, name)
        
        # You can also set a default style for all prompts
        print("\n" + "=" * 50)
        print("  Setting Default Style")
        print("=" * 50)
        
        if confirm("Set Dark theme as default for all prompts?"):
            set_default_style(DARK_STYLE)
            print("  ✅ Dark theme is now the default")
            
            # These will use the new default
            text("This uses the new default style:")
    
    except PromptAbortedError:
        print("\n\n  Aborted by user (Ctrl+C)")
    
    except ImportError as e:
        print(f"\n  Error: {e}")
        print("  Install dependencies: pip install questionary")


if __name__ == "__main__":
    main()
