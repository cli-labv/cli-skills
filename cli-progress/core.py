"""
Core implementation of CLI Progress.

Progress indicators using rich.progress.
"""

from __future__ import annotations

import time
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Iterator, List, Optional, Sequence

try:
    from rich.console import Console
    from rich.progress import (
        Progress,
        SpinnerColumn,
        TextColumn,
        BarColumn,
        TaskProgressColumn,
        TimeRemainingColumn,
        DownloadColumn,
        TransferSpeedColumn,
    )
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


# Spinner styles
SPINNERS = {
    "dots": "dots",
    "line": "line",
    "circle": "circle",
    "arc": "arc",
    "bounce": "bouncingBall",
    "clock": "clock",
    "moon": "moon",
    "runner": "runner",
}


@contextmanager
def spinner(message: str = "Loading...", style: str = "dots"):
    """
    Context manager for spinner.
    
    Example:
        >>> with spinner("Processing..."):
        ...     do_work()
    """
    if not HAS_RICH:
        print(f"{message}")
        yield
        return
    
    spinner_name = SPINNERS.get(style, style)
    
    with Progress(
        SpinnerColumn(spinner_name),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        progress.add_task(message, total=None)
        yield


@contextmanager
def progress(
    total: int,
    description: str = "Processing",
    show_speed: bool = False,
):
    """
    Context manager for progress bar.
    
    Example:
        >>> with progress(100, "Downloading") as update:
        ...     for i in range(100):
        ...         update(1)
    """
    if not HAS_RICH:
        print(f"{description}: 0/{total}")
        current = [0]
        def update(n: int = 1):
            current[0] += n
            print(f"\r{description}: {current[0]}/{total}", end="")
        yield update
        print()
        return
    
    columns = [
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
    ]
    
    if show_speed:
        columns.append(TransferSpeedColumn())
    
    columns.append(TimeRemainingColumn())
    
    with Progress(*columns, console=console) as prog:
        task = prog.add_task(description, total=total)
        
        def update(n: int = 1):
            prog.update(task, advance=n)
        
        yield update


def track(
    sequence: Sequence[Any],
    description: str = "Processing",
) -> Iterator[Any]:
    """
    Track progress over a sequence.
    
    Example:
        >>> for item in track(items, "Loading"):
        ...     process(item)
    """
    if not HAS_RICH:
        total = len(sequence)
        for i, item in enumerate(sequence):
            print(f"\r{description}: {i+1}/{total}", end="")
            yield item
        print()
        return
    
    from rich.progress import track as rich_track
    yield from rich_track(sequence, description=description, console=console)


def track_download(
    sequence: Sequence[Any],
    total_bytes: int,
    description: str = "Downloading",
) -> Iterator[Any]:
    """Track download progress."""
    if not HAS_RICH:
        yield from sequence
        return
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as prog:
        task = prog.add_task(description, total=total_bytes)
        
        for chunk in sequence:
            prog.update(task, advance=len(chunk))
            yield chunk


def countdown(seconds: int, message: str = "Starting in"):
    """Show countdown timer."""
    if HAS_RICH:
        for i in range(seconds, 0, -1):
            console.print(f"\r{message} {i}...", end="")
            time.sleep(1)
        console.print()
    else:
        for i in range(seconds, 0, -1):
            print(f"\r{message} {i}...", end="")
            time.sleep(1)
        print()


class TaskGroup:
    """
    Group of parallel tasks.
    
    Example:
        >>> group = TaskGroup("Downloads")
        >>> t1 = group.add_task("File 1", total=100)
        >>> t2 = group.add_task("File 2", total=50)
        >>> 
        >>> with group.run():
        ...     group.update(t1, 50)
        ...     group.update(t2, 25)
    """
    
    def __init__(self, title: str = "Tasks"):
        if not HAS_RICH:
            raise ImportError("rich required: pip install rich")
        
        self.title = title
        self._progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console,
        )
        self._tasks = {}
    
    def add_task(self, description: str, total: int) -> int:
        """Add a task, returns task ID."""
        task_id = self._progress.add_task(description, total=total)
        self._tasks[task_id] = description
        return task_id
    
    def update(self, task_id: int, advance: int = 1) -> None:
        """Update task progress."""
        self._progress.update(task_id, advance=advance)
    
    @contextmanager
    def run(self):
        """Start tracking tasks."""
        with self._progress:
            yield


if __name__ == "__main__":
    print("CLI Progress Demo")
    print("=" * 40)
    
    # Spinner
    print("\n1. Spinner:")
    with spinner("Processing..."):
        time.sleep(2)
    
    # Progress bar
    print("\n2. Progress bar:")
    with progress(100, "Downloading") as update:
        for _ in range(100):
            update(1)
            time.sleep(0.02)
    
    # Track
    print("\n3. Track:")
    for item in track(range(50), "Items"):
        time.sleep(0.02)
    
    print("\n✅ Demo complete!")
