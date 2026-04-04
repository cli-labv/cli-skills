#!/usr/bin/env python3
"""
Example: Generate consolidated start.sh

Shows how to generate a single entry point script.
"""

from skills.cli_scaffold import generate_start_sh

def main():
    print("Generate start.sh Example")
    print("=" * 50)
    
    # Generate basic start.sh
    content = generate_start_sh(
        project_name="myapp",
        python_cmd="python3",
        use_venv=True,
        main_script="src/main.py"
    )
    
    # Show first 50 lines
    print("\nGenerated start.sh (preview):")
    print("-" * 50)
    
    lines = content.split("\n")
    for line in lines[:50]:
        print(line)
    
    print("\n... (truncated)")
    print(f"\nTotal lines: {len(lines)}")
    
    # Save to file
    output_file = "/tmp/example_start.sh"
    with open(output_file, "w") as f:
        f.write(content)
    
    print(f"\n✅ Saved to: {output_file}")
    print("   Run: chmod +x /tmp/example_start.sh && /tmp/example_start.sh help")


if __name__ == "__main__":
    main()
