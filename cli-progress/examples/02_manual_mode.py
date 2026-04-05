#!/usr/bin/env python3
"""
Example 2: Manual Mode & Advanced Features

Demonstrates percentage-based progress and advanced features.
"""

import time
from skills.cli_progress import manual_progress, progress, countdown


def main():
    print("\n" + "=" * 60)
    print("  Advanced Features - Manual Mode & More")
    print("=" * 60)
    
    # 1. Manual percentage mode
    print("\n1️⃣  Manual Mode (set percentage directly)")
    print("-" * 60)
    print("Useful when you only have % feedback, not item count\n")
    
    with manual_progress("Installing", spinner="dots") as bar:
        for percentage in [0.0, 0.25, 0.50, 0.75, 1.0]:
            bar(percentage)
            time.sleep(1)
    
    print("✅ Installation complete!\n")
    
    # 2. Manual mode with slower feedback
    print("2️⃣  Manual Mode with smooth updates")
    print("-" * 60)
    
    with manual_progress("Building Docker image", spinner="moon") as bar:
        steps = [0.1, 0.3, 0.5, 0.7, 0.85, 1.0]
        for step in steps:
            bar(step)
            time.sleep(1.5)
    
    print("✅ Build complete!\n")
    
    # 3. Progress with custom ETA
    print("3️⃣  Progress bar with variable throughput")
    print("-" * 60)
    print("Notice how ETA adjusts based on actual speed!\n")
    
    with progress(200, "Variable load task", spinner="bounce") as bar:
        # First half: fast
        for i in range(100):
            bar()
            time.sleep(0.01)  # Fast
        
        # Second half: slow
        for i in range(100):
            bar()
            time.sleep(0.03)  # Slower
    
    print()
    
    # 4. Manual mode with real-world example
    print("4️⃣  Real-world: Database migration")
    print("-" * 60)
    
    def simulate_db_migration():
        """Simulate a database migration with stages."""
        stages = [
            ("Planning", 0.1),
            ("Creating tables", 0.3),
            ("Inserting data", 0.7),
            ("Building indexes", 0.9),
            ("Validating", 1.0),
        ]
        
        with manual_progress("Database Migration", spinner="circle_quarters") as bar:
            for stage_name, percentage in stages:
                print(f"\n  → {stage_name}...")
                bar(percentage)
                time.sleep(1.5)
    
    simulate_db_migration()
    
    print("\n✅ Migration complete!\n")
    
    # 5. Countdown timer
    print("5️⃣  Countdown Timer")
    print("-" * 60)
    
    countdown(5, "Deployment starting in {remaining}s", "🚀 Deploying!")
    
    print("\n" + "=" * 60)
    print("✅ All advanced demos complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Install with: pip install alive-progress")
