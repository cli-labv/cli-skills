"""
CLI Scaffold - Project Structure & Shell Orchestration

This module provides:
1. File placement rules (where each file type should go)
2. Path validation (prevent wrong file locations)
3. Shell script consolidation (single start.sh entry point)
4. Project scaffolding (generate standard structures)

Design Principles:
- SOLID: Single responsibility per function
- DRY: No code repetition
- Clean Code: Self-documenting, minimal comments
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


# =============================================================================
# FILE PLACEMENT RULES
# =============================================================================

@dataclass
class ProjectRules:
    """
    Define where files should be placed in a project.
    
    Example:
        >>> rules = ProjectRules()
        >>> rules.get_correct_path("CHANGELOG.md")
        'docs/CHANGELOG.md'
        >>> rules.validate("src/main.py")
        (True, None)
    """
    
    # Files allowed in root (exceptions)
    root_allowed: Set[str] = field(default_factory=lambda: {
        "README.md",
        "LICENSE",
        "LICENSE.md",
        ".gitignore",
        ".env",
        ".env.example",
        "Makefile",
        "Dockerfile",
        "docker-compose.yml",
        "pyproject.toml",
        "setup.py",
        "setup.cfg",
        "requirements.txt",
        "package.json",
        "tsconfig.json",
        "start.sh",
        ".editorconfig",
    })
    
    # Extension to folder mapping
    extension_rules: Dict[str, str] = field(default_factory=lambda: {
        ".md": "docs",
        ".rst": "docs",
        ".txt": "docs",  # Except requirements.txt (in root_allowed)
        ".test.py": "tests",
        "_test.py": "tests",
        ".spec.py": "tests",
        ".test.js": "tests",
        ".spec.js": "tests",
        ".test.ts": "tests",
        ".spec.ts": "tests",
        ".sh": "scripts",  # Except start.sh (in root_allowed)
        ".bash": "scripts",
        ".sql": "sql",
        ".migration.py": "migrations",
    })
    
    # Pattern rules (more specific than extension)
    pattern_rules: Dict[str, str] = field(default_factory=lambda: {
        "test_*.py": "tests",
        "*_test.py": "tests",
        "conftest.py": "tests",
        "pytest.ini": "tests",
        "install*.sh": "scripts",
        "setup*.sh": "scripts",
        "build*.sh": "scripts",
        "deploy*.sh": "scripts",
        "*.example": "docs/examples",
        "CHANGELOG*": "docs",
        "CONTRIBUTING*": "docs",
        "SECURITY*": "docs",
        "CODE_OF_CONDUCT*": "docs",
    })
    
    def is_root_allowed(self, filename: str) -> bool:
        """Check if file is allowed in root."""
        return filename in self.root_allowed
    
    def get_target_folder(self, filepath: str) -> Optional[str]:
        """
        Get the correct folder for a file.
        
        Returns None if file can stay where it is.
        Returns folder name if file should be moved.
        """
        filename = Path(filepath).name
        
        # Root allowed files can stay in root
        if self.is_root_allowed(filename):
            return None
        
        # Check pattern rules first (more specific)
        for pattern, folder in self.pattern_rules.items():
            if self._match_pattern(filename, pattern):
                return folder
        
        # Check extension rules
        for ext, folder in self.extension_rules.items():
            if filename.endswith(ext):
                return folder
        
        return None
    
    def _match_pattern(self, filename: str, pattern: str) -> bool:
        """Simple pattern matching with * wildcard."""
        if "*" not in pattern:
            return filename == pattern
        
        if pattern.startswith("*"):
            return filename.endswith(pattern[1:])
        if pattern.endswith("*"):
            return filename.startswith(pattern[:-1])
        
        parts = pattern.split("*")
        return filename.startswith(parts[0]) and filename.endswith(parts[1])
    
    def validate(self, filepath: str) -> Tuple[bool, Optional[str]]:
        """
        Validate if a file is in the correct location.
        
        Returns:
            (True, None) if valid
            (False, "suggested/path") if invalid
        """
        path = Path(filepath)
        filename = path.name
        parent = str(path.parent) if path.parent != Path(".") else ""
        
        target = self.get_target_folder(filepath)
        
        # No rule applies, file is fine
        if target is None:
            return True, None
        
        # File is already in correct folder
        if parent == target or parent.endswith(f"/{target}"):
            return True, None
        
        # File should be moved
        correct_path = f"{target}/{filename}"
        return False, correct_path
    
    def get_correct_path(self, filepath: str) -> str:
        """Get the correct path for a file."""
        is_valid, suggested = self.validate(filepath)
        return filepath if is_valid else suggested


# Global default rules
_default_rules = ProjectRules()


def validate_path(filepath: str, rules: ProjectRules = None) -> Tuple[bool, Optional[str]]:
    """
    Validate file path against project rules.
    
    Example:
        >>> valid, suggestion = validate_path("NOTES.md")
        >>> if not valid:
        ...     print(f"Move to: {suggestion}")
        Move to: docs/NOTES.md
    """
    r = rules or _default_rules
    return r.validate(filepath)


def get_correct_path(filepath: str, rules: ProjectRules = None) -> str:
    """
    Get the correct path for a file.
    
    Example:
        >>> get_correct_path("install.sh")
        'scripts/install.sh'
        >>> get_correct_path("start.sh")
        'start.sh'
    """
    r = rules or _default_rules
    return r.get_correct_path(filepath)


# =============================================================================
# SHELL SCRIPT ORCHESTRATION
# =============================================================================

def generate_start_sh(
    project_name: str,
    commands: Dict[str, str] = None,
    python_cmd: str = "python3",
    use_venv: bool = True,
    main_script: str = "src/main.py",
) -> str:
    """
    Generate a consolidated start.sh script.
    
    This creates a single entry point that:
    - Handles all project tasks (install, run, build, test, etc.)
    - Follows SOLID principles
    - Is easily extensible
    
    Example:
        >>> sh = generate_start_sh("myapp", {"lint": "flake8 src/"})
        >>> print(sh)
    """
    
    venv_setup = '''
# =============================================================================
# VIRTUAL ENVIRONMENT
# =============================================================================

setup_venv() {
    if [ ! -d "venv" ]; then
        log_info "Creating virtual environment..."
        python3 -m venv venv
    fi
}

activate_venv() {
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
    elif [ -f "venv/Scripts/activate" ]; then
        source venv/Scripts/activate
    fi
}
''' if use_venv else ''

    venv_calls = '''    setup_venv
    activate_venv
''' if use_venv else ''

    template = f'''#!/usr/bin/env bash
# =============================================================================
# {project_name.upper()} - START SCRIPT
# =============================================================================
#
# Single entry point for all project tasks.
# Usage: ./start.sh [command]
#
# Principles:
#   - Single Responsibility: Each function does ONE thing
#   - DRY: Common logic in shared functions
#   - Fail Fast: Exit on first error
#
# =============================================================================

set -e  # Exit on error

# =============================================================================
# CONFIGURATION
# =============================================================================

PROJECT_NAME="{project_name}"
PYTHON_CMD="{python_cmd}"
MAIN_SCRIPT="{main_script}"

# Colors
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
CYAN='\\033[0;36m'
NC='\\033[0m'

# =============================================================================
# LOGGING FUNCTIONS (Single Responsibility)
# =============================================================================

log_info()    {{ echo -e "${{BLUE}}ℹ️  $1${{NC}}"; }}
log_success() {{ echo -e "${{GREEN}}✅ $1${{NC}}"; }}
log_warning() {{ echo -e "${{YELLOW}}⚠️  $1${{NC}}"; }}
log_error()   {{ echo -e "${{RED}}❌ $1${{NC}}"; }}

print_banner() {{
    echo -e "${{CYAN}}"
    echo "╔════════════════════════════════════════╗"
    echo "║  $PROJECT_NAME"
    echo "╚════════════════════════════════════════╝"
    echo -e "${{NC}}"
}}
{venv_setup}
# =============================================================================
# COMMAND FUNCTIONS (Single Responsibility)
# =============================================================================

cmd_install() {{
    log_info "Installing dependencies..."
{venv_calls}
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    elif [ -f "pyproject.toml" ]; then
        pip install -e .
    elif [ -f "package.json" ]; then
        npm install
    fi
    log_success "Dependencies installed!"
}}

cmd_run() {{
    log_info "Running $PROJECT_NAME..."
{venv_calls}
    $PYTHON_CMD "$MAIN_SCRIPT" "$@"
}}

cmd_dev() {{
    log_info "Starting development mode..."
{venv_calls}
    $PYTHON_CMD "$MAIN_SCRIPT" --dev "$@"
}}

cmd_test() {{
    log_info "Running tests..."
{venv_calls}
    if [ -f "pytest.ini" ] || [ -d "tests" ]; then
        pytest tests/ -v "$@"
    else
        $PYTHON_CMD -m unittest discover -v
    fi
}}

cmd_lint() {{
    log_info "Running linter..."
{venv_calls}
    if command -v ruff &> /dev/null; then
        ruff check .
    elif command -v flake8 &> /dev/null; then
        flake8 src/
    else
        log_warning "No linter found. Install ruff or flake8."
    fi
}}

cmd_build() {{
    log_info "Building project..."
{venv_calls}
    if [ -f "pyproject.toml" ]; then
        python -m build
    elif [ -f "setup.py" ]; then
        python setup.py build
    elif [ -f "package.json" ]; then
        npm run build
    fi
    log_success "Build complete!"
}}

cmd_clean() {{
    log_info "Cleaning temporary files..."
    rm -rf __pycache__ .pytest_cache .ruff_cache
    rm -rf build/ dist/ *.egg-info
    rm -rf node_modules/ .next/
    find . -type d -name "__pycache__" -exec rm -rf {{}} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    log_success "Cleaned!"
}}

cmd_help() {{
    print_banner
    echo "Usage: ./start.sh [command] [options]"
    echo ""
    echo "Commands:"
    echo "  install    Install dependencies"
    echo "  run        Run the application"
    echo "  dev        Run in development mode"
    echo "  test       Run tests"
    echo "  lint       Run linter"
    echo "  build      Build the project"
    echo "  clean      Clean temporary files"
    echo "  help       Show this help"
    echo ""
    echo "Examples:"
    echo "  ./start.sh install"
    echo "  ./start.sh run --verbose"
    echo "  ./start.sh test -k test_main"
}}

# =============================================================================
# MAIN DISPATCHER (Open/Closed - easy to extend)
# =============================================================================

main() {{
    local cmd="${{1:-help}}"
    shift 2>/dev/null || true
    
    case "$cmd" in
        install) cmd_install "$@" ;;
        run)     cmd_run "$@" ;;
        dev)     cmd_dev "$@" ;;
        test)    cmd_test "$@" ;;
        lint)    cmd_lint "$@" ;;
        build)   cmd_build "$@" ;;
        clean)   cmd_clean "$@" ;;
        help|-h|--help) cmd_help ;;
        *)
            log_error "Unknown command: $cmd"
            cmd_help
            exit 1
            ;;
    esac
}}

# =============================================================================
# ENTRY POINT
# =============================================================================

main "$@"
'''
    
    return template


# =============================================================================
# PROJECT SCAFFOLDING
# =============================================================================

@dataclass
class ProjectStructure:
    """Standard project structure."""
    
    folders: List[str] = field(default_factory=lambda: [
        "src",
        "tests",
        "docs",
        "scripts",
    ])
    
    files: Dict[str, str] = field(default_factory=dict)


def scaffold_project(
    name: str,
    path: str = ".",
    template: str = "python-cli",
    create_files: bool = True,
) -> Dict[str, str]:
    """
    Scaffold a new project with proper structure.
    
    Templates:
        - python-cli: Python CLI application
        - python-lib: Python library
        - minimal: Just essential folders
    
    Returns dict of created paths.
    
    Example:
        >>> files = scaffold_project("myapp", template="python-cli")
        >>> print(files.keys())
    """
    
    base = Path(path) / name if name != "." else Path(path)
    created = {}
    
    # Define structures
    structures = {
        "python-cli": ProjectStructure(
            folders=["src", "tests", "docs", "scripts"],
            files={
                "README.md": f"# {name}\n\nA Python CLI application.\n",
                "src/__init__.py": "",
                "src/main.py": f'''"""Main entry point."""

def main():
    print("Hello from {name}!")

if __name__ == "__main__":
    main()
''',
                "tests/__init__.py": "",
                "tests/test_main.py": '''"""Tests for main module."""

def test_placeholder():
    assert True
''',
                "docs/.gitkeep": "",
                "scripts/.gitkeep": "",
                ".gitignore": '''# Python
__pycache__/
*.pyc
*.pyo
venv/
.venv/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local
''',
                "requirements.txt": "# Add your dependencies here\n",
            }
        ),
        "python-lib": ProjectStructure(
            folders=["src", "tests", "docs", "examples"],
            files={
                "README.md": f"# {name}\n\nA Python library.\n",
                "src/__init__.py": f'"""{name} - A Python library."""\n\n__version__ = "0.1.0"\n',
                "tests/__init__.py": "",
                "docs/.gitkeep": "",
                "examples/.gitkeep": "",
                "pyproject.toml": f'''[project]
name = "{name}"
version = "0.1.0"
description = ""
readme = "README.md"
requires-python = ">=3.9"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
''',
            }
        ),
        "minimal": ProjectStructure(
            folders=["src", "docs"],
            files={
                "README.md": f"# {name}\n",
                "src/.gitkeep": "",
                "docs/.gitkeep": "",
            }
        ),
    }
    
    structure = structures.get(template, structures["minimal"])
    
    # Create folders
    for folder in structure.folders:
        folder_path = base / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        created[str(folder_path)] = "folder"
    
    # Create files
    if create_files:
        for filepath, content in structure.files.items():
            file_path = base / filepath
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            if not file_path.exists():
                file_path.write_text(content)
                created[str(file_path)] = "file"
        
        # Generate start.sh
        start_sh_path = base / "start.sh"
        if not start_sh_path.exists():
            start_sh_path.write_text(generate_start_sh(name))
            start_sh_path.chmod(0o755)
            created[str(start_sh_path)] = "file"
    
    return created


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("CLI Scaffold Demo")
    print("=" * 50)
    
    # Test validation
    print("\n1. Path Validation:")
    test_files = [
        "README.md",
        "CHANGELOG.md",
        "notes.md",
        "install.sh",
        "start.sh",
        "test_main.py",
        "main.py",
    ]
    
    for f in test_files:
        valid, suggestion = validate_path(f)
        if valid:
            print(f"  ✅ {f} → OK (root allowed)")
        else:
            print(f"  📁 {f} → {suggestion}")
    
    # Show start.sh preview
    print("\n2. Generated start.sh (first 30 lines):")
    sh = generate_start_sh("myapp")
    for i, line in enumerate(sh.split("\n")[:30]):
        print(f"  {line}")
    print("  ...")
