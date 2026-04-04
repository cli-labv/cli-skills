# CLI Errors ❌

Beautiful error messages for Python CLI applications.

## Installation

```bash
pip install rich
```

## Quick Start

```python
from skills.cli_errors import CLIError, print_error, exit_error

# Simple error
print_error("Something went wrong")

# With hint and suggestion
print_error(
    "Config file not found",
    hint="Create config.json in current directory",
    suggestion="Run 'myapp init' to generate one"
)

# Exit with error
exit_error("Fatal error", code=1)
```

## Features

### CLIError Exception

```python
from skills.cli_errors import CLIError

raise CLIError(
    "Database connection failed",
    hint="Check if PostgreSQL is running",
    suggestion="Run 'docker-compose up -d'"
)
```

### Error Handler

```python
from skills.cli_errors import ErrorHandler

handler = ErrorHandler(app_name="myapp", show_traceback=True)

try:
    risky_operation()
except Exception as e:
    handler.handle(e)  # Prints and exits
```

### Output Example

```
╭─────────────────────── Error ───────────────────────╮
│                                                      │
│ Database connection failed                           │
│                                                      │
│ 💡 Hint: Check if PostgreSQL is running             │
│                                                      │
│ 📝 Suggestion: Run 'docker-compose up -d'           │
│                                                      │
╰──────────────────────────────────────────────────────╯
```

## License

MIT
