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

#runs a shell command and handles errors
def run_command(command): #written with help from microsoft copilot
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

def main():
    # first install dependencies
    run_command("npm install")
    run_command("pip install -r requirements.txt")

    #FOR THE BETA RELEASE: the updater does not clear duplicates, so please clear the database first
    run_command("node db-setup/clearDB.js")
    run_command("I WANT TO DELETE ALL COURSES")

    #next run the scraper, parser and updater to setup the database
    run_command("python webscraper/webscraper.py")
    run_command("node db-setup/parser.js")
    run_command("node db-setup/updateDB.js")

if __name__ == "__main__":
    main()




