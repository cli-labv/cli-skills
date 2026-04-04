#!/usr/bin/env python3
"""
Example 1: Basic Prompts

Demonstrates the fundamental prompt types:
- confirm (yes/no)
- text input
- password input
- single select
"""

from skills.cli_prompts import (
    confirm,
    text,
    password,
    select,
    PromptAbortedError,
)


def main():
    """Run basic prompts demo."""
    print("=" * 50)
    print("  Basic Prompts Demo")
    print("=" * 50)
    print()
    
    try:
        # 1. Simple confirmation
        proceed = confirm("Would you like to start the demo?", default=True)
        
        if not proceed:
            print("Demo cancelled. Goodbye!")
            return
        
        # 2. Text input
        name = text(
            "What's your name?",
            default="Developer",
        )
        print(f"  → Hello, {name}!")
        print()
        
        # 3. Text with validation
        email = text(
            "Enter your email:",
            validate=lambda x: "@" in x and "." in x or "Please enter a valid email",
        )
        print(f"  → Email: {email}")
        print()
        
        # 4. Password input
        api_key = password(
            "Enter your API key:",
            validate=lambda x: len(x) >= 8 or "API key must be at least 8 characters",
        )
        print(f"  → API key received ({len(api_key)} characters)")
        print()
        
        # 5. Single selection
        environment = select(
            "Select deployment environment:",
            choices=[
                "development",
                "staging",
                "production",
            ],
            default="development",
        )
        print(f"  → Selected: {environment}")
        print()
        
        # Summary
        print("=" * 50)
        print("  Configuration Summary")
        print("=" * 50)
        print(f"  Name: {name}")
        print(f"  Email: {email}")
        print(f"  Environment: {environment}")
        print()
        
        if confirm("Save this configuration?"):
            print("  ✅ Configuration saved!")
        else:
            print("  ❌ Configuration discarded")
    
    except PromptAbortedError:
        print("\n\n  Aborted by user (Ctrl+C)")
    
    except ImportError as e:
        print(f"\n  Error: {e}")
        print("  Install dependencies: pip install questionary")


if __name__ == "__main__":
    main()
