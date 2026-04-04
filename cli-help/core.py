"""
Core implementation of CLI Help.

Beautiful help panels using rich.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


@dataclass
class Command:
    """A CLI command."""
    name: str
    description: str
    args: str = ""


@dataclass
class Example:
    """A usage example."""
    command: str
    description: str = ""


@dataclass
class HelpPanel:
    """
    Help panel generator.
    
    Example:
        >>> help = HelpPanel(
        ...     name="myapp",
        ...     version="1.0.0",
        ...     description="My awesome CLI"
        ... )
        >>> help.add_command("init", "Initialize project", "[name]")
        >>> help.add_example("myapp init my-project")
        >>> help.print()
    """
    name: str
    version: str = "1.0.0"
    description: str = ""
    commands: List[Command] = field(default_factory=list)
    examples: List[Example] = field(default_factory=list)
    
    def add_command(
        self,
        name: str,
        description: str,
        args: str = "",
    ) -> "HelpPanel":
        """Add a command."""
        self.commands.append(Command(name, description, args))
        return self
    
    def add_example(
        self,
        command: str,
        description: str = "",
    ) -> "HelpPanel":
        """Add an example."""
        self.examples.append(Example(command, description))
        return self
    
    def print(self) -> None:
        """Print the help panel."""
        if HAS_RICH:
            self._print_rich()
        else:
            self._print_plain()
    
    def _print_rich(self) -> None:
        """Print with rich formatting."""
        # Header
        console.print(Panel(
            f"[bold cyan]{self.name}[/] v{self.version}\n{self.description}",
            border_style="cyan"
        ))
        
        # Usage
        console.print("\n[bold]Usage:[/bold]")
        console.print(f"  {self.name} [command] [options]\n")
        
        # Commands
        if self.commands:
            console.print("[bold]Commands:[/bold]")
            table = Table(show_header=False, box=None, padding=(0, 2))
            table.add_column(style="green")
            table.add_column(style="dim")
            table.add_column()
            
            for cmd in self.commands:
                table.add_row(
                    f"  {cmd.name}",
                    cmd.args if cmd.args else "",
                    cmd.description
                )
            console.print(table)
        
        # Examples
        if self.examples:
            console.print("\n[bold]Examples:[/bold]")
            for ex in self.examples:
                console.print(f"  [cyan]$[/] {ex.command}")
                if ex.description:
                    console.print(f"    [dim]{ex.description}[/]")
        
        console.print()
    
    def _print_plain(self) -> None:
        """Print without formatting."""
        print(f"\n{self.name} v{self.version}")
        print(f"{self.description}\n")
        print("Usage:")
        print(f"  {self.name} [command] [options]\n")
        
        if self.commands:
            print("Commands:")
            for cmd in self.commands:
                args = f" {cmd.args}" if cmd.args else ""
                print(f"  {cmd.name}{args}  {cmd.description}")
        
        if self.examples:
            print("\nExamples:")
            for ex in self.examples:
                print(f"  $ {ex.command}")


def print_help(
    name: str,
    version: str = "1.0.0",
    description: str = "",
    commands: Dict[str, str] = None,
    examples: List[str] = None,
) -> None:
    """Print quick help."""
    panel = HelpPanel(name, version, description)
    for cmd, desc in (commands or {}).items():
        panel.add_command(cmd, desc)
    for ex in (examples or []):
        panel.add_example(ex)
    panel.print()


def print_usage(name: str, usage: str) -> None:
    """Print usage line."""
    if HAS_RICH:
        console.print(f"[bold]Usage:[/] {name} {usage}")
    else:
        print(f"Usage: {name} {usage}")


def print_examples(examples: List[str]) -> None:
    """Print example commands."""
    if HAS_RICH:
        console.print("[bold]Examples:[/bold]")
        for ex in examples:
            console.print(f"  [cyan]$[/] {ex}")
    else:
        print("Examples:")
        for ex in examples:
            print(f"  $ {ex}")


if __name__ == "__main__":
    help = HelpPanel(
        name="myapp",
        version="2.0.0",
        description="A modern CLI application"
    )
    help.add_command("init", "Initialize a new project", "[name]")
    help.add_command("build", "Build the project", "[--prod]")
    help.add_command("deploy", "Deploy to production")
    help.add_command("config", "Manage configuration", "[get|set]")
    
    help.add_example("myapp init my-project")
    help.add_example("myapp build --prod", "Build for production")
    help.add_example("myapp config set api_key xxxxx")
    
    help.print()
