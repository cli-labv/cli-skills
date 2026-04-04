"""CLI Scaffold - Project structure and shell orchestration."""
from .core import (
    ProjectRules,
    validate_path,
    get_correct_path,
    scaffold_project,
    generate_start_sh,
)

__version__ = "1.0.0"
__all__ = [
    "ProjectRules",
    "validate_path", 
    "get_correct_path",
    "scaffold_project",
    "generate_start_sh",
]
