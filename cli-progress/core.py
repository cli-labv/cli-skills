"""
Core implementation of CLI Progress.

Modern progress indicators using alive-progress with fallback to rich.
Provides spinners, progress bars, task tracking with dynamic animation and ETA.
"""

from __future__ import annotations

import time
from contextlib import contextmanager
from typing import Any, Iterator, Optional, Sequence, Callable

try:
    from alive_progress import alive_bar, alive_it, show_bars, show_spinners
    from alive_progress.styles import showtime, Show
    from alive_progress.animations import bouncing, scrolling, frames, sequential
    HAS_ALIVE = True
except ImportError:
    HAS_ALIVE = False

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


# Pre-defined spinner styles (alive-progress style names)
SPINNERS = {
    "dots": "dots",
    "dots_waves": "dots_waves",
    "dots_waves2": "dots_waves2",
    "dots_jumping": "dots_jumping",
    "dots_sawing": "dots_sawing",
    "line": "line",
    "line_waves": "line_waves",
    "circle": "circle",
    "circle_quarters": "circle_quarters",
    "arc": "arc",
    "arrow": "arrow",
    "bounce": "bouncing",
    "clock": "clock",
    "moon": "moon",
    "ruler": "ruler",
    "earth": "earth",
    "hearts": "hearts",
    "triangles": "triangles",
    "classic": "classic",
}


@contextmanager
def spinner(
    message: str = "Loading...",
    style: str = "dots",
    manual: bool = False,
    disable: bool = False,
):
    """
    Context manager for spinner - indeterminate progress.
    
    Uses alive-progress by default with rich fallback.
    The spinner dynamically reacts to actual processing speed!
    
    Args:
        message: Display message
        style: Spinner style (dots, dots_waves, circle, moon, etc.)
        manual: If True, don't print the final receipt
        disable: If True, don't show animation at all
    
    Example:
        >>> with spinner("Processing...") as bar:
        ...     do_work()
        ...     bar.text("Phase 1: Complete")
    """
    if disable:
        yield None
        return
    
    if HAS_ALIVE:
        spinner_name = SPINNERS.get(style, style)
        try:
            # alive_bar without total = unknown mode (indeterminate)
            # The spinner will dance based on your actual throughput!
            with alive_bar(
                manual=manual,
                title=message,
                spinner=spinner_name,
                receipt=not manual,
            ) as bar:
                yield bar
        except Exception:
            # Fallback if alive-progress fails
            if HAS_RICH:
                with Progress(
                    SpinnerColumn(SPINNERS.get(style, style)),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                    transient=not manual,
                ) as progress:
                    progress.add_task(message, total=None)
                    yield None
            else:
                print(f"{message}")
                yield None
    elif HAS_RICH:
        spinner_name = SPINNERS.get(style, style)
        with Progress(
            SpinnerColumn(spinner_name),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=not manual,
        ) as progress:
            progress.add_task(message, total=None)
            yield None
    else:
        print(f"{message}")
        yield None


@contextmanager
def progress(
    total: int,
    description: str = "Processing",
    show_speed: bool = True,
    manual: bool = False,
    spinner: str = "dots",
    calibrate: Optional[int] = None,
):
    """
    Context manager for deterministic progress bar.
    
    Uses alive-progress which includes:
    - Dynamic spinner reacting to throughput
    - Accurate ETA using Exponential Smoothing Algorithm
    - Over/underflow detection
    - Automatic print() and logging hooks
    
    Args:
        total: Total items to process
        description: Display message
        show_speed: Show current throughput (items/sec)
        manual: Manual mode - set percentage directly
        spinner: Spinner style to use
        calibrate: Calibrate animation speed (default: auto)
    
    Example:
        >>> with progress(100, "Downloading") as bar:
        ...     for i in range(100):
        ...         process_item(i)
        ...         bar()  # increment
        
        >>> with progress(100, description="Manual", manual=True) as bar:
        ...     bar(0.5)  # set to 50%
    """
    if not total:
        total = 1
    
    if HAS_ALIVE:
        try:
            spinner_style = SPINNERS.get(spinner, spinner)
            with alive_bar(
                total=total,
                title=description,
                manual=manual,
                spinner=spinner_style,
                calibrate=calibrate,
                force_tty=None,  # auto-detect
            ) as bar:
                yield bar
            return
        except Exception:
            pass  # Fallback to rich
    
    # Fallback to rich
    if HAS_RICH:
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
    else:
        print(f"{description}: 0/{total}")
        current = [0]
        def update(n: int = 1):
            current[0] += n
            print(f"\r{description}: {current[0]}/{total}", end="", flush=True)
        yield update
        print()


