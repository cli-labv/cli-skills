#!/usr/bin/env python3
"""
Example 2: Multiple Tasks

Demonstrates managing multiple concurrent progress tasks.
"""

import time
import random
from skills.cli_progress import TaskGroup, spinner


def simulate_download(size: int = 100) -> int:
    """Simulate downloading chunks."""
    downloaded = 0
    while downloaded < size:
        chunk = random.randint(1, 10)
        downloaded = min(downloaded + chunk, size)
        yield chunk
        time.sleep(0.05)


def main():
    print("=" * 50)
    print("  Multiple Concurrent Tasks")
    print("=" * 50)
    print()
    
    # Simulate downloading and processing multiple files
    files = [
        {"name": "document.pdf", "size": 80},
        {"name": "image.png", "size": 120},
        {"name": "data.json", "size": 60},
    ]
    
    print("Downloading multiple files...")
    print()
    
    with TaskGroup() as group:
        # Add tasks for each file
        tasks = {}
        for f in files:
            task = group.add_task(f"📥 {f['name']}", total=f["size"])
            tasks[f["name"]] = {"task": task, "size": f["size"], "done": 0}
        
        # Simulate concurrent downloads
        all_done = False
        while not all_done:
            all_done = True
            for name, info in tasks.items():
                if info["done"] < info["size"]:
                    all_done = False
                    # Download random chunk
                    chunk = random.randint(1, 5)
                    chunk = min(chunk, info["size"] - info["done"])
                    info["done"] += chunk
                    group.advance(info["task"], chunk)
            time.sleep(0.05)
    
    print()
    print("✅ All downloads complete!")
    print()
    
    # Now process each file
    print("Processing downloaded files...")
    print()
    
    with TaskGroup() as group:
        for f in files:
            task = group.add_task(f"⚙️ Processing {f['name']}", total=100)
            for _ in range(100):
                group.advance(task)
                time.sleep(0.01)
    
    print()
    print("✅ All files processed!")


if __name__ == "__main__":
    try:
        main()
    except ImportError as e:
        print(f"Error: {e}")
        print("Install with: pip install rich")
