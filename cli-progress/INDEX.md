# CLI Progress Skill - Complete Index

## 📋 Overview

Modern progress indicators powered by **alive-progress** with automatic fallback to **rich**.

**Version:** 3.0.0
**Status:** ✅ Production Ready
**Library:** alive-progress (primary) + rich (fallback)

## 📁 File Structure

```
cli-progress/
├── README.md              # Main documentation (500+ lines)
├── INDEX.md              # This file
├── UPGRADE_NOTES.md      # What's new in 3.0
├── __init__.py           # Module exports
├── core.py               # Core implementation (alive-progress)
└── examples/
    ├── 01_basic_progress.py       # Basic spinners and progress
    ├── 02_manual_mode.py          # Manual mode and advanced
    ├── 02_spinner_showcase.py     # Animation gallery
    ├── 03_real_world.py           # Real-world examples
    └── 05_unique_features.py      # Unique alive-progress features
```

## 🎯 Quick API Reference

### Core Functions

```python
# Indeterminate progress
with spinner(message, style="dots", manual=False) as bar:
    long_operation()
    bar.text("Update message")

# Deterministic progress
with progress(total, description, spinner="dots", calibrate=None) as bar:
    for item in items:
        bar()  # Increment by 1

# Manual percentage mode (NEW!)
with manual_progress(description, spinner="dots") as bar:
    bar(0.25)  # Set to 25%
    bar(0.75)  # Set to 75%

# Auto-tracking iterator (easiest!)
for item in track(sequence, description, transient=False):
    process(item)

# Download progress
for chunk in track_download(sequence, total_bytes, description):
    save(chunk)

# Countdown timer
countdown(seconds, message="Starting in {remaining}s", on_complete="Go!")

# Visualization (NEW!)
show_all_spinners(pattern=None, length=40, fps=15)
show_all_bars(pattern=None, length=40, fps=15)
show_all_themes(pattern=None, length=40, fps=15)
```

### TaskGroup (Multi-task)

```python
group = TaskGroup("Operations")
task1 = group.add_task("Download", total=100)
task2 = group.add_task("Process", total=50)

with group.run():
    group.update(task1, 50)
    group.update(task2, 25)
```

## 🎨 Spinner Styles (20+)

### Simple
- `dots` - ⠋⠙⠹⠸⠼⠴
- `line` - -\|/
- `classic` - |/-\

### Wave Effects
- `dots_waves` - Dotted waves
- `dots_waves2` - Alternative waves
- `line_waves` - Line waves

### Bouncing
- `dots_jumping` - Jumping dots
- `dots_sawing` - Sawtooth
- `bounce` / `bouncing` - Bouncing animation
- `circle_quarters` - Quarter circles

### Animated Characters
- `circle` - ◡⊙◠
- `arc` - ◜◠◝
- `arrow` - Arrow spinner
- `ruler` - Ruler animation

### Emoji (🎉)
- `clock` - 🕐🕑🕒... (clock faces)
- `moon` - 🌑🌒🌓🌔 (moon phases)
- `earth` - 🌍🌎🌏 (rotating earth)
- `hearts` - 💛💙💜💚 (beating hearts)
- `triangles` - Triangle animation

**See all:** `show_all_spinners()`

## 📊 Parameters Explained

### spinner()

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | str | "Loading..." | Display message |
| `style` | str | "dots" | Spinner style name |
| `manual` | bool | False | Don't print receipt |
| `disable` | bool | False | Disable animation |

### progress()

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `total` | int | - | Total items to process |
| `description` | str | "Processing" | Display message |
| `show_speed` | bool | True | Show items/sec throughput |
| `manual` | bool | False | Set percentage manually |
| `spinner` | str | "dots" | Spinner style |
| `calibrate` | int | None | Animation speed (items/s) |

### track()

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `sequence` | iterable | - | Items to iterate |
| `description` | str | "Processing" | Display message |
| `transient` | bool | False | Remove bar when done |

### manual_progress()

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `description` | str | "Processing" | Display message |
| `spinner` | str | "dots" | Spinner style |
| `calibrate` | int | None | Animation speed |

## 💡 Usage Patterns

### Pattern 1: Simple Spinner (Unknown Duration)

```python
from skills.cli_progress import spinner

with spinner("Processing..."):
    long_operation()
```

### Pattern 2: Known Total (Best Performance)

```python
from skills.cli_progress import progress

with progress(len(items), "Processing") as bar:
    for item in items:
        process(item)
        bar()
```

### Pattern 3: Auto-Track (Simplest)

```python
from skills.cli_progress import track

for item in track(items, "Processing"):
    process(item)
```

### Pattern 4: External API Reporting %

