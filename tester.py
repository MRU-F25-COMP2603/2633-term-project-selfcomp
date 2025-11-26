'''
Testing script for the SelfCOMP test suites

Purpose: Runs pytest and jest tests
Usage: Running python tester.py
'''
from builder import run_command

def main():
    run_command("npm test")
    run_command("pytest -v")

if __name__ == "__main__":
    main()
