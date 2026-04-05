#!/usr/bin/env python3
"""
Example 1: Basic Progress Indicators

Demonstrates spinners and simple progress bars using alive-progress.
"""

import time
from skills.cli_progress import spinner, progress, track


def main():
    print("\n" + "=" * 60)
    print("  Basic Progress Indicators - alive-progress Examples")
    print("=" * 60)
    
    # 1. Simple spinner
    print("\n1️⃣  Simple Spinner (indeterminate progress)")
    print("-" * 60)
    
    with spinner("Connecting to server...", style="dots"):
        time.sleep(2)
    
    print("✅ Connected!\n")
    
    # 2. Spinner with different style
    print("2️⃣  Spinner with custom style (dots_waves)")
    print("-" * 60)
    
    with spinner("Downloading updates...", style="dots_waves"):
        time.sleep(2)
    
    print("✅ Downloaded!\n")
    
    # 3. Spinner with text updates
    print("3️⃣  Spinner with live updates")
    print("-" * 60)
    
    with spinner("Processing...", style="earth") as bar:
        time.sleep(0.5)
        bar.text("Phase 1: Reading data...")
        time.sleep(1)
        bar.text("Phase 2: Analyzing...")
        time.sleep(1)
        bar.text("Phase 3: Writing results...")
        time.sleep(1)
    
    print("✅ Complete!\n")
    
    # 4. Progress bar (deterministic)
    print("4️⃣  Progress Bar (with known total)")
    print("-" * 60)
    
    with progress(100, "Installing packages", spinner="dots_jumping") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar()
    
    print()
    
    # 5. Track iterator (easiest!)
    print("5️⃣  Auto-tracking iterator (simplest way!)")
    print("-" * 60)
    
    items = list(range(50))
    for item in track(items, "Processing files"):
        time.sleep(0.05)
    
    print()
    
    # 6. Track with different spinner
    print("6️⃣  Track with emoji spinner")
    print("-" * 60)
    
    data = range(30)
    for value in track(data, "Computing values"):
        time.sleep(0.07)
    
    print("\n" + "=" * 60)
    print("✅ All demos complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Install with: pip install alive-progress")
