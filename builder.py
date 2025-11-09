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
def run_command(command): #reccoommended with help from microsoft copilot
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

def main():
    run_command("python Webscraper/webscraper.py") #run the webscraper first
    run_command("node db-setup/parser.js") #setup the database first
    run_command("node db-setup/updateDB.js") #update the database last

if __name__ == "__main__":
    main()




