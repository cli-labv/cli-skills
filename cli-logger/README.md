# CLI Logger 📝

Beautiful logging for Python CLI applications.

A custom logger with colored output, emoji icons, file logging, and timer utilities.

## Installation

```bash
pip install rich
```

## Quick Start

```python
from skills.cli_logger import info, success, error, warning

info("Starting application")
success("Connected to database")
warning("Cache is disabled")
error("Failed to load config")
```

Output:
```
14:32:15 ℹ️  INF [app] Starting application
14:32:15 ✅ OK  [app] Connected to database
14:32:16 ⚠️  WRN [app] Cache is disabled
14:32:16 ❌ ERR [app] Failed to load config
```

## Features

### Log Levels

```python
from skills.cli_logger import Logger, LogLevel

log = Logger("myapp", level=LogLevel.DEBUG)

log.trace("Very detailed info")    # 🔍 TRC
log.debug("Debug information")      # 🐛 DBG
log.info("General information")     # ℹ️  INF
log.success("Operation succeeded")  # ✅ OK
log.warning("Something to note")    # ⚠️  WRN
log.error("Something went wrong")   # ❌ ERR
log.critical("System failure")      # 🚨 CRT
```

### Extra Data

```python
log.info("User logged in", user="alice", ip="192.168.1.1")
# 14:32:15 ℹ️  INF [myapp] User logged in user=alice ip=192.168.1.1

log.error("Query failed", table="users", duration="5.2s")
```

### Timed Operations

```python
with log.timer("Database migration"):
    migrate_database()

# Output:
# ✅ OK  [myapp] Database migration (2.34s)
```

### File Logging

```python
log = Logger(
    "myapp",
    level=LogLevel.INFO,
    file="logs/app.log",
    file_level=LogLevel.DEBUG,  # Log more to file
)
```

### Configuration

```python
log = Logger(
    name="myapp",
    level=LogLevel.INFO,
    show_time=True,
    show_level=True,
    show_name=True,
    show_icons=True,
    time_format="%H:%M:%S",
)
```

### Sections and Rules

```python
log.section("Configuration")
log.info("Loading config.json")

log.rule("Database Setup")
log.info("Connecting to PostgreSQL")
```

### Global Logger

```python
from skills.cli_logger import configure, info, success

# Configure once at startup
configure("myapp", level=LogLevel.DEBUG)

# Use anywhere
info("Application started")
success("Ready!")
```

## API Reference

### Logger Class

```python
Logger(
    name: str = "app",
    level: LogLevel = LogLevel.INFO,
    show_time: bool = True,
    show_level: bool = True,
    show_name: bool = True,
    show_icons: bool = True,
    time_format: str = "%H:%M:%S",
    file: str = None,
    file_level: LogLevel = None,
)
```

### Methods

| Method | Description |
|--------|-------------|
| `trace(msg, **kwargs)` | Log trace message |
| `debug(msg, **kwargs)` | Log debug message |
| `info(msg, **kwargs)` | Log info message |
| `success(msg, **kwargs)` | Log success message |
| `warning(msg, **kwargs)` | Log warning message |
| `error(msg, **kwargs)` | Log error message |
| `critical(msg, **kwargs)` | Log critical message |
| `timer(msg)` | Context manager for timing |
| `rule(title)` | Print horizontal rule |
| `section(title)` | Print section header |

### Log Levels

| Level | Value | Icon | Use |
|-------|-------|------|-----|
| TRACE | 5 | 🔍 | Very detailed debugging |
| DEBUG | 10 | 🐛 | Debug information |
| INFO | 20 | ℹ️ | General information |
| SUCCESS | 25 | ✅ | Successful operations |
| WARNING | 30 | ⚠️ | Warnings |
| ERROR | 40 | ❌ | Errors |
| CRITICAL | 50 | 🚨 | Critical failures |

## License

MIT
