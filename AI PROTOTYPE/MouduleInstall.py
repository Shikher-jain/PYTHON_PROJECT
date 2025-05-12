import subprocess
import sys

def check(package_name):
    try:
        __import__(package_name)  # Try to import the package
        print(f"'{package_name}' is already installed.")
    except ImportError:
        print(f"'{package_name}' is not installed. Installing now...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"'{package_name}' has been installed successfully!")
        except subprocess.CalledProcessError:
            print(f"Failed to install '{package_name}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__=="__main__":
    check("sys")  # Replace 'requests' with the module you want to check/install
