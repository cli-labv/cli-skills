"""
Core implementation of CLI Args.

Simplified argument parsing wrapper for Typer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Optional, List

try:
    import typer
    from typer import Argument as TyperArgument
    from typer import Option as TyperOption
    HAS_TYPER = True
except ImportError:
    HAS_TYPER = False


def Argument(
    default: Any = ...,
    help: str = "",
    **kwargs
) -> Any:
    """Create a CLI argument."""
    if not HAS_TYPER:
        return default
    return TyperArgument(default, help=help, **kwargs)


def Option(
    default: Any = None,
    help: str = "",
    short: str = "",
    **kwargs
) -> Any:
    """Create a CLI option."""
    if not HAS_TYPER:
        return default
    names = []
    if short:
        names.append(f"-{short}")
    return TyperOption(default, *names, help=help, **kwargs)


class App:
    """
    CLI application wrapper.
    
    Example:
        >>> app = App("myapp", "My awesome CLI")
        >>> 
        >>> @app.command()
        >>> def hello(name: str = Argument(..., help="Name")):
        ...     print(f"Hello {name}")
        >>> 
        >>> app.run()
    """
    
    def __init__(
        self,
        name: str = "app",
        help: str = "",
        version: str = None,
    ):
        if not HAS_TYPER:
            raise ImportError("typer required: pip install typer")
        
        self.name = name
        self._app = typer.Typer(
            name=name,
            help=help,
            add_completion=False,
        )
        
        if version:
            self._add_version(version)
    
    def _add_version(self, version: str) -> None:
        """Add version callback."""
        def version_callback(value: bool):
            if value:
                print(f"{self.name} v{version}")
                raise typer.Exit()
        
        @self._app.callback()
        def main(
            version: bool = typer.Option(
                False, "--version", "-v",
                callback=version_callback,
                is_eager=True,
                help="Show version"
            )
        ):
            pass
    
    def command(
        self,
        name: str = None,
        help: str = "",
    ) -> Callable:
        """Decorator to add a command."""
        return self._app.command(name=name, help=help)
    
    def run(self) -> None:
        """Run the application."""
        self._app()


def run(func: Callable) -> None:
    """Run a single function as CLI."""
    if not HAS_TYPER:
        raise ImportError("typer required: pip install typer")
    typer.run(func)


if __name__ == "__main__":
    app = App("demo", "Demo CLI", version="1.0.0")
    
    @app.command()
    def greet(
        name: str = Argument(..., help="Name to greet"),
        loud: bool = Option(False, help="Shout greeting", short="l"),
    ):
        """Greet someone."""
        msg = f"Hello, {name}!"
        if loud:
            msg = msg.upper()
        print(msg)
    
    @app.command()
    def goodbye(name: str = Argument("World")):
        """Say goodbye."""
        print(f"Goodbye, {name}!")
    
    app.run()