@contextmanager
def manual_progress(
    description: str = "Processing",
    spinner: str = "dots",
    calibrate: Optional[int] = None,
):
    """
    Manual mode - YOU set the percentage directly.
    
    Useful when you have percentage feedback instead of item counts.
    Perfect for monitoring external processes that only report progress %.
    
    Args:
        description: Display message
        spinner: Spinner style
        calibrate: Animation speed calibration
    
    Example:
        >>> with manual_progress("Installing") as bar:
        ...     bar(0.25)  # 25%
        ...     bar(0.50)  # 50%
        ...     bar(1.0)   # 100%
    """
    if HAS_ALIVE:
        try:
            spinner_style = SPINNERS.get(spinner, spinner)
            with alive_bar(
                manual=True,
                title=description,
                spinner=spinner_style,
                calibrate=calibrate,
            ) as bar:
                yield bar
            return
        except Exception:
            pass
    
    # Rich doesn't have manual percentage mode easily
    if HAS_RICH:
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
        ) as prog:
            task = prog.add_task(description, total=100)
            
            def update_percent(percent: float):
                """percent should be 0.0 to 1.0"""
                completed = int(percent * 100)
                prog.update(task, completed=completed)
            
            yield update_percent
    else:
        print(f"{description}: 0%")
        def update_percent(percent: float):
            print(f"\r{description}: {percent*100:.0f}%", end="", flush=True)
        yield update_percent
        print()


def track(
    sequence: Sequence[Any],
    description: str = "Processing",
    transient: bool = False,
) -> Iterator[Any]:
    """
    Auto-tracking iterator - the easiest way to show progress!
    
    Uses alive-progress alive_it() which:
    - Automatically counts items
    - Shows accurate ETA
    - Requires no manual bar() calls
    
    Args:
        sequence: Iterable to process
        description: Display message
        transient: If True, remove bar when complete
    
    Example:
        >>> for item in track(items, "Processing"):
        ...     process(item)
    """
    if HAS_ALIVE:
        try:
            # alive_it auto-infers total from sequence
            for item in alive_it(
                sequence,
                title=description,
                disable=(not transient),
            ):
                yield item
            return
        except Exception:
            pass  # Fallback to rich
    
    # Fallback to rich or manual
    if HAS_RICH:
        from rich.progress import track as rich_track
        yield from rich_track(sequence, description=description, console=console)
    else:
        total = len(sequence) if hasattr(sequence, '__len__') else 0
        for i, item in enumerate(sequence):
            if total:
                print(f"\r{description}: {i+1}/{total}", end="", flush=True)
            yield item
        if total:
            print()


def track_download(
    sequence: Sequence[Any],
    total_bytes: int,
    description: str = "Downloading",
) -> Iterator[Any]:
    """
    Track download progress with speed and size information.
    
    Args:
        sequence: Iterator yielding chunks
        total_bytes: Total bytes to download
        description: Display message
    
    Example:
        >>> for chunk in track_download(response.iter_content(), 1024*1024):
        ...     file.write(chunk)
    """
    if HAS_ALIVE:
        try:
            # Convert bytes to human-readable format
            with alive_bar(total_bytes, title=description) as bar:
                for chunk in sequence:
                    bar(len(chunk))
                    yield chunk
            return
        except Exception:
            pass
    
    # Fallback to rich
    if HAS_RICH:
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
    else:
        for chunk in sequence:
            yield chunk


def countdown(
    seconds: int,
    message: str = "Starting in {remaining}s",
    on_complete: str = "Go!",
):
    """
    Countdown timer - counts down from N seconds.
    
    Args:
        seconds: Number of seconds to countdown
        message: Message template (use {remaining} for countdown)
        on_complete: Message when done
    
    Example:
        >>> countdown(5, "Deploying in {remaining}s...")
        >>> countdown(3, on_complete="Starting!")
    """
    for i in range(seconds, 0, -1):
        msg = message.format(remaining=i)
        print(f"\r{msg}", end="", flush=True)
        time.sleep(1)
    print(f"\r{on_complete}", flush=True)


