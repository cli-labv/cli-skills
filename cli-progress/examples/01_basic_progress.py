#!/usr/bin/env python3
"""
Example 1: Basic Progress Indicators

Demonstrates spinners and simple progress bars.
"""

import time
from skills.cli_progress import spinner, progress, track


def main():
    print("=" * 50)
    print("  Basic Progress Indicators")
    print("=" * 50)
    print()
    
    # 1. Simple spinner
    print("1. Simple Spinner")
    print("-" * 40)
    
    with spinner("Connecting to server..."):
        time.sleep(2)
    
    print()
    
    # 2. Spinner with success message
    print("2. Spinner with completion message")
    print("-" * 40)
    
    with spinner(
        "Downloading updates...",
        success_message="Updates downloaded successfully!"
    ):
        time.sleep(2)
    
    print()
    
    # 3. Spinner with update
    print("3. Spinner with status updates")
    print("-" * 40)
    
    with spinner("Starting process...") as s:
        time.sleep(1)
        s.update("Connecting to database...")
        time.sleep(1)
        s.update("Loading configuration...")
        time.sleep(1)
        s.update("Almost done...")
        time.sleep(1)
        s.succeed("Process completed!")
    
    print()
    
    # 4. Progress bar with context manager
    print("4. Progress Bar")
    print("-" * 40)
    
    with progress(100, "Installing packages") as pb:
        for i in range(100):
            time.sleep(0.03)
            pb.advance()
    
    print()
    
    # 5. Track iterator
    print("5. Track Iterator")
    print("-" * 40)
    
    items = list(range(50))
    for item in track(items, "Processing files"):
        time.sleep(0.05)
    
    print()
    print("✅ Demo complete!")


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Install with: pip install rich")
