#!/usr/bin/env python3
"""
Example 3: Spinner Showcase

Display all available spinner styles to help you choose!
"""

import time
from skills.cli_progress import show_all_spinners, show_all_bars, show_all_themes, SPINNERS, spinner


def main():
    print("\n" + "=" * 60)
    print("  Spinner & Bar Showcase")
    print("=" * 60)
    
    # 1. Show all spinners interactively
    print("\n1️⃣  All available spinners")
    print("-" * 60)
    print("View all spinner animations to find your favorite!\n")
    
    try:
        show_all_spinners()
    except Exception as e:
        print(f"Could not display spinners: {e}")
        print("Make sure alive-progress is installed: pip install alive-progress")
    
    # 2. Show all bars
    print("\n2️⃣  All available bar styles")
    print("-" * 60)
    
    try:
        show_all_bars()
    except Exception:
        print("Bars showcase not available")
    
    # 3. Show all themes
    print("\n3️⃣  All available themes (spinner + bar combinations)")
    print("-" * 60)
    
    try:
        show_all_themes()
    except Exception:
        print("Themes showcase not available")
    
    # 4. Quick demo of some popular spinners
    print("\n4️⃣  Quick demo of popular spinners")
    print("-" * 60)
    
    popular_spinners = [
        ("dots", "Classic dots spinner"),
        ("dots_waves", "Dotted wave effect"),
        ("moon", "Moon phases 🌑🌒🌓🌔"),
        ("earth", "Rotating earth 🌍🌎🌏"),
        ("hearts", "Beating hearts 💛💙💜💚"),
        ("bounce", "Bouncing animation"),
        ("circle_quarters", "Rotating circle quarters"),
    ]
    
    for spinner_name, description in popular_spinners:
        if spinner_name in SPINNERS or spinner_name == "bounce":
            print(f"\n▶ {description}")
            with spinner(f"  {spinner_name} spinner...", style=spinner_name):
                time.sleep(2)
    
    print("\n" + "=" * 60)
    print("✅ Showcase complete!")
    print("=" * 60)
    print("\nTip: Use these spinner names in your code:")
    print("  with progress(100, 'Task', spinner='dots_waves') as bar:")
    print("      bar()")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
    except Exception as e:
        print(f"Error: {e}")
        print("Install with: pip install alive-progress")
