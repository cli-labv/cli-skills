#!/usr/bin/env python3
"""
Example: Basic path validation

Shows how to validate file paths before creating them.
"""

from skills.cli_scaffold import validate_path, get_correct_path

def main():
    print("File Path Validation Example")
    print("=" * 50)
    
    # Test various file paths
    test_files = [
        # Root allowed
        "README.md",
        "LICENSE",
        "requirements.txt",
        "start.sh",
        ".gitignore",
        
        # Should go in docs/
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "API_DOCS.md",
        "notes.md",
        
        # Should go in scripts/
        "install.sh",
        "setup.sh",
        "deploy.sh",
        
        # Should go in tests/
        "test_main.py",
        "user_test.py",
        "conftest.py",
    ]
    
    print("\nValidation Results:")
    print("-" * 50)
    
    for filepath in test_files:
        valid, suggestion = validate_path(filepath)
        
        if valid:
            print(f"✅ {filepath:<25} → OK (root)")
        else:
            print(f"📁 {filepath:<25} → {suggestion}")
    
    # Direct correction
    print("\n\nDirect Path Correction:")
    print("-" * 50)
    
    files_to_create = ["NOTES.md", "build.sh", "test_api.py"]
    
    for f in files_to_create:
        correct = get_correct_path(f)
        print(f"  {f} → {correct}")


if __name__ == "__main__":
    main()
