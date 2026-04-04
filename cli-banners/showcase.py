#!/usr/bin/env python3
"""
showcase.py - Full demonstration of CLI Banners skill
Shows all capabilities with visual examples
"""

import sys
import time
from pathlib import Path

# Import the skill
sys.path.insert(0, str(Path(__file__).parent / "python"))
from cli_banners import generate_text, generate_shape, Colors

def pause(seconds=1.2):
    """Pause for visual effect."""
    time.sleep(seconds)

def showcase():
    """Showcase all CLI banners capabilities."""
    
    # Intro
    print("\n" * 2)
    print("="*75)
    print(" " * 20 + "CLI BANNERS SKILL SHOWCASE")
    print("="*75)
    pause()
    
    # Section 1: Text Generation
    print("\n📝 TEXT GENERATION\n")
    pause()
    
    print("Block Style:")
    print(generate_text("HELLO", style="block", color="cyan"))
    pause()
    
    print("\nMinimal Style:")
    print(generate_text("WORLD", style="minimal", color="green"))
    pause()
    
    # Section 2: Shapes
    print("\n\n🎨 SHAPES & SYMBOLS\n")
    pause()
    
    print("Arrows:")
    arrow_r = generate_shape("arrow_right", style="block")
    arrow_l = generate_shape("arrow_left", style="block")
    arrow_u = generate_shape("arrow_up", style="block")
    arrow_d = generate_shape("arrow_down", style="block")
    print(f"  Right: {arrow_r}  Left: {arrow_l}  Up: {arrow_u}  Down: {arrow_d}")
    pause()
    
    print("\nStatus Symbols:")
    check_min = generate_shape("check", style="minimal")
    check_det = generate_shape("check", style="detailed", color="green")
    cross_min = generate_shape("cross", style="minimal")
    cross_det = generate_shape("cross", style="detailed", color="red")
    star = generate_shape("star", style="block", color="yellow")
    heart = generate_shape("heart", style="block", color="red")
    
    print(f"  Check (minimal): {check_min}")
    print(f"  Check (detailed): {check_det}")
    print(f"  Cross (minimal): {cross_min}")
    print(f"  Cross (detailed): {cross_det}")
    print(f"  Star: {star}")
    print(f"  Heart: {heart}")
    pause()
    
    # Section 3: Colors
    print("\n\n🌈 COLOR SUPPORT\n")
    pause()
    
    colors = [
        ("SUCCESS", "green"),
        ("WARNING", "yellow"),
        ("ERROR", "red"),
        ("INFO", "cyan"),
    ]
    
    for text, color in colors:
        banner = generate_text(text, style="minimal", color=color)
        print(banner)
        pause(0.5)
    
    # Section 4: Use Cases
    print("\n\n💼 PRACTICAL USE CASES\n")
    pause()
    
    print("1. Welcome Screen:")
    print("-" * 50)
    title = generate_text("MYAPP", style="block", color="cyan")
    print(title)
    star = generate_shape("star", style="block", color="yellow")
    print(f"{star} Version 2.0.0 - Production Ready\n")
    pause()
    
    print("2. Status Messages:")
    print("-" * 50)
    check = generate_shape("check", style="detailed", color="green")
    cross = generate_shape("cross", style="detailed", color="red")
    arrow = generate_shape("arrow_right", style="block", color="cyan")
    
    print(f"  {check} Build successful")
    print(f"  {check} Tests passed (127/127)")
    print(f"  {cross} Deployment failed")
    print(f"  {arrow} Retrying in 30 seconds...")
    pause()
    
    print("\n3. Interactive Menu:")
    print("-" * 50)
    menu_title = generate_text("MENU", style="minimal", color="cyan")
    print(menu_title)
    arrow = generate_shape("arrow_right", style="block")
    print(f"{arrow} Start Application")
    print(f"{arrow} View Settings")
    print(f"{arrow} Run Tests")
    print(f"{arrow} Exit")
    pause()
    
    print("\n4. Progress Indication:")
    print("-" * 50)
    loading_frames = [
        generate_shape("loading", style="minimal"),
        generate_shape("loading", style="block"),
        generate_shape("loading", style="detailed"),
    ]
    
    for i, frame in enumerate(loading_frames, 1):
        print(f"  {frame} Processing step {i}/3...")
        time.sleep(0.5)
    
    check = generate_shape("check", style="detailed", color="green")
    print(f"  {check} Complete!")
    pause()
    
    # Section 5: Comparison
    print("\n\n📊 BEFORE vs AFTER\n")
    pause()
    
    print(f"{Colors.RED}❌ BEFORE (manual ASCII):{Colors.RESET}")
    print("  _____ _____ ____ _____")
    print("    |   |     |      |")
    print("    |   |__   __|    |")
    print("    |   |       |    |")
    print("    |   |___  __|    |")
    print()
    
    print(f"{Colors.GREEN}✅ AFTER (cli-banners skill):{Colors.RESET}")
    print(generate_text("TEST", style="block", color="green"))
    pause()
    
    # Section 6: Features Summary
    print("\n\n⭐ FEATURES SUMMARY\n")
    pause()
    
    features = [
        ("No dependencies", "Works anywhere Python/Bash runs"),
        ("Two text styles", "block (bold) and minimal (clean)"),
        ("9+ shapes", "arrows, checks, stars, hearts, etc."),
        ("Full color support", "Standard and bright ANSI colors"),
        ("Easy integration", "Works with perfect-boxes and other skills"),
    ]
    
    check = generate_shape("check", style="detailed", color="green")
    for title, desc in features:
        print(f"  {check} {Colors.BOLD}{title}{Colors.RESET}")
        print(f"     {desc}")
        time.sleep(0.4)
    
    # Final
    print("\n")
    print("="*75)
    final = generate_text("READY", style="minimal", color="bright_green")
    print(final)
    print("="*75)
    print()
    print(f"  {Colors.CYAN}📚 Documentation:{Colors.RESET} skills/cli-banners/README.md")
    print(f"  {Colors.CYAN}📖 Quick Start:{Colors.RESET} skills/cli-banners/QUICKSTART.md")
    print(f"  {Colors.CYAN}📦 Examples:{Colors.RESET} skills/cli-banners/examples/")
    print()


if __name__ == "__main__":
    try:
        showcase()
    except KeyboardInterrupt:
        print("\n\n⚠️  Showcase interrupted\n")
        sys.exit(0)
