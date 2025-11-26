'''
builder.py
References: https://www.geeksforgeeks.org/python/executing-shell-commands-with-python/

This is the builder for the SelfCOMP project to be run simply as `python builder.py`
This builder is safe to execute multiple times without issues. Repeat entries will be ignored.

Steps taken:
1. run webscraper to get data
2. run parser.js to parse data and export a json
3. run updateDB.js to update the database with the new json
'''

import subprocess
import sys

#runs a shell command and handles errors
import subprocess
import sys

def run_command(cmd): #build using micosoft copilot
    try:
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True, check=True)
        print(f"Success: {cmd}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        print(f"Exit code: {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while running {cmd}: {e}")
        sys.exit(1)


def main():
    # first install dependencies
    run_command("npm install")
    run_command("pip install -r requirements.txt")

    #FOR THE BETA RELEASE: the updater does not clear duplicates, so please clear the database first
    run_command("node db-setup/clearDB.js")

    #next run the scraper, parser and updater to setup the database
    run_command("python webscraper/webscraper.py")
    run_command("node db-setup/parser.js")
    run_command("node db-setup/schedules.js")
    run_command("node db-setup/updateDB.js")

if __name__ == "__main__":
    main()




