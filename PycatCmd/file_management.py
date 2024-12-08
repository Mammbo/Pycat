### list all avaiable files ### 

def list_files(requested_dir):
        import os

        if requested_dir == "PycatCmd/wordlists":
            path = "PycatCmd/wordlists/"
            directory = "Wordlist Directory"
            file = "Wordlists"
        elif requested_dir == "PycatCmd/rules":
            path = "PycatCmd/rules/"
            directory = "Rules Directory"
            file = "Rules"
        elif requested_dir == "PycatCmd/charsets":   
            path = "PycatCmd/charsets/"
            directory = "Charset Dictonary"
            file = "Charsets"

        all_files = {}
        # Traverse the directory structure and collect files for each directory
        for root, dirs, files in os.walk(requested_dir):
            relative_dir = os.path.relpath(root, requested_dir)

            # Skip the base directory if it contains no files
            if relative_dir == ".":
                continue

            # Store the files in the dictionary only if the directory contains files
            if files:
                all_files[path + relative_dir] = files

        # Calculate the maximum length for directory and filenames to ensure even spacing
        max_dir_len = max(len(dir_name) for dir_name in all_files.keys())
        max_file_len = max(len(file) for files in all_files.values() for file in files)

        # Create the header row with evenly spaced columns
        header = f"{directory.ljust(max_dir_len)} | " + " | ".join([f"{file.ljust(max_file_len)}"] * 4)
        print(header)
        print("-" * len(header))  # Separator line to match the length of the header

        # Print each directory with its files, ensuring even spacing
        for dir_name, files in all_files.items():
            # Split the list of files into groups of 4
            file_chunks = [files[i:i + 4] for i in range(0, len(files), 4)]

            # Print the directory name only once for each set of file rows
            for i, chunk in enumerate(file_chunks):
                if i == 0:
                    # Print the directory name with the first row of files
                    row = [f"{dir_name.ljust(max_dir_len)}"] + [f"{file.ljust(max_file_len)}" for file in chunk]
                    print(" | ".join(row))
                else:
                    # Indent subsequent rows with files only
                    row = [" " * max_dir_len] + [f"{file.ljust(max_file_len)}" for file in chunk]
                    print(" | ".join(row))
        print("\n")
### upload files ### 
#wget file 
# mv file on the system 
#create a file and copy and paste data 

def upload_files():
    import subprocess
    print("\nOptions: \n1. Wget File\n2. Move File on System\n3. Create a file and Copy Paste data")
    choice = input("Enter Option: ")
    file_type = input("Enter what file type (Wordlist, Rule, Charset): ").lower()
    
    #file_type dir'
    try:
        if file_type == "wordlist":
            save_directory = "PycatCmd/wordlists/custom"
        elif file_type == "rule":
            save_directory = "PycatCmd/rules/custom"
        elif file_type == "charset":
            save_directory = "PycatCmd/charsets/custom"
    except Exception as e: 
        print(f"An exception occurred: {e}")
        

    #option selection
    try: 
        if choice == "1":
            wget_url = input("enter wget url: ")
            subprocess.run(['wget', "-P", save_directory, wget_url], stdout=subprocess.PIPE)

        elif choice == "2":
            pass
        elif choice == "3":
            pass
    except Exception as e:
            print(f"An error occurred: {e}")

upload_files()