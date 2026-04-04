# CLI Help 📖

Beautiful help panels for Python CLI applications.

## Installation

```bash
pip install rich
```

## Quick Start

```python
from skills.cli_help import HelpPanel

help = HelpPanel("myapp", "1.0.0", "My awesome CLI")
help.add_command("init", "Initialize project", "[name]")
help.add_command("build", "Build project")
help.add_example("myapp init my-project")
help.print()
```

## Features

### HelpPanel Class

```python
from skills.cli_help import HelpPanel

help = HelpPanel(
    name="myapp",
    version="2.0.0",
    description="A modern CLI tool"
)

# Add commands
help.add_command("init", "Initialize", "[name]")
help.add_command("build", "Build", "[--prod]")

# Add examples
help.add_example("myapp init my-project")
help.add_example("myapp build --prod", "Production build")

help.print()
```

### Quick Functions

```python
from skills.cli_help import print_help, print_usage, print_examples

# Quick help
print_help(
    name="myapp",
    version="1.0.0",
    commands={"init": "Initialize", "build": "Build"},
    examples=["myapp init my-project"]
)

# Just usage
print_usage("myapp", "[command] [options]")

# Just examples
print_examples(["myapp init", "myapp build"])
```

### Output

```
╭────────────────────────────────────────╮
│ myapp v2.0.0                           │
│ A modern CLI tool                      │
╰────────────────────────────────────────╯

Usage:
  myapp [command] [options]

Commands:
  init   [name]     Initialize
  build  [--prod]   Build

Examples:
  $ myapp init my-project
  $ myapp build --prod
    Production build
```

## License

MIT
