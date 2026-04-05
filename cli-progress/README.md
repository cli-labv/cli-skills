# CLI Progress ⏳

Modern progress indicators for Python CLI applications, powered by **alive-progress**.

This skill provides beautiful spinners, progress bars, and task tracking with a simple, Pythonic API. The primary library is **alive-progress**, which offers:

- 🎯 **Dynamic spinners** that react to your actual processing speed
- ⏱️ **Accurate ETA** with Exponential Smoothing Algorithm
- 📊 **Multiple bar styles** and theme combinations
- 🎨 **Highly customizable** animations and appearances
- 🪝 **Auto hooks** for print() and logging integration
- ⏸️ **Pause mechanism** to pause/resume processing
- 📱 **Multi-mode operation** (auto, unknown, manual percentage)

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Spinners](#spinners)
- [Progress Bars](#progress-bars)
- [Auto-Tracking Iterators](#auto-tracking-iterators)
- [Manual Mode (Percentage)](#manual-mode-percentage)
- [Download Progress](#download-progress)
- [Multiple Tasks](#multiple-tasks)
- [Utilities](#utilities)
- [Advanced Features](#advanced-features)
- [API Reference](#api-reference)

## Installation

```bash
pip install alive-progress
# Optional fallback:
pip install rich
```

The skill uses `alive-progress` by default with automatic fallback to `rich` if needed.

## Quick Start

```python
from skills.cli_progress import spinner, progress, track

# 1. Spinner - for indeterminate tasks
with spinner("Loading..."):
    long_operation()

# 2. Progress bar - for known totals
with progress(100, "Downloading") as bar:
    for item in items:
        bar()  # increment counter

# 3. Auto-tracking iterator - simplest!
for item in track(items, "Processing"):
    process(item)
```

## Spinners

For operations with unknown duration. The spinner dynamically reacts to your actual processing speed!

```python
from skills.cli_progress import spinner

# Simple spinner
with spinner("Connecting..."):
    connect_to_server()

# With custom style
with spinner("Loading...", style="dots_waves"):
    load_data()

# With custom spinner and update text during operation
with spinner("Starting...", style="earth") as bar:
    bar.text("Phase 1: Connecting...")
    connect()
    bar.text("Phase 2: Loading...")
    load()
```

### Available Spinner Styles

Common styles:
- **dots** - Animated dots (⠋⠙⠹⠸⠼⠴)
- **dots_waves** - Dotted wave animation
- **dots_waves2** - Alternative dotted waves
- **dots_jumping** - Bouncing dots
- **dots_sawing** - Sawtooth wave
- **line** - Line spinner (-\|/)
- **line_waves** - Animated line waves
- **circle** - Rotating circle (◡⊙◠)
- **circle_quarters** - Quarter circles
- **arc** - Arc spinner
- **arrow** - Arrow spinner
- **bounce** / **bouncing** - Bouncing animation
- **clock** - Clock animation (🕐🕑🕒...)
- **moon** - Moon phases (🌑🌒🌓🌔)
- **ruler** - Ruler animation
- **earth** - Rotating earth (🌍🌎🌏)
- **hearts** - Heart animation (💛💙💜💚)
- **triangles** - Triangle animation
- **classic** - Classic minimal spinner

See all available spinners:

```python
from skills.cli_progress import show_all_spinners

show_all_spinners()
show_all_spinners(pattern='wave')  # Filter by pattern
```

## Progress Bars

For operations with a known total. The bar shows percentage, ETA, and throughput.

```python
from skills.cli_progress import progress

# Basic usage
with progress(100, "Processing") as bar:
    for i in range(100):
        process_item(i)
        bar()  # increment by 1

# With custom increments
with progress(len(files), "Downloading") as bar:
    for file in files:
        size = download(file)
        bar(size)  # increment by size

# With custom spinner style
with progress(
    1000,
    "Computing",
    spinner="dots_jumping",
    show_speed=True,
) as bar:
    for _ in range(1000):
        compute()
        bar()

# Calibrate animation speed if it feels too slow/fast
with progress(500, "Processing", calibrate=250) as bar:
    for item in items:
        bar()
```

### Features

- ✅ **Accurate ETA** - Uses exponential smoothing algorithm
- ✅ **Throughput tracking** - Items per second
- ✅ **Over/underflow detection** - Shows if you're ahead/behind
- ✅ **Over/underflow detection** - Shows if you're ahead/behind
- ✅ **Auto print hooks** - Seamlessly integrate print() calls
- ✅ **Auto logging hooks** - Integrate with Python logging

## Auto-Tracking Iterators

The easiest way to track progress! No manual bar() calls needed.

```python
from skills.cli_progress import track

# Just wrap your iterable
for item in track(items, "Processing"):
    process(item)

# Works with any iterable
for line in track(open("file.txt"), "Reading"):
    parse(line)

# With list comprehension
results = [process(x) for x in track(data, "Computing")]

# Transient mode (removes bar when done)
for item in track(items, "Quick task", transient=True):
    do_quick_work(item)
```

The tracker automatically:
- Infers total from sequence length
- Shows accurate ETA
- Shows throughput
- Requires no manual calls

## Manual Mode (Percentage)

When you only have percentage feedback (not item count):

```python
from skills.cli_progress import manual_progress

# Set percentage directly (0.0 to 1.0)
with manual_progress("Installing packages") as bar:
    bar(0.25)  # 25%
    bar(0.50)  # 50%
    bar(0.75)  # 75%
    bar(1.0)   # 100% - Complete!

# Perfect for monitoring external processes
def monitor_external_process():
    with manual_progress("Building Docker image") as bar:
        process = start_docker_build()
        while process.running:
            progress = get_progress_from_stderr(process)
            bar(progress)  # progress is 0.0-1.0
```

## Download Progress

Track file downloads with speed and size information:

```python
from skills.cli_progress import track_download

# Download with progress
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open('file.bin', 'wb') as f:
    for chunk in track_download(
        response.iter_content(chunk_size=8192),
        total_size,
        "Downloading file"
    ):
        f.write(chunk)
```

Shows:
- Progress bar
- Downloaded size
- Download speed
- Estimated time remaining

## Multiple Tasks

Track multiple operations (with limitations in alive-progress):

```python
from skills.cli_progress import TaskGroup

group = TaskGroup("Batch Operations")
task1 = group.add_task("Download", total=100)
task2 = group.add_task("Process", total=100)

with group.run():
    for i in range(100):
        group.update(task1, 1)
        process()
        group.update(task2, 1)
```

Note: For multiple simultaneous bars, alive-progress is still working on this feature (most requested). Currently shows the primary task.

## Utilities

### Countdown Timer

```python
from skills.cli_progress import countdown

# Simple countdown
countdown(5, "Deploying in {remaining}s...")

# With completion message
countdown(3, "Server restart in {remaining}...", on_complete="Ready!")

# Custom message
countdown(10, "Resume in {remaining} seconds")
```

### View All Animations

```python
from skills.cli_progress import show_all_spinners, show_all_bars, show_all_themes

# Show all spinner styles
show_all_spinners()

# Show all bar styles
show_all_bars()

# Show all theme combinations
show_all_themes()

# Filter by pattern
show_all_spinners(pattern='wave')
show_all_bars(pattern='block')
```

## Advanced Features

### Pause Mechanism

*This feature is unique to alive-progress!*

Pause progress, handle items manually, then resume:

```python
def reconcile_transactions():
    with progress(qs.count()) as bar:
        for transaction in qs:
            if faulty(transaction):
                with bar.pause():
                    yield transaction  # Back to prompt!
            bar()

# In your REPL
gen = reconcile_transactions()
tx = next(gen, None)  # Process pauses at fault
# Inspect and fix the transaction manually
next(gen, None)  # Resume
```

### Over/Underflow Detection

```python
with progress(100, "Items") as bar:
    for _ in range(100):
        bar()  # 100% - perfect
    
    # But if we call bar() more times...
    bar(10)  # Will show as ⚠️ overflow indicator!
```

### Manual Increments

```python
with progress(total=1000) as bar:
    bar()      # Increment by 1
    bar(5)     # Increment by 5
    bar(0)     # Don't increment (show current state)
    bar(-3)    # Decrement by 3 (rare but possible)
```

### Access Current State

```python
with progress(100) as bar:
    for i in range(100):
        bar()
        if i % 10 == 0:
            # Get current information
            print(f"Monitor: {bar.monitor}")
            print(f"ETA: {bar.eta}")
            print(f"Rate: {bar.rate}")
            print(f"Elapsed: {bar.elapsed}s")
```

### FPS Calibration

If the spinner feels too slow/fast, adjust the calibration:

```python
with progress(
    10000,
    "Heavy computation",
    calibrate=5000  # Expects 5000 items/sec as baseline
) as bar:
    for item in process_heavy():
        bar()
```

## API Reference

### Functions

| Function | Description |
|----------|-------------|
| `spinner(message, style, manual, disable)` | Context manager for spinners |
| `progress(total, description, show_speed, manual, spinner, calibrate)` | Context manager for progress bars |
| `manual_progress(description, spinner, calibrate)` | Context manager for percentage-based progress |
| `track(sequence, description, transient)` | Auto-tracking iterator |
| `track_download(sequence, total_bytes, description)` | Download progress iterator |
| `countdown(seconds, message, on_complete)` | Countdown timer |
| `show_all_spinners(pattern, length, fps)` | Display all spinner styles |
| `show_all_bars(pattern, length, fps)` | Display all bar styles |
| `show_all_themes(pattern, length, fps)` | Display all theme combinations |

### Spinner/Progress Context Manager Methods

```python
with progress(100) as bar:
    bar()                    # Increment counter by 1
    bar(5)                   # Increment counter by 5
    bar.text("Phase 1")      # Update status text
    bar.title = "New Title"  # Update title
    value = bar.current      # Get current counter/percentage
    monitor = bar.monitor    # Get formatted monitor widget
    eta = bar.eta            # Get formatted ETA widget
    rate = bar.rate          # Get formatted rate widget
    elapsed = bar.elapsed    # Get elapsed time in seconds
    receipt = bar.receipt    # Get final receipt data
```

### TaskGroup

| Method | Description |
|--------|-------------|
| `add_task(description, total)` | Add a task, returns task ID |
| `update(task_id, advance)` | Advance a task |
| `run()` | Context manager to start tracking |

## Examples

See the `examples/` folder for complete examples:

- `01_basic_progress.py` - Spinners and progress bars
- `02_manual_mode.py` - Percentage-based progress
- `03_spinner_showcase.py` - All spinner animations
- `04_download_example.py` - Download progress tracking
- `05_pause_mechanism.py` - Pausing and resuming (requires alive-progress)

## Dependencies

- **alive-progress** (primary) - Modern progress bars with dynamic animations
- **rich** (optional fallback) - Beautiful terminal formatting

## Key Differences from Rich

| Feature | alive-progress | rich |
|---------|---|---|
| Dynamic spinner speed | ✅ Reacts to throughput | ❌ Static speed |
| ETA accuracy | ✅ Exponential smoothing | ⚠️ Simple estimation |
| Pause/Resume | ✅ Unique feature! | ❌ Not available |
| Print hooks | ✅ Auto-integrated | ⚠️ Manual setup |
| Manual percentage | ✅ Full support | ⚠️ Complex setup |
| Multiple bars | ⏳ In development | ✅ Supported |

## Tips for Best Results

1. **Install alive-progress**: `pip install alive-progress` for full features
2. **Choose appropriate spinner**: Different spinners feel different - experiment!
3. **Use track()** for simplicity when possible
4. **Calibrate if needed**: If animation feels off, use `calibrate` parameter
5. **Force TTY in notebooks**: Use `force_tty=True` in Jupyter
6. **Check over/underflow**: If your progress looks wrong, check bar() calls

## License

MIT
