import subprocess
def run_command(command): #reccoommended with help from microsoft copilot
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")

def main():
    run_command("flask run") 
    
if __name__ == "__main__":
    main()
