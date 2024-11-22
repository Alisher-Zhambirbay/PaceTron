import sys
import subprocess

def __is_win32__():
    return sys.platform == "win32"

def __install_modules__():
    p = 0
    command = []

    if __is_win32__():
        command = ["py", "-m", "pip", "install", "-r", "requirements.txt"]
    else:
        command = ["python3", "-m", "pip", "install", "-r", "requirements.txt"]

    try:
        print(f"Running command: {' '.join(command)}")

        subprocess.check_call(command)

        print("Dependencies installed successfully.")

        p = 1
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return p

def run():
    __c__ = (__install_modules__())
    
    if (__c__):
        try:
            from Programm import main
            main.run_pacetron()
        except ImportError as e:
            print(f"Error: unable to import main from Programm.\n{e}")
        except AttributeError as e:
            print(f"Error: The 'main' module does not contain 'run_pacetron' function: {e}")
        except KeyboardInterrupt: exit(1) #ignore this error.
    else:
        print("Cannot run PaceTron. Setup not was succesfull")

if __name__ == "__main__":
    run()