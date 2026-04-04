# CLI Updater 🔄

Version checking for Python CLI applications.

## Quick Start

```python
from skills.cli_updater import check_update, print_update_notice

# Quick check and notify
print_update_notice("myapp", "1.0.0")
```

## Features

### VersionChecker

```python
from skills.cli_updater import VersionChecker

checker = VersionChecker("myapp", "1.0.0")

# Check PyPI
update = checker.check_pypi()
if update.has_update:
    print(f"New version: {update.latest}")
    checker.print_notice(update)

# Check GitHub
update = checker.check_github("owner", "repo")
```

### Check Functions

```python
from skills.cli_updater import check_update, print_update_notice

# PyPI
update = check_update("myapp", "1.0.0")

# GitHub
update = check_update(
    "myapp", "1.0.0",
    source="github",
    owner="myuser",
    repo="myapp"
)

# Auto-print if update available
print_update_notice("myapp", "1.0.0")
```

### UpdateInfo

```python
update = check_update("myapp", "1.0.0")
print(update.current)    # "1.0.0"
print(update.latest)     # "1.2.0"
print(update.has_update) # True
print(update.install_cmd) # "pip install --upgrade myapp"
```

### Caching

Results are cached for 24 hours to avoid repeated API calls.

```python
# Disable cache
checker = VersionChecker("myapp", "1.0.0", use_cache=False)
```

### Output

```
╭─────────────── 🔄 Update Available ───────────────╮
│ Update available: 1.0.0 → 1.2.0                    │
│ Run: pip install --upgrade myapp                   │
╰────────────────────────────────────────────────────╯
```

## License

MIT
