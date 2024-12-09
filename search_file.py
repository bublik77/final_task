import os
import fnmatch
import platform
import sys

def get_os_type():
    os_type = platform.system()
    return os_type

def get_default_directory(os_type):
    if os_type == "Windows":
        user_name = os.environ.get("USERNAME")
        return f"C:\\Users\\{user_name}"
    elif os_type == "Linux":
        user_name = os.environ.get("USERNAME")
        return f"/home/{user_name}"
    elif os_type == "Darwin":
        user_name = os.environ.get("USERNAME")
        return f"/home/{user_name}"
    else:
        return "/"

def check_sudo():
    if platform.system() == "Linux":
        if os.geteuid() != 0:
            print("Warning: if you need access to the root / directory run this script with sudo.")
            print("If you want to continue press any key, but if you want to stop please type stop")
            answer = input()
            if answer == 'stop':
                sys.exit()

def search_files(start_directory, search_word="*"):
    found_files = []
    
    for root, dirs, files in os.walk(start_directory):
        for file in files:
            if fnmatch.fnmatch(file, search_word):
                found_files.append(os.path.join(root, file))

    return found_files

def display_files(file_list):
    if not file_list:
        print("Any file(s) found.")
    else:
        print(f"Found {len(file_list)} file(s):")
        for file in file_list:
            print(file)

def main():
    os_type = get_os_type()
    print(f"Operating System is: {os_type}")

    if os_type == "Linux":
        check_sudo()

    if len(sys.argv) < 2:
        default_directory = get_default_directory(os_type)
        print(f"Default directory: {default_directory}")
        search_word = input("Enter word to search(*.txt or file_name): ")
        start_directory = input(f"Enter in which directory to search(by default: {default_directory}): ") or default_directory
    elif len(sys.argv) > 0 and len(sys.argv) < 2:
        print("You should use search_file.py \"directory\" file_name")
        sys.exit()
    else:
        start_directory = sys.argv[1]
        search_word = sys.argv[2]


    if not os.path.isdir(start_directory):
        print(f"The directory {start_directory} does not exist or is not accessible.")
        return

    found_files = search_files(start_directory, search_word)

    display_files(found_files)

if __name__ == "__main__":
    main()