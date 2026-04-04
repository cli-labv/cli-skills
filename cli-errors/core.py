"""
Core implementation of CLI Errors.

Beautiful error messages with hints and suggestions.
"""

from __future__ import annotations

import sys
import traceback
from dataclasses import dataclass
from typing import Any, Optional, List

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    HAS_RICH = True
    console = Console(stderr=True)
except ImportError:
    HAS_RICH = False
    console = None


@dataclass
class CLIError(Exception):
    """
    CLI error with rich formatting support.
    
    Example:
        >>> raise CLIError(
        ...     "Config file not found",
        ...     hint="Create config.json in current directory",
        ...     suggestion="Run 'myapp init' to generate default config"
        ... )
    """
    message: str
    hint: Optional[str] = None
    suggestion: Optional[str] = None
    code: Optional[str] = None
    
    def __str__(self) -> str:
        return self.message


class ErrorHandler:
    """
    Error handler for CLI applications.
    
    Example:
        >>> handler = ErrorHandler(app_name="myapp")
        >>> 
        >>> try:
        ...     risky_operation()
        >>> except Exception as e:
        ...     handler.handle(e)
    """
    
    def __init__(
        self,
        app_name: str = "app",
        show_traceback: bool = False,
    ):
        self.app_name = app_name
        self.show_traceback = show_traceback
    
    def handle(self, error: Exception, exit_code: int = 1) -> None:
        """Handle an exception."""
        self.print_error(error)
        sys.exit(exit_code)
    
    def print_error(self, error: Exception) -> None:
        """Print formatted error."""
        if HAS_RICH:
            self._print_rich(error)
        else:
            self._print_plain(error)
    
    def _print_rich(self, error: Exception) -> None:
        """Print with rich formatting."""
        if isinstance(error, CLIError):
            # Header
            title = f"[bold red]Error[/bold red]"
            if error.code:
                title = f"[bold red]Error [{error.code}][/bold red]"
            
            content = Text()
            content.append(f"\n{error.message}\n", style="white")
            
            if error.hint:
                content.append(f"\n💡 Hint: ", style="yellow")
                content.append(f"{error.hint}\n", style="dim")
            
            if error.suggestion:
                content.append(f"\n📝 Suggestion: ", style="cyan")
                content.append(f"{error.suggestion}\n", style="dim")
            
            console.print(Panel(content, title=title, border_style="red"))
        else:
            console.print(f"[bold red]Error:[/bold red] {error}")
        
        if self.show_traceback:
            console.print_exception()
    
    def _print_plain(self, error: Exception) -> None:
        """Print without formatting."""
        if isinstance(error, CLIError):
            print(f"\nError: {error.message}", file=sys.stderr)
            if error.hint:
                print(f"  Hint: {error.hint}", file=sys.stderr)
            if error.suggestion:
                print(f"  Suggestion: {error.suggestion}", file=sys.stderr)
        else:
            print(f"Error: {error}", file=sys.stderr)
        
        if self.show_traceback:
            traceback.print_exc()


def print_error(
    message: str,
    hint: Optional[str] = None,
    suggestion: Optional[str] = None,
) -> None:
    """Print a formatted error message."""
    error = CLIError(message, hint, suggestion)
    handler = ErrorHandler()
    handler.print_error(error)


def exit_error(
    message: str,
    hint: Optional[str] = None,
    suggestion: Optional[str] = None,
    code: int = 1,
) -> None:
    """Print error and exit."""
    print_error(message, hint, suggestion)
    sys.exit(code)


if __name__ == "__main__":
    print("CLI Errors Demo")
    print("=" * 40)
    
    # Simple error
    print("\n1. Simple Error:")
    print_error("Something went wrong")
    
    # With hint
    print("\n2. With Hint:")
    print_error(
        "Configuration file not found",
        hint="Make sure config.json exists"
    )
    
    # Full error
    print("\n3. Full Error:")
    print_error(
        "Failed to connect to database",
        hint="Check if PostgreSQL is running",
        suggestion="Run 'docker-compose up -d postgres'"
    )
