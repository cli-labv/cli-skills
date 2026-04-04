#!/usr/bin/env python3
"""Example: Basic table operations."""

from skills.cli_tables import print_table, print_dict, print_key_value

# Sample data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "role": "Admin"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "role": "User"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "role": "User"},
]

def main():
    print("=" * 50)
    print("  CLI Tables - Basic Examples")
    print("=" * 50)
    
    # Basic table
    print("\n1. Basic Table:")
    print_table(users, title="Users")
    
    # Styled columns
    print("\n2. With Column Styles:")
    print_table(
        users,
        title="Team Members",
        column_styles={
            "name": "cyan bold",
            "role": "green",
            "email": "dim",
        }
    )
    
    # Dictionary
    print("\n3. Dictionary Display:")
    config = {
        "database": "postgresql",
        "host": "localhost",
        "port": 5432,
        "ssl": True,
    }
    print_dict(config, title="Database Config")
    
    # Key-value
    print("\n4. Key-Value Pairs:")
    print_key_value([
        ("Status", "✅ Running"),
        ("Uptime", "3 days"),
        ("Memory", "256 MB"),
        ("CPU", "12%"),
    ], title="System Status")


if __name__ == "__main__":
    main()
