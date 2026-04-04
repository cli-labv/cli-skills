"""
CLI Prompts - Beautiful interactive prompts for CLI applications.

A wrapper around questionary with enhanced defaults and consistent styling.

Example:
    >>> from skills.cli_prompts import confirm, select, text
    >>> 
    >>> if confirm("Do you want to continue?"):
    ...     name = text("What's your name?")
    ...     color = select("Favorite color?", ["red", "green", "blue"])
"""

from .core import (
    # Main prompt functions
    confirm,
    text,
    password,
    select,
    checkbox,
    path,
    
    # Advanced prompts
    autocomplete,
    
    # Styling
    PromptStyle,
    get_default_style,
    set_default_style,
    
    # Utilities
    pause,
    clear,
    
    # Aliases
    yes_no,
    ask,
    choose,
    multi_choose,
    
    # Exceptions
    PromptAbortedError,
)

__version__ = "2.0.0"
__all__ = [
    "confirm",
    "text",
    "password",
    "select",
    "checkbox",
    "path",
    "autocomplete",
    "PromptStyle",
    "get_default_style",
    "set_default_style",
    "pause",
    "clear",
    "yes_no",
    "ask",
    "choose",
    "multi_choose",
    "PromptAbortedError",
]