import sys
import pkg_resources
import os

def check_dependencies():
    print("Python version:", sys.version)
    print("Current working directory:", os.getcwd())
    
    required = {'Flask', 'gunicorn'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    
    if missing:
        print("Missing packages:", missing)
    else:
        print("All required packages are installed")
        print("\nInstalled versions:")
        for package in required:
            version = pkg_resources.get_distribution(package).version
            print(f"{package}: {version}")

if __name__ == "__main__":
    check_dependencies() 