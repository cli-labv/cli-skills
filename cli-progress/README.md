# CLI Progress ⏳

Beautiful progress indicators for Python CLI applications.

A wrapper around [rich.progress](https://rich.readthedocs.io/en/latest/progress.html) providing spinners, progress bars, and task tracking with a simple API.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Spinners](#spinners)
- [Progress Bars](#progress-bars)
- [Track Iterables](#track-iterables)
- [Multiple Tasks](#multiple-tasks)
- [Utilities](#utilities)
- [API Reference](#api-reference)

## Installation

```bash
pip install rich
```

## Quick Start

```python
from skills.cli_progress import spinner, track

# Spinner for indeterminate operations
with spinner("Loading..."):
    do_something_slow()

# Progress bar for iterables
for item in track(items, "Processing"):
    process(item)
```

## Spinners

For operations with unknown duration:

```python
from skills.cli_progress import spinner, Spinner

# Simple spinner
with spinner("Connecting..."):
    connect_to_server()

# With success/failure messages
with spinner("Downloading...", success_message="Done!"):
    download_file()

# Update message during operation
with spinner("Starting...") as s:
    s.update("Connecting to database...")
    connect()
    s.update("Loading config...")
    load()
    s.succeed("Ready!")

# Manual control
s = Spinner("Working...")
s.start()
try:
    do_work()
    s.succeed("Complete!")
except Exception:
    s.fail("Failed!")
```

### Spinner Styles

```python
# Available styles
with spinner("Loading...", style="dots"):    # ⠋⠙⠹⠸⠼⠴
with spinner("Loading...", style="line"):    # -\|/
with spinner("Loading...", style="moon"):    # 🌑🌒🌓🌔
with spinner("Loading...", style="clock"):   # 🕐🕑🕒...
with spinner("Loading...", style="earth"):   # 🌍🌎🌏
with spinner("Loading...", style="hearts"):  # 💛💙💜💚
```

### Spinner Colors

```python
with spinner("Loading...", color="cyan"):
with spinner("Loading...", color="green"):
with spinner("Loading...", color="yellow"):
with spinner("Loading...", color="red"):
```

## Progress Bars

For operations with known total:

```python
from skills.cli_progress import progress, ProgressBar

# Context manager
with progress(100, "Installing") as pb:
    for i in range(100):
        install_package(i)
        pb.advance()

# Update description
with progress(len(files), "Processing") as pb:
    for f in files:
        pb.update(description=f"Processing {f}")
        process(f)
        pb.advance()

# Manual control
pb = ProgressBar(total=100, description="Loading")
pb.start()
for i in range(100):
    pb.advance()
pb.stop()
```

## Track Iterables

The easiest way to show progress:

```python
from skills.cli_progress import track, track_download

# Basic tracking
for item in track(items, "Processing"):
    process(item)

# With list comprehension
results = [process(x) for x in track(data, "Computing")]

# Download progress (shows speed and size)
for chunk in track_download(response.iter_content(), total=file_size):
    file.write(chunk)

# Transient (removes bar when done)
for x in track(items, "Quick task", transient=True):
    process(x)
```

## Multiple Tasks

Track multiple operations simultaneously:

```python
from skills.cli_progress import TaskGroup

with TaskGroup() as group:
    # Add tasks
    download = group.add_task("Downloading", total=100)
    process = group.add_task("Processing", total=100)
    
    for i in range(100):
        # Download step
        group.advance(download)
        
        # Process every other item
        if i % 2 == 0:
            group.advance(process, 2)
```

## Utilities

### Countdown Timer

```python
from skills.cli_progress import countdown

countdown(5, "Deploying in {remaining}s...")
deploy()

# With completion message
countdown(3, "Starting in {remaining}...", on_complete="Go!")
```

### Status Context

```python
from skills.cli_progress import status

with status("Connecting..."):
    connect()
```

## API Reference

### Spinner

| Method | Description |
|--------|-------------|
| `start()` | Start the spinner |
| `stop(success=True)` | Stop the spinner |
| `update(message)` | Update spinner text |
| `succeed(message)` | Stop with success |
| `fail(message)` | Stop with failure |

### ProgressBar

| Method | Description |
|--------|-------------|
| `start()` | Start the progress bar |
| `stop()` | Stop the progress bar |
| `advance(amount=1)` | Increment progress |
| `update(completed, description, total)` | Update state |

### Functions

| Function | Description |
|----------|-------------|
| `spinner(message, style, color)` | Context manager for spinners |
| `progress(total, description)` | Context manager for progress bars |
| `track(iterable, description)` | Progress iterator |
| `track_download(iterable, total)` | Download progress iterator |
| `countdown(seconds, message)` | Countdown timer |
| `status(message)` | Simple status spinner |

### TaskGroup

| Method | Description |
|--------|-------------|
| `add_task(description, total)` | Add a task, returns task name |
| `advance(task_name, amount)` | Advance a task |
| `update(task_name, **kwargs)` | Update a task |

## Examples

See the `examples/` folder:

- `01_basic_progress.py` - Spinners and progress bars
- `02_multiple_tasks.py` - Concurrent task tracking
- `03_spinner_styles.py` - All spinner animations

## Dependencies

- **rich** - Rich text and progress library

## License

MIT
