#!/usr/bin/env python3
"""Example: Basic logging operations."""

import time
from skills.cli_logger import Logger, LogLevel, configure, info, success, warning, error

def main():
    print("=" * 50)
    print("  CLI Logger - Basic Examples")
    print("=" * 50)
    
    # Create logger
    log = Logger("demo", level=LogLevel.TRACE)
    
    # All levels
    print("\n1. Log Levels:")
    log.trace("Trace message - very detailed")
    log.debug("Debug message - for debugging")
    log.info("Info message - general info")
    log.success("Success message - operation ok")
    log.warning("Warning message - attention needed")
    log.error("Error message - something failed")
    log.critical("Critical message - system failure")
    
    # With data
    print("\n2. With Extra Data:")
    log.info("User action", user="alice", action="login")
    log.warning("High usage", cpu="85%", memory="72%")
    log.error("Request failed", url="/api/data", status=500)
    
    # Timer
    print("\n3. Timed Operations:")
    with log.timer("Database query"):
        time.sleep(0.3)
    
    with log.timer("File processing"):
        time.sleep(0.5)
    
    # Sections
    print("\n4. Sections:")
    log.section("Application Startup")
    log.info("Loading configuration...")
    log.success("Configuration loaded")
    
    # Global logger
    print("\n5. Global Logger:")
    configure("myapp")
    info("Using global logger")
    success("Works great!")


if __name__ == "__main__":
    main()