class TaskGroup:
    """
    Group of parallel tasks for simultaneous tracking.
    
    Perfect for monitoring multiple operations at once.
    Uses alive-progress multi-task capabilities.
    
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
        if not HAS_ALIVE and not HAS_RICH:
            raise ImportError("Install alive-progress or rich: pip install alive-progress")
        
        self.title = title
        self._use_alive = HAS_ALIVE
        
        if self._use_alive:
            try:
                self._progress = None
                self._bar = None
                self._tasks = {}
            except Exception:
                self._use_alive = False
        
        if not self._use_alive:
            self._progress = Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                TimeRemainingColumn(),
                console=console,
            )
            self._tasks = {}
    
    def add_task(self, description: str, total: int) -> str:
        """Add a task, returns task ID."""
        task_id = description.lower().replace(" ", "_")
        
        if self._use_alive:
            # Store task info for later use with alive_bar
            self._tasks[task_id] = {"description": description, "total": total}
        else:
            # Rich mode
            task_id = self._progress.add_task(description, total=total)
            self._tasks[task_id] = {"description": description, "total": total}
        
        return task_id
    
    def update(self, task_id: str, advance: int = 1) -> None:
        """Update task progress."""
        if not self._use_alive:
            self._progress.update(task_id, advance=advance)
    
    @contextmanager
    def run(self):
        """Start tracking tasks."""
        if self._use_alive:
            # For alive-progress: we'll use multiple progress calls
            # This is a limitation - alive-progress doesn't support multiple bars
            # We show the first task
            if self._tasks:
                first_task = list(self._tasks.values())[0]
                with alive_bar(
                    first_task["total"],
                    title=f"{self.title}: {first_task['description']}",
                ) as bar:
                    self._bar = bar
                    yield
        else:
            # Rich mode
            with self._progress:
                yield


# Utility functions for alive-progress features

def show_all_spinners(pattern: Optional[str] = None, length: int = 40, fps: int = 15):
    """
    Display all available spinner animations.
    
    Great for choosing which spinner style you like!
    
    Args:
        pattern: Filter spinners (e.g., 'dots', 'wave', 'scroll')
        length: Bar length to display
        fps: Frames per second for animation
    
    Example:
        >>> show_all_spinners()
        >>> show_all_spinners(pattern='wave')
    """
    if HAS_ALIVE:
        from alive_progress.styles import showtime, Show
        try:
            showtime(Show.SPINNERS, pattern=pattern, length=length, fps=fps)
        except Exception as e:
            print(f"Could not show spinners: {e}")
    else:
        print("Install alive-progress to see spinner showcase: pip install alive-progress")


def show_all_bars(pattern: Optional[str] = None, length: int = 40, fps: int = 15):
    """Display all available bar animations."""
    if HAS_ALIVE:
        from alive_progress.styles import showtime, Show
        try:
            showtime(Show.BARS, pattern=pattern, length=length, fps=fps)
        except Exception as e:
            print(f"Could not show bars: {e}")
    else:
        print("Install alive-progress to see bar showcase: pip install alive-progress")


def show_all_themes(pattern: Optional[str] = None, length: int = 40, fps: int = 15):
    """Display all available themes (spinner + bar combinations)."""
    if HAS_ALIVE:
        from alive_progress.styles import showtime, Show
        try:
            showtime(Show.THEMES, pattern=pattern, length=length, fps=fps)
        except Exception as e:
            print(f"Could not show themes: {e}")
    else:
        print("Install alive-progress to see theme showcase: pip install alive-progress")


if __name__ == "__main__":
    print("CLI Progress Demo")
    print("=" * 50)
    
    # Demo 1: Spinner
    print("\n1️⃣  Spinner (indeterminate progress):")
    with spinner("Processing...", style="dots"):
        time.sleep(2)
    
    # Demo 2: Progress bar
    print("\n2️⃣  Progress bar (deterministic):")
    with progress(100, "Downloading", spinner="dots") as bar:
        for _ in range(100):
            bar()
            time.sleep(0.01)
    
    # Demo 3: Track iterator
    print("\n3️⃣  Auto-tracking iterator:")
    for item in track(range(50), "Processing items"):
        time.sleep(0.02)
    
    # Demo 4: Manual mode
    print("\n4️⃣  Manual mode (set percentage directly):")
    with manual_progress("Installing packages") as bar:
        for pct in [0.25, 0.50, 0.75, 1.0]:
            bar(pct)
            time.sleep(0.5)
    
    # Demo 5: Countdown
    print("\n5️⃣  Countdown timer:")
    countdown(3, "Starting in {remaining}s", "Ready!")
    
    print("\n✅ Demo complete!")
