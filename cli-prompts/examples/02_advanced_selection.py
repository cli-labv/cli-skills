#!/usr/bin/env python3
"""
Example 2: Advanced Selection

Demonstrates advanced selection features:
- Checkbox (multi-select)
- Select with custom display names
- Autocomplete
- Path selection
"""

from skills.cli_prompts import (
    select,
    checkbox,
    autocomplete,
    path,
    confirm,
    PromptAbortedError,
)


# Sample data
COUNTRIES = [
    "Argentina", "Australia", "Brazil", "Canada", "Chile",
    "China", "France", "Germany", "India", "Italy",
    "Japan", "Mexico", "Spain", "United Kingdom", "United States",
]

FRAMEWORKS = [
    {"name": "FastAPI - Modern async API", "value": "fastapi"},
    {"name": "Flask - Lightweight WSGI", "value": "flask"},
    {"name": "Django - Batteries included", "value": "django"},
    {"name": "Starlette - ASGI toolkit", "value": "starlette"},
]

FEATURES = [
    {"name": "🔐 Authentication", "value": "auth"},
    {"name": "📊 Database ORM", "value": "database"},
    {"name": "📝 API Documentation", "value": "docs"},
    {"name": "🧪 Testing Suite", "value": "testing"},
    {"name": "🐳 Docker Support", "value": "docker"},
    {"name": "🚀 CI/CD Pipeline", "value": "cicd"},
]


def main():
    """Run advanced selection demo."""
    print("=" * 50)
    print("  Advanced Selection Demo")
    print("=" * 50)
    print()
    
    try:
        # 1. Select with custom display names
        print("1. Framework Selection (with descriptions)")
        print("-" * 40)
        framework = select(
            "Choose a web framework:",
            choices=FRAMEWORKS,
            instruction="Use arrow keys to navigate",
        )
        print(f"  → Selected: {framework}")
        print()
        
        # 2. Checkbox multi-select
        print("2. Feature Selection (multi-select)")
        print("-" * 40)
        features = checkbox(
            "Select features to include:",
            choices=FEATURES,
            default=["auth", "database"],  # Pre-selected
            validate=lambda x: len(x) >= 1 or "Select at least one feature",
        )
        print(f"  → Selected features: {features}")
        print()
        
        # 3. Autocomplete
        print("3. Country Autocomplete")
        print("-" * 40)
        country = autocomplete(
            "Enter your country:",
            choices=COUNTRIES,
            match_middle=True,  # Match anywhere in string
        )
        print(f"  → Selected: {country}")
        print()
        
        # 4. Path selection
        print("4. Path Selection")
        print("-" * 40)
        project_path = path(
            "Select project directory:",
            default="./",
            only_directories=True,
        )
        print(f"  → Path: {project_path}")
        print()
        
        # Summary
        print("=" * 50)
        print("  Project Configuration")
        print("=" * 50)
        print(f"  Framework: {framework}")
        print(f"  Features: {', '.join(features)}")
        print(f"  Country: {country}")
        print(f"  Path: {project_path}")
        print()
        
        if confirm("Create project with these settings?"):
            print("  ✅ Project created!")
        else:
            print("  ❌ Cancelled")
    
    except PromptAbortedError:
        print("\n\n  Aborted by user (Ctrl+C)")
    
    except ImportError as e:
        print(f"\n  Error: {e}")
        print("  Install dependencies: pip install questionary")


if __name__ == "__main__":
    main()
