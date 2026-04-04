"""
Core implementation of CLI Tables.

Table formatting using rich.table.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

try:
    from rich.console import Console
    from rich.table import Table as RichTable
    from rich import box
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


# Predefined styles
STYLES = {
    "default": "ROUNDED",
    "simple": "SIMPLE",
    "minimal": "MINIMAL",
    "heavy": "HEAVY",
    "double": "DOUBLE",
    "markdown": "MARKDOWN",
    "ascii": "ASCII",
}


@dataclass
class TableStyle:
    """Table styling options."""
    box_style: str = "ROUNDED"
    header_style: str = "bold cyan"
    row_styles: List[str] = field(default_factory=lambda: ["", "dim"])
    show_header: bool = True
    show_lines: bool = False


class Table:
    """
    Rich table wrapper.
    
    Example:
        >>> table = Table("Users")
        >>> table.add_column("ID", style="cyan")
        >>> table.add_column("Name")
        >>> table.add_column("Role")
        >>> table.add_row("1", "Alice", "Admin")
        >>> table.add_row("2", "Bob", "User")
        >>> table.print()
    """
    
    def __init__(
        self,
        title: str = "",
        style: Union[str, TableStyle] = "default",
    ):
        if not HAS_RICH:
            raise ImportError("rich required: pip install rich")
        
        if isinstance(style, str):
            box_name = STYLES.get(style, "ROUNDED")
            self.style = TableStyle(box_style=box_name)
        else:
            self.style = style
        
        box_obj = getattr(box, self.style.box_style, box.ROUNDED)
        
        self._table = RichTable(
            title=title if title else None,
            box=box_obj,
            header_style=self.style.header_style,
            show_header=self.style.show_header,
            show_lines=self.style.show_lines,
            row_styles=self.style.row_styles,
        )
    
    def add_column(
        self,
        header: str,
        style: str = "",
        justify: str = "left",
        width: int = None,
    ) -> "Table":
        """Add a column."""
        self._table.add_column(
            header,
            style=style or None,
            justify=justify,
            width=width,
        )
        return self
    
    def add_row(self, *values: Any) -> "Table":
        """Add a row."""
        self._table.add_row(*[str(v) for v in values])
        return self
    
    def print(self) -> None:
        """Print the table."""
        console.print(self._table)


def print_table(
    data: Union[List[Dict], List[List]],
    columns: List[str] = None,
    title: str = "",
    style: str = "default",
) -> None:
    """
    Quick table print.
    
    Example:
        >>> data = [
        ...     {"name": "Alice", "age": 30},
        ...     {"name": "Bob", "age": 25},
        ... ]
        >>> print_table(data, title="Users")
    """
    if not data:
        return
    
    table = Table(title, style)
    
    # Determine columns
    if not columns:
        if isinstance(data[0], dict):
            columns = list(data[0].keys())
        else:
            columns = [f"Col {i+1}" for i in range(len(data[0]))]
    
    for col in columns:
        table.add_column(col)
    
    # Add rows
    for row in data:
        if isinstance(row, dict):
            table.add_row(*[row.get(c, "") for c in columns])
        else:
            table.add_row(*row)
    
    table.print()


def print_dict(
    data: Dict[str, Any],
    title: str = "",
    key_style: str = "cyan",
) -> None:
    """Print dictionary as key-value table."""
    if not HAS_RICH:
        for k, v in data.items():
            print(f"{k}: {v}")
        return
    
    table = Table(title, "simple")
    table.add_column("Key", style=key_style)
    table.add_column("Value")
    
    for key, value in data.items():
        table.add_row(str(key), str(value))
    
    table.print()


def print_key_value(
    items: List[tuple],
    title: str = "",
) -> None:
    """Print key-value pairs."""
    print_dict(dict(items), title)


if __name__ == "__main__":
    print("CLI Tables Demo")
    print("=" * 40)
    
    # From dict list
    print("\n1. From dictionaries:")
    data = [
        {"name": "Alice", "role": "Admin", "status": "Active"},
        {"name": "Bob", "role": "User", "status": "Active"},
        {"name": "Charlie", "role": "User", "status": "Inactive"},
    ]
    print_table(data, title="Users")
    
    # Custom table
    print("\n2. Custom table:")
    table = Table("Products", style="double")
    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Name")
    table.add_column("Price", justify="right")
    table.add_row("1", "Widget", "$9.99")
    table.add_row("2", "Gadget", "$19.99")
    table.add_row("3", "Gizmo", "$14.99")
    table.print()
    
    # Key-value
    print("\n3. Key-value pairs:")
    print_dict({
        "Version": "1.0.0",
        "Python": "3.11",
        "OS": "Linux",
    }, title="Config")
