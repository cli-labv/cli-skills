#!/usr/bin/env python3
"""
Example 4: Real-world Examples

Practical examples matching common CLI tasks.
"""

import time
from skills.cli_progress import progress, track, spinner, track_download


def simulate_download(total_bytes=1024*1024):
    """Simulate file download with chunks."""
    chunk_size = 8192
    chunks = []
    bytes_transferred = 0
    
    while bytes_transferred < total_bytes:
        chunk = min(chunk_size, total_bytes - bytes_transferred)
        chunks.append(chunk)
        bytes_transferred += chunk
    
    return chunks


def main():
    print("\n" + "=" * 60)
    print("  Real-world Examples")
    print("=" * 60)
    
    # 1. Processing files
    print("\n1️⃣  Batch Processing Files")
    print("-" * 60)
    
    files = [f"document_{i}.pdf" for i in range(1, 21)]
    
    for filename in track(files, "Converting PDFs to images"):
        # Simulate conversion
        time.sleep(0.1)
    
    print()
    
    # 2. Database operations
    print("2️⃣  Database Operations")
    print("-" * 60)
    
    def process_records():
        """Process database records."""
        total_records = 5000
        
        with progress(
            total_records,
            "Processing database records",
            spinner="dots_jumping"
        ) as bar:
            for record_id in range(total_records):
                # Simulate DB operation
                if record_id % 50 == 0:
                    bar.text(f"Processing record {record_id + 1}/{total_records}")
                bar()
                time.sleep(0.0001)  # Simulate quick operation
    
    process_records()
    print()
    
    # 3. Network requests
    print("3️⃣  API Requests")
    print("-" * 60)
    
    endpoints = [
        "/api/users",
        "/api/posts",
        "/api/comments",
        "/api/likes",
        "/api/shares",
        "/api/followers",
        "/api/trends",
        "/api/search",
    ]
    
    with progress(
        len(endpoints),
        "Fetching data from API",
        spinner="arrow"
    ) as bar:
        for endpoint in endpoints:
            bar.text(f"Requesting {endpoint}")
            time.sleep(0.3)  # Simulate network delay
            bar()
    
    print()
    
    # 4. Download simulation
    print("4️⃣  File Download")
    print("-" * 60)
    
    total_size = 10 * 1024 * 1024  # 10 MB
    chunks = simulate_download(total_size)
    
    bytes_downloaded = 0
    with progress(
        total_size,
        "Downloading large_file.zip",
        spinner="circle"
    ) as bar:
        for chunk_size in chunks:
            bar(chunk_size)
            bytes_downloaded += chunk_size
            time.sleep(0.001)
    
    print()
    
    # 5. Batch operations with retry logic
    print("5️⃣  Batch Operation with Retries")
    print("-" * 60)
    
    items = range(1, 31)
    failed_items = [5, 15, 22]  # Simulate failures
    
    with progress(len(items), "Processing items", spinner="bounce") as bar:
        for item in items:
            if item in failed_items:
                bar.text(f"Retrying item {item}...")
                time.sleep(0.3)
            bar()
            time.sleep(0.05)
    
    print()
    
    # 6. Complex workflow
    print("6️⃣  Complex Workflow")
    print("-" * 60)
    
    with spinner("Starting complex workflow...", style="earth") as bar:
        time.sleep(1)
        bar.text("Phase 1: Data extraction")
        time.sleep(1)
    
    print()
    
    print("Processing data in phases:")
    
    for phase in range(1, 4):
        with progress(
            100,
            f"Phase {phase}: Processing",
            spinner="dots_waves"
        ) as bar:
            for i in range(100):
                bar()
                time.sleep(0.01)
    
    print()
    
    # 7. Finally, cleanup
    with spinner("Finalizing...", style="clock") as bar:
        time.sleep(1)
        bar.text("Writing results to disk...")
        time.sleep(1)
    
    print("\n" + "=" * 60)
    print("✅ All real-world examples complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
    except Exception as e:
        print(f"Error: {e}")
        print("Install with: pip install alive-progress")