```python
from skills.cli_progress import manual_progress

with manual_progress("API Request") as bar:
    api = ExternalAPI()
    while api.running:
        bar(api.progress)  # 0.0 to 1.0
```

### Pattern 5: Complex Workflow

```python
from skills.cli_progress import progress, spinner

with spinner("Initializing..."):
    initialize()

for phase in range(1, 4):
    with progress(100, f"Phase {phase}") as bar:
        for i in range(100):
            process()
            bar()

with spinner("Finalizing...", style="moon") as bar:
    finalize()
    bar.text("Writing results...")
```

### Pattern 6: Real-time Updates

```python
with progress(100, "Task") as bar:
    for i in range(100):
        if i % 10 == 0:
            print(f"Status: {i} items done")
        bar()
```

## 🔄 Main Changes from v2.0 → v3.0

| Feature | v2.0 (rich) | v3.0 (alive-progress) |
|---------|---|---|
| Spinner speed | Fixed | ✅ Dynamic (reacts to throughput) |
| ETA accuracy | Simple | ✅ Exponential Smoothing |
| Manual mode | ❌ | ✅ New |
| Over/underflow | ❌ | ✅ Visual indicators |
| Multiple bars | ✅ | ⏳ Limited |
| Pause/Resume | ❌ | ✅ Unique! |
| Print hooks | Manual | ✅ Auto |
| Styles | 8 | ✅ 20+ |

## 🚀 Performance Tips

1. **Use `track()` when possible** - Simplest and most reliable
2. **Provide `total` when known** - Enables accurate ETA
3. **Use `manual=True` for slow operations** - Avoids overhead
4. **Calibrate for very fast/slow ops** - `calibrate=10000` for 10k items/s
5. **Use `transient=True` for temporary bars** - Cleaner output

## 📚 Example Usage

### Example 1: Download with Progress

```python
from skills.cli_progress import track_download
import requests

response = requests.get(url, stream=True)
size = int(response.headers.get('content-length', 0))

with open('file.zip', 'wb') as f:
    for chunk in track_download(
        response.iter_content(8192),
        size,
        "Downloading"
    ):
        f.write(chunk)
```

### Example 2: Database Processing

```python
from skills.cli_progress import progress

with progress(10000, "Processing records") as bar:
    for record in fetch_records():
        process(record)
        bar()  # Increment
        
        if processed % 1000 == 0:
            bar.text(f"Processed {processed} records")
```

### Example 3: Multi-step Workflow

```python
from skills.cli_progress import progress, countdown

# Step 1
with progress(100, "Download") as bar:
    for item in items:
        download(item)
        bar()

# Step 2
with progress(100, "Process") as bar:
    for item in items:
        process(item)
        bar()

# Countdown before next action
countdown(5, "Starting deployment in {remaining}s")
```

## 🎓 For AI Agents

When using this skill in your projects:

1. **Explore**: Read README.md and examples
2. **Choose pattern**: Pick the right one for your use case
3. **Generate code**: Write your own progress tracking
4. **Delete skill**: `rm -rf skills/cli-progress/` before commit
5. **Push**: Upload only your code, not the skill

Example agent usage:

```python
# From skill (learn)
from skills.cli_progress import track, progress, show_all_spinners

# See options
show_all_spinners()

# Generate YOUR code
for item in track(my_items, "Processing"):
    my_process(item)
```

## 📖 Documentation Files

- **README.md** (500+ lines)
  - Complete feature documentation
  - All API methods explained
  - Tips and best practices
  
- **UPGRADE_NOTES.md**
  - What's new in 3.0
  - Migration guide
  - Before/after examples

- **examples/**
  - 01_basic_progress.py - Start here
  - 02_manual_mode.py - Advanced usage
  - 02_spinner_showcase.py - See all spinners
  - 03_real_world.py - Real cases
  - 05_unique_features.py - Special features

## ⚙️ Installation

```bash
# Primary library
pip install alive-progress

# Optional fallback
pip install rich
```

## ✅ Testing

```bash
# Run any example
python examples/01_basic_progress.py
python examples/02_spinner_showcase.py
python examples/03_real_world.py

# Test import
python -c "from skills.cli_progress import progress, track; print('✅ OK')"
```

## 🔗 References

- **alive-progress GitHub**: https://github.com/rsalmei/alive-progress
- **Documentation**: In README.md (complete)
- **Features**: Dynamic spinners, accurate ETA, pause mechanism, manual mode

## 📞 Support

For issues or questions:
1. Check README.md
2. Run examples to see expected behavior
3. Read UPGRADE_NOTES.md for new features
4. Review code examples for patterns

---

**Last Updated:** 2024
**Status:** ✅ Production Ready - Fully Tested
