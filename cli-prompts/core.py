"""
Core implementation of CLI Prompts.

This module provides beautiful, interactive command-line prompts using
questionary with enhanced defaults and consistent styling.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from pathlib import Path as PathLib
from typing import (
    Any,
    Callable,
    List,
    Optional,
    Sequence,
    TypeVar,
    Union,
)

try:
    import questionary
    from questionary import Style, Choice
    HAS_QUESTIONARY = True
except ImportError:
    HAS_QUESTIONARY = False
    questionary = None
    Style = None
    Choice = None

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


# Type variables
T = TypeVar("T")


class PromptAbortedError(Exception):
    """Raised when user aborts a prompt (Ctrl+C)."""
    pass


@dataclass
class PromptStyle:
    """
    Configuration for prompt styling.
    
    Attributes:
        question_mark: Color for the question mark prefix
        question: Color for the question text
        answer: Color for the user's answer
        pointer: Color for the selection pointer
        highlighted: Color for highlighted items
        selected: Color for selected checkbox items
        instruction: Color for instruction text
        separator: Color for separators
    """
    question_mark: str = "#5F87FF bold"  # Blue
    question: str = "bold"
    answer: str = "#87D75F bold"  # Green
    pointer: str = "#5F87FF bold"  # Blue
    highlighted: str = "#5F87FF"  # Blue
    selected: str = "#87D75F"  # Green
    instruction: str = "#8A8A8A"  # Gray
    separator: str = "#8A8A8A"  # Gray
    
    def to_questionary_style(self) -> Optional[Style]:
        """Convert to questionary Style object."""
        if not HAS_QUESTIONARY:
            return None
        return Style([
            ("qmark", self.question_mark),
            ("question", self.question),
            ("answer", self.answer),
            ("pointer", self.pointer),
            ("highlighted", self.highlighted),
            ("selected", self.selected),
            ("instruction", self.instruction),
            ("separator", self.separator),
        ])


# Default style instance
_default_style = PromptStyle()


def get_default_style() -> PromptStyle:
    """Get the current default prompt style."""
    return _default_style


def set_default_style(style: PromptStyle) -> None:
    """Set the default prompt style."""
    global _default_style
    _default_style = style


def _check_dependencies() -> None:
    """Check if required dependencies are installed."""
    if not HAS_QUESTIONARY:
        raise ImportError(
            "questionary is required for cli-prompts. "
            "Install it with: pip install questionary"
        )


def _handle_abort(result: Any) -> Any:
    """Handle None result (user abort) by raising exception."""
    if result is None:
        raise PromptAbortedError("User aborted the prompt")
    return result


def confirm(
    message: str,
    default: bool = False,
    auto_enter: bool = True,
    style: Optional[PromptStyle] = None,
) -> bool:
    """
    Ask for yes/no confirmation.
    
    Args:
        message: The question to ask
        default: Default value if user just presses Enter
        auto_enter: If True, single keypress (y/n) confirms without Enter
        style: Custom style (uses default if None)
    
    Returns:
        True if user confirmed, False otherwise
    
    Raises:
        PromptAbortedError: If user presses Ctrl+C
    
    Example:
        >>> if confirm("Delete all files?", default=False):
        ...     print("Deleting...")
        ... else:
        ...     print("Cancelled")
    """
    _check_dependencies()
    
    style = style or _default_style
    
    result = questionary.confirm(
        message,
        default=default,
        auto_enter=auto_enter,
        style=style.to_questionary_style(),
    ).ask()
    
    return _handle_abort(result)


def text(
    message: str,
    default: str = "",
    multiline: bool = False,
    validate: Optional[Callable[[str], Union[bool, str]]] = None,
    instruction: Optional[str] = None,
    style: Optional[PromptStyle] = None,
) -> str:
    """
    Ask for text input.
    
    Args:
        message: The question to ask
        default: Default value
        multiline: Allow multiple lines (Alt+Enter to submit)
        validate: Validation function returning True or error message
        instruction: Help text shown below the prompt
        style: Custom style (uses default if None)
    
    Returns:
        The text entered by the user
    
    Raises:
        PromptAbortedError: If user presses Ctrl+C
    
    Example:
        >>> name = text("What's your name?", default="Anonymous")
        >>> email = text(
        ...     "Email address?",
        ...     validate=lambda x: "@" in x or "Must contain @"
        ... )
    """
    _check_dependencies()
    
    style = style or _default_style
    
    result = questionary.text(
        message,
        default=default,
        multiline=multiline,
        validate=validate,
        instruction=instruction,
        style=style.to_questionary_style(),
    ).ask()
    
    return _handle_abort(result)


def password(
    message: str,
    validate: Optional[Callable[[str], Union[bool, str]]] = None,
    style: Optional[PromptStyle] = None,
) -> str:
    """
    Ask for password input (hidden).
    
    Args:
        message: The question to ask
        validate: Validation function returning True or error message
        style: Custom style (uses default if None)
    
    Returns:
        The password entered by the user
    
    Raises:
        PromptAbortedError: If user presses Ctrl+C
    
    Example:
        >>> pwd = password("Enter password:")
        >>> pwd = password(
        ...     "Password (min 8 chars):",
        ...     validate=lambda x: len(x) >= 8 or "Too short"
        ... )
    """
    _check_dependencies()
    
    style = style or _default_style
    
    result = questionary.password(
        message,
        validate=validate,
        style=style.to_questionary_style(),
    ).ask()
    
    return _handle_abort(result)


def select(
    message: str,
    choices: Sequence[Union[str, Choice, dict]],
    default: Optional[str] = None,
    instruction: Optional[str] = None,
    use_shortcuts: bool = False,
    use_arrow_keys: bool = True,
    use_jk_keys: bool = True,
    style: Optional[PromptStyle] = None,
) -> str:
    """
    Select one option from a list.
    
    Args:
        message: The question to ask
        choices: List of choices (strings, Choice objects, or dicts)
        default: Default selected choice
        instruction: Help text shown below the prompt
        use_shortcuts: Allow number shortcuts (1, 2, 3...)
        use_arrow_keys: Allow arrow key navigation
        use_jk_keys: Allow j/k vim-style navigation
        style: Custom style (uses default if None)
    
    Returns:
        The selected choice value
    
    Raises:
        PromptAbortedError: If user presses Ctrl+C
    
    Example:
        >>> color = select("Pick a color:", ["red", "green", "blue"])
        >>> 
        >>> # With custom display
        >>> env = select("Environment:", [
        ...     {"name": "Development", "value": "dev"},
        ...     {"name": "Production", "value": "prod"},
        ... ])
    """
    _check_dependencies()
    
    style = style or _default_style
    
    # Convert dict choices to Choice objects
    processed_choices = []
    for choice in choices:
        if isinstance(choice, dict):
            processed_choices.append(Choice(
                title=choice.get("name", choice.get("title", "")),
                value=choice.get("value"),
                disabled=choice.get("disabled"),
            ))
        else:
            processed_choices.append(choice)
    
    result = questionary.select(
        message,
        choices=processed_choices,
        default=default,
        instruction=instruction,
        use_shortcuts=use_shortcuts,
        use_arrow_keys=use_arrow_keys,
        use_jk_keys=use_jk_keys,
        style=style.to_questionary_style(),
    ).ask()
    
    return _handle_abort(result)


def checkbox(
    message: str,
    choices: Sequence[Union[str, Choice, dict]],
    default: Optional[List[str]] = None,
    instruction: Optional[str] = None,
    validate: Optional[Callable[[List[str]], Union[bool, str]]] = None,
    style: Optional[PromptStyle] = None,
) -> List[str]:
    """
    Select multiple options from a list.
    
    Args:
        message: The question to ask
        choices: List of choices
        default: List of pre-selected values
        instruction: Help text shown below the prompt
        validate: Validation function for the selection
        style: Custom style (uses default if None)
    
    Returns:
        List of selected choice values
    
    Raises:
        PromptAbortedError: If user presses Ctrl+C
    
    Example:
        >>> features = checkbox(
        ...     "Select features:",
        ...     ["auth", "api", "admin", "docs"],
        ...     default=["auth"]
        ... )
        >>> 
        >>> # Require at least one selection
        >>> items = checkbox(
        ...     "Pick at least one:",
        ...     ["A", "B", "C"],
        ...     validate=lambda x: len(x) > 0 or "Select at least one"
        ... )
    """
    _check_dependencies()
    
    style = style or _default_style
    
    # Process choices
    processed_choices = []
    default_set = set(default or [])
    
    for choice in choices:
        if isinstance(choice, dict):
            value = choice.get("value", choice.get("name", ""))
            processed_choices.append(Choice(
                title=choice.get("name", choice.get("title", "")),
                value=value,
                checked=value in default_set or choice.get("checked", False),
                disabled=choice.get("disabled"),
            ))
        elif isinstance(choice, str):
            processed_choices.append(Choice(
                title=choice,
                value=choice,
                checked=choice in default_set,
            ))
        else:
            processed_choices.append(choice)
    
    result = questionary.checkbox(
        message,
        choices=processed_choices,
        instruction=instruction,
        validate=validate,
        style=style.to_questionary_style(),
    ).ask()
    
    return _handle_abort(result)


def path(
    message: str,
    default: str = "",
    only_directories: bool = False,
    file_filter: Optional[Callable[[str], bool]] = None,
    complete_style: str = "MULTI_COLUMN",
    validate: Optional[Callable[[str], Union[bool, str]]] = None,
    style: Optional[PromptStyle] = None,
) -> str:
    """
    Ask for a file or directory path with autocomplete.
    
    Args:
        message: The question to ask
        default: Default path
        only_directories: Only show directories in completion
        file_filter: Function to filter shown files
        complete_style: Completion display style
        validate: Validation function
        style: Custom style (uses default if None)
    
    Returns:
        The selected path
    
    Raises:
        PromptAbortedError: If user presses Ctrl+C
    
    Example:
        >>> config_file = path("Config file:", default="./config.json")
        >>> output_dir = path("Output directory:", only_directories=True)
    """
    _check_dependencies()
    
    style = style or _default_style
    
    result = questionary.path(
        message,
        default=default,
        only_directories=only_directories,
        file_filter=file_filter,
        validate=validate,
        style=style.to_questionary_style(),
    ).ask()
    
    return _handle_abort(result)


def autocomplete(
    message: str,
    choices: Sequence[str],
    default: str = "",
    match_middle: bool = True,
    validate: Optional[Callable[[str], Union[bool, str]]] = None,
    style: Optional[PromptStyle] = None,
) -> str:
    """
    Text input with autocomplete suggestions.
    
    Args:
        message: The question to ask
        choices: List of autocomplete suggestions
        default: Default value
        match_middle: Match anywhere in string (not just start)
        validate: Validation function
        style: Custom style (uses default if None)
    
    Returns:
        The entered/selected text
    
    Raises:
        PromptAbortedError: If user presses Ctrl+C
    
    Example:
        >>> country = autocomplete(
        ...     "Country:",
        ...     ["United States", "United Kingdom", "Canada", "Mexico"]
        ... )
    """
    _check_dependencies()
    
    style = style or _default_style
    
    result = questionary.autocomplete(
        message,
        choices=list(choices),
        default=default,
        match_middle=match_middle,
        validate=validate,
        style=style.to_questionary_style(),
    ).ask()
    
    return _handle_abort(result)


def pause(message: str = "Press Enter to continue...") -> None:
    """
    Pause execution until user presses Enter.
    
    Args:
        message: Message to display
    
    Example:
        >>> print("Step 1 complete!")
        >>> pause()
        >>> print("Continuing to step 2...")
    """
    if HAS_RICH:
        console.print(f"\n[dim]{message}[/dim]", end="")
    else:
        print(f"\n{message}", end="")
    
    input()


def clear() -> None:
    """
    Clear the terminal screen.
    
    Example:
        >>> clear()
        >>> print("Fresh start!")
    """
    os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# Convenience functions for common patterns
# ============================================================

def yes_no(message: str, default: bool = True) -> bool:
    """Alias for confirm() with more intuitive name."""
    return confirm(message, default=default)


def ask(message: str, default: str = "") -> str:
    """Alias for text() with simpler name."""
    return text(message, default=default)


def choose(message: str, options: List[str]) -> str:
    """Alias for select() with simpler name."""
    return select(message, options)


def multi_choose(message: str, options: List[str]) -> List[str]:
    """Alias for checkbox() with simpler name."""
    return checkbox(message, options)


if __name__ == "__main__":
    # Quick demo
    print("CLI Prompts Demo")
    print("=" * 40)
    
    try:
        name = text("What's your name?", default="Developer")
        print(f"Hello, {name}!")
        
        if confirm("Do you want to continue?"):
            color = select("Pick a color:", ["red", "green", "blue"])
            print(f"You chose: {color}")
            
            features = checkbox(
                "Select features:",
                ["auth", "api", "admin", "docs"],
                default=["auth"]
            )
            print(f"Features: {features}")
        
        print("\nDemo complete!")
        
    except PromptAbortedError:
        print("\nAborted by user")
    except ImportError as e:
        print(f"\nMissing dependency: {e}")
        print("Install with: pip install questionary rich")
