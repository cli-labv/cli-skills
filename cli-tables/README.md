# CLI Tables 📊

Beautiful table formatting for Python CLI applications.

A wrapper around [rich.table](https://rich.readthedocs.io/en/latest/tables.html) providing easy-to-use table rendering with colors, styles, and formatting.

## Installation

```bash
pip install rich
```

## Quick Start

```python
from skills.cli_tables import print_table

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
]

print_table(data, title="Users")
```

Output:
```
╭───────────────────────────────────╮
│              Users                │
├─────────┬─────┬─────────────────┤
│ name    │ age │ city            │
├─────────┼─────┼─────────────────┤
│ Alice   │ 30  │ New York        │
│ Bob     │ 25  │ Los Angeles     │
╰─────────┴─────┴─────────────────╯
```

## Features

### Basic Table

```python
from skills.cli_tables import print_table

users = [
    {"name": "Alice", "role": "Admin", "active": True},
    {"name": "Bob", "role": "User", "active": False},
]

print_table(users)
```

### Styled Columns

```python
print_table(
    users,
    title="Team Members",
    column_styles={
        "name": "cyan",
        "role": "green",
        "active": "yellow",
    }
)
```

### Custom Formatters

```python
print_table(
    users,
    formatters={
        "active": lambda x: "✅" if x else "❌",
        "name": lambda x: x.upper(),
    }
)
```

### Table Styles

```python
# Rounded corners (default)
print_table(data, style="rounded")

# Simple lines
print_table(data, style="simple")

# Double lines
print_table(data, style="double")

# ASCII only
print_table(data, style="ascii")

# Minimal
print_table(data, style="minimal")
```

### Table Builder

For more control:

```python
from skills.cli_tables import Table

table = Table(title="Products")

table.add_column("ID", style="dim")
table.add_column("Name", style="cyan")
table.add_column("Price", justify="right", style="green")
table.add_column("Stock", justify="right")

table.add_row("001", "Widget", "$9.99", "50")
table.add_row("002", "Gadget", "$19.99", "25")
table.add_row("003", "Gizmo", "$14.99", "0")

table.print()
```

### Dictionary Display

```python
from skills.cli_tables import print_dict

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
}

print_dict(config, title="Configuration")
```

### Key-Value Pairs

```python
from skills.cli_tables import print_key_value

print_key_value([
    ("Application", "My CLI App"),
    ("Version", "2.0.0"),
    ("Status", "✅ Running"),
])
```

## API Reference

### print_table()

```python
print_table(
    data: List[Dict] | List[List],
    columns: List[str] = None,        # Auto-detected
    title: str = None,
    style: str = "default",
    column_styles: Dict[str, str] = None,
    formatters: Dict[str, Callable] = None,
)
```

### Table Class

```python
table = Table(title="My Table", style="rounded")
table.add_column(header, style=None, justify="left", width=None)
table.add_row(*values, style=None)
table.add_rows(rows)
table.print()
```

### Styles

| Style | Description |
|-------|-------------|
| `rounded` | Rounded corners (default) |
| `simple` | Simple lines |
| `minimal` | Very minimal |
| `double` | Double lines |
| `heavy` | Thick lines |
| `ascii` | ASCII only |

## License

MIT
