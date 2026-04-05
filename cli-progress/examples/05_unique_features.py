#!/usr/bin/env python3
"""
Example 5: Alive-progress Unique Features

Showcase unique capabilities of alive-progress that other libraries don't have.
"""

import time
from skills.cli_progress import progress, manual_progress, spinner


def main():
    print("\n" + "=" * 60)
    print("  Alive-progress Unique Features")
    print("=" * 60)
    
    # 1. Dynamic spinner speed (reacts to throughput)
    print("\n1️⃣  Dynamic Spinner Speed")
    print("-" * 60)
    print("Watch how the spinner REACTS to your processing speed!")
    print("It speeds up with fast operations and slows down with slow ones.\n")
    
    print("Fast operation (small delay):")
    with progress(100, "Fast task", spinner="dots") as bar:
        for i in range(100):
            bar()
            time.sleep(0.001)  # Very fast
    
    print("\nSlow operation (larger delay):")
    with progress(100, "Slow task", spinner="dots") as bar:
        for i in range(100):
            bar()
            time.sleep(0.05)  # Much slower
    
    print("\n✨ Notice how the spinner matched the speed!\n")
    
    # 2. Accurate ETA with Exponential Smoothing
    print("2️⃣  Accurate ETA Calculation")
    print("-" * 60)
    print("ETA is calculated using Exponential Smoothing Algorithm")
    print("It adapts when speed changes mid-process!\n")
    
    with progress(200, "Variable speed task") as bar:
        # Start fast
        print("  Phase 1: Fast processing...")
        for i in range(50):
            bar()
            time.sleep(0.005)
        
        # Transition
        print("  Phase 2: Hitting bottleneck...")
        time.sleep(1)
        
        # Slow down
        print("  Phase 3: Slow processing...")
        for i in range(150):
            bar()
            time.sleep(0.02)
    
    print("✨ Watch how ETA updates as speed changes!\n")
    
    # 3. Over/Underflow Detection
    print("3️⃣  Over/Underflow Detection")
    print("-" * 60)
    print("Bar shows visual indicators if you call bar() more/fewer times!\n")
    
    print("Perfect scenario (100 items, 100 calls):")
    with progress(100, "Perfect") as bar:
        for i in range(100):
            bar()
            time.sleep(0.005)
    
    print("\nOverflow scenario (100 items, 120 calls):")
    with progress(100, "Overflow") as bar:
        for i in range(120):
            bar()
            time.sleep(0.004)
    
    print("\n✨ Notice the ⚠️ warning indicator on overflow!\n")
    
    # 4. Manual mode for external progress reporting
    print("4️⃣  Manual Mode - Perfect for External APIs")
    print("-" * 60)
    print("When an external service reports %, set it directly:\n")
    
    def simulate_api_with_percentage():
        """Simulate an API that only gives percentage progress."""
        # Simulating an API that reports progress as percentage
        api_progress_updates = [
            0.0, 0.15, 0.30, 0.45, 0.60, 0.75, 0.85, 0.95, 1.0
        ]
        
        with manual_progress("API Request (external %)", spinner="circle") as bar:
            for percentage in api_progress_updates:
                print(f"  API reported: {percentage*100:.0f}%")
                bar(percentage)
                time.sleep(1)
    
    simulate_api_with_percentage()
    print()
    
    # 5. Print hooks (integrated print statements)
    print("5️⃣  Automatic Print Hooks")
    print("-" * 60)
    print("Normal print() calls integrate seamlessly!\n")
    
    with progress(50, "Processing with print statements") as bar:
        for i in range(50):
            if i % 10 == 0 and i > 0:
                print(f"  ✓ Processed {i} items")
            bar()
            time.sleep(0.03)
    
    print()
    
    # 6. Final receipt with statistics
    print("6️⃣  Final Receipt & Statistics")
    print("-" * 60)
    print("Alive-progress prints a nice summary when done!\n")
    
    with progress(150, "Task with statistics") as bar:
        for i in range(150):
            bar()
            time.sleep(0.02)
    
    print("\n✨ The bar above shows total items, elapsed time, and throughput!\n")
    
    # 7. Multiple modes comparison
    print("7️⃣  Mode Comparison")
    print("-" * 60)
    print("Alive-progress has different modes for different situations:\n")
    
    print("  A) AUTO mode (total provided):")
    print("     - Shows: percentage ✓, counter ✓, ETA ✓, rate ✓")
    with progress(50, "Auto mode example") as bar:
        for i in range(50):
            bar()
            time.sleep(0.01)
    
    print("\n  B) MANUAL mode (you set percentage):")
    print("     - Shows: percentage ✓, counter (from total), ETA ✓, rate ✓")
    with manual_progress("Manual mode example", spinner="dots") as bar:
        for pct in [0.25, 0.50, 0.75, 1.0]:
            bar(pct)
            time.sleep(1)
    
    print()
    
    print("\n" + "=" * 60)
    print("✅ All unique features demonstrated!")
    print("=" * 60)
    print("\nThese are features you don't get in other progress libraries! 🚀\n")


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Install with: pip install alive-progress")
