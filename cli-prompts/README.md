# CLI Prompts 💬

Beautiful interactive command-line prompts for Python applications.

A professional wrapper around [questionary](https://github.com/tmbo/questionary) with enhanced defaults, consistent styling, and easy-to-use API.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Prompt Types](#prompt-types)
- [Validation](#validation)
- [Custom Styling](#custom-styling)
- [Error Handling](#error-handling)
- [API Reference](#api-reference)

## Installation

```bash
pip install questionary rich
```

## Quick Start

```python
from skills.cli_prompts import confirm, text, select, checkbox

# Simple confirmation
if confirm("Do you want to continue?"):
    
    # Text input
    name = text("What's your name?")
    
    # Single selection
    color = select("Pick a color:", ["red", "green", "blue"])
    
    # Multi selection
    features = checkbox("Select features:", ["auth", "api", "docs"])
    
    print(f"Hello {name}! You chose {color} and {features}")
```

## Prompt Types

### confirm() - Yes/No Questions

```python
from skills.cli_prompts import confirm

# Basic
proceed = confirm("Continue?")

# With default
delete = confirm("Delete all files?", default=False)

# Output:
# ? Continue? (Y/n)
```

### text() - Text Input

```python
from skills.cli_prompts import text

# Basic
name = text("Your name:")

# With default
name = text("Your name:", default="Anonymous")

# With validation
email = text(
    "Email:",
    validate=lambda x: "@" in x or "Invalid email"
)

# Multiline (Alt+Enter to submit)
description = text("Description:", multiline=True)
```

### password() - Hidden Input

```python
from skills.cli_prompts import password

# Basic
secret = password("API Key:")

# With validation
pwd = password(
    "Password:",
    validate=lambda x: len(x) >= 8 or "Min 8 characters"
)
```

### select() - Single Selection

```python
from skills.cli_prompts import select

# Simple list
color = select("Color:", ["red", "green", "blue"])

# With descriptions
env = select("Environment:", [
    {"name": "Development (local)", "value": "dev"},
    {"name": "Staging (testing)", "value": "staging"},
    {"name": "Production (live)", "value": "prod"},
])

# With shortcuts (press 1, 2, 3...)
option = select("Choose:", ["A", "B", "C"], use_shortcuts=True)
```

### checkbox() - Multiple Selection

```python
from skills.cli_prompts import checkbox

# Basic
features = checkbox("Features:", ["auth", "api", "docs"])

# With pre-selected
features = checkbox(
    "Features:",
    ["auth", "api", "docs", "tests"],
    default=["auth", "docs"]
)

# With validation
features = checkbox(
    "Select at least 2:",
    ["A", "B", "C", "D"],
    validate=lambda x: len(x) >= 2 or "Select at least 2"
)
```

### path() - File/Directory Paths

```python
from skills.cli_prompts import path

# Any path
file = path("Select file:")

# Directories only
folder = path("Output folder:", only_directories=True)

# With default
config = path("Config file:", default="./config.json")
```

### autocomplete() - Text with Suggestions

```python
from skills.cli_prompts import autocomplete

countries = ["USA", "UK", "Canada", "Mexico", "Brazil"]

country = autocomplete(
    "Country:",
    choices=countries,
    match_middle=True  # Match anywhere, not just start
)
```

## Validation

All prompts support validation functions:

```python
from skills.cli_prompts import text

# Return True for valid, or error message string
def validate_email(value):
    if "@" not in value:
        return "Must contain @"
    if "." not in value:
        return "Must contain a domain"
    return True

email = text("Email:", validate=validate_email)

# Or use lambda for simple cases
age = text(
    "Age:",
    validate=lambda x: x.isdigit() or "Must be a number"
)
```

## Custom Styling

Create custom color themes:

```python
from skills.cli_prompts import (
    PromptStyle,
    set_default_style,
    confirm,
)

# Define custom style
my_style = PromptStyle(
    question_mark="#FF6B6B bold",  # Red
    question="bold",
    answer="#4ECDC4 bold",         # Teal
    pointer="#FF6B6B bold",
    highlighted="#FF6B6B",
    selected="#4ECDC4",
    instruction="#888888",
    separator="#888888",
)

# Use for single prompt
confirm("Continue?", style=my_style)

# Or set as default for all prompts
set_default_style(my_style)
confirm("This uses the new default")
```

## Error Handling

Handle user cancellation (Ctrl+C):

```python
from skills.cli_prompts import confirm, PromptAbortedError

try:
    result = confirm("Continue?")
    print(f"User chose: {result}")
except PromptAbortedError:
    print("User cancelled")
```

## API Reference

### Main Functions

| Function | Description | Returns |
|----------|-------------|---------|
| `confirm(message, default=False)` | Yes/No question | `bool` |
| `text(message, default="")` | Text input | `str` |
| `password(message)` | Hidden input | `str` |
| `select(message, choices)` | Single selection | `str` |
| `checkbox(message, choices)` | Multiple selection | `List[str]` |
| `path(message, only_directories=False)` | Path input | `str` |
| `autocomplete(message, choices)` | Text with suggestions | `str` |

### Utility Functions

| Function | Description |
|----------|-------------|
| `pause(message)` | Wait for Enter key |
| `clear()` | Clear terminal screen |

### Aliases (Simpler Names)

| Alias | Equivalent |
|-------|------------|
| `yes_no()` | `confirm()` |
| `ask()` | `text()` |
| `choose()` | `select()` |
| `multi_choose()` | `checkbox()` |

## Examples

See the `examples/` folder for complete working examples:

- `01_basic_prompts.py` - Fundamental prompt types
- `02_advanced_selection.py` - Checkbox, autocomplete, paths
- `03_custom_styling.py` - Custom color themes

## Dependencies

- **questionary** - Core prompt library
- **rich** (optional) - Enhanced console output

## License

MIT
