### list all avaiable files ### 

def inspect_files(requested_file):
    try:
        with open(requested_file, 'r') as f:
            contents = f.read()
        print(f"Contents of {requested_file}: \n{contents}\n")
    except FileNotFoundError:
        print(f"Error: File '{requested_file}' not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_files(requested_dir):
    import os 
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Map for directories and their labels
    dir_map = {
        "wordlists": ("PycatCmd/wordlists", "Wordlist Directory", "Wordlists"),
        "rules": ("PycatCmd/rules", "Rules Directory", "Rules"),
        "charsets": ("PycatCmd/charsets", "Charset Directory", "Charsets"),
        "masks": ("PycatCmd/masks", "Masks Directory", "Masks"),
    }

    # Validate requested directory
    if requested_dir not in dir_map:
        return

    # Unpack details for the requested directory
    relative_path, directory_label, file_label = dir_map[requested_dir]

    # Dynamically adjust the base path to avoid duplicate nesting
    if "PycatCmd" in os.path.basename(BASE_DIR):
        path = os.path.join(BASE_DIR, relative_path.replace("PycatCmd/", ""))
    else:
        path = os.path.join(BASE_DIR, relative_path)

    # Check if the directory exists
    if not os.path.exists(path):
        print(f"Error: The directory {path} does not exist.")
        return

    # Initialize a dictionary to hold files by directory
    all_files = {}

    # Traverse the directory structure and collect files
    for dirpath, dirnames, filenames in os.walk(path):
        if filenames:
            all_files[dirpath] = filenames

    # Check if any files were found
    if not all_files:
        print(f"No files found in {path}.")
        return

    # Calculate maximum lengths for even formatting
    max_dir_len = max(len(dir_name) for dir_name in all_files.keys())
    max_file_len = max(len(file) for files in all_files.values() for file in files)

    # Print header
    header = f"{directory_label.ljust(max_dir_len)} | {file_label.ljust(max_file_len)}"
    print(header)
    print("-" * len(header))

    # Print files grouped by directory
    for dir_name, files in all_files.items():
        # Split the files into chunks for better formatting
        file_chunks = [files[i:i + 4] for i in range(0, len(files), 4)]

        for i, chunk in enumerate(file_chunks):
            if i == 0:
                row = [f"{dir_name.ljust(max_dir_len)}"] + [f"{file.ljust(max_file_len)}" for file in chunk]
            else:
                row = [" " * max_dir_len] + [f"{file.ljust(max_file_len)}" for file in chunk]
            print(" | ".join(row))

    print("\n")

#make a function to inspect the contents of a file and print it out to the console then have everything reprint with the option pop back up again

### upload files ### 
#wget file 
# mv file on the system 
#create a file and copy and paste data 

def upload_files():
    import subprocess
    import shutil
    import datetime
    import os 

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    date = datetime.datetime.now()
    date = date.strftime("%m-%d-%Y")

    print("\nOptions: \n1. Wget File\n2. Move File on System\n3. Create a file and Copy Paste data")
    choice = input("Enter Option: ").strip()
    file_type = input("Enter what file type (Wordlist, Rule, Charset, Mask): ").strip().lower()
    
    # File type directory and extension mapping
    save_directory = None
    file_extension = None
    
    try:
        if file_type == "wordlist":
            save_directory = f"{BASE_DIR}/wordlists/custom"
            file_extension = ".txt"
        elif file_type == "rule":
            save_directory = f"{BASE_DIR}/rules/custom"
            file_extension = ".rule"
        elif file_type == "charset":
            save_directory = f"{BASE_DIR}/charsets/custom"
            file_extension = ".char"
        elif file_type == "mask":
            save_directory = f"{BASE_DIR}/masks/custom"
            file_extension = ".hcmask"
        else:
            print("Invalid file type. Please select from Wordlist, Rule, Charset, or Mask.")
            return

        # Create the directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)
    
    except Exception as e: 
        print(f"An exception occurred while setting up directories: {e}")
        return

    # Option selection
    try: 
        if choice == "1":  # wget functionality
            wget_url = input("Enter wget URL: ").strip()
            subprocess.run(['wget', "-P", save_directory, wget_url], stdout=subprocess.PIPE)
            print(f"File downloaded to {save_directory}")

        elif choice == "2":  # Move file on system
            file_location = input("Enter path of file to move: ").strip()
            shutil.move(file_location, save_directory)
            print(f"File moved to {save_directory}")

        elif choice == "3":  # Create file and copy-paste data
            file_name = input("Enter name of file: ").strip()
            if file_name:
                print("Paste data below. Press Enter to finish:")
                data = []
                try: 
                    while True:
                        line = input()
                        if not line.strip():
                            break
                        data.append(line.strip())
                    
                    # Save the file with the appropriate extension
                    file_path = f"{save_directory}/{file_name}-{date}{file_extension}"
                    with open(file_path, 'w') as f: 
                        f.write("\n".join(data) + "\n")
                    
                    print(f"File saved as {file_path}")
                
                except Exception as e: 
                    print(f"An error occurred while saving the file: {e}")
        else:
            print("Invalid option. Please select 1, 2, or 3.")

    except Exception as e:
        print(f"An error occurred: {e}")

