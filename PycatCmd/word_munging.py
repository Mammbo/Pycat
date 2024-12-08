# as far as i know you can not use either of these in windows only in linux and mac 
def cewl_munging(url, wordlist_name):
    import subprocess
    import datetime
    
    date = datetime.datetime.now()
    date = date.strftime("%m-%d-%Y")

    help_menu = (subprocess.run(["cewl", "-h"], stdout=subprocess.PIPE))
    print(help_menu.stdout.decode())

    #ask for file name 
    options = input('input parameters for cewl like ("xxx,xxx,xxx"): ')
    full_cmd = ["cewl"] + options.replace('"', "").split(",")
    full_cmd.append(url.replace('"', ""))
    #results = subprocess.run(['cewl', "-e", "-m", "-j",  hashes.replace('"', "").replace(",", "")], stdout=subprocess.PIPE)

    #run cewl print output to the screen 

    try:
        print("running.......")
        output = subprocess.run(full_cmd, stdout=subprocess.PIPE)
        words = output.stdout.decode()
        wordlist = words.split("\n", 1)[1]
        print(wordlist)

        with open(f"PycatCmd/Wordlists/Custom/{wordlist_name}-{date}.txt", 'w') as f: 
            f.write(wordlist)

    except Exception as e:
        print(f"An error occurred: {e}")

    #have output piped into a file 
    # make a file in wordlists/custom with the file name and time where they can use their wordlists 

def crunch_munging():
    import subprocess
    import os
    import datetime

    date = datetime.datetime.now()
    date = date.strftime("%m-%d-%Y")

    help_menu = (subprocess.run(["man", "crunch"], stdout=subprocess.PIPE))
    print(help_menu.stdout.decode())

    list_charsets = input("list charsets?(y/n): ")

    if list_charsets == 'y':
        charset_dir = "PycatCmd/charsets/"
        all_charsets = {}

        # Traverse the directory structure and collect files for each directory
        for root, dirs, files in os.walk(charset_dir):
            relative_dir = os.path.relpath(root, charset_dir)

            # Skip the base directory if it contains no files
            if relative_dir == ".":
                continue

            # Store the files in the dictionary only if the directory contains files
            if files:
                all_charsets[relative_dir] = files

        # Calculate the maximum length for directory and filenames to ensure even spacing
        max_dir_len = max(len(dir_name) for dir_name in all_charsets.keys())
        max_file_len = max(len(file) for files in all_charsets.values() for file in files)

        # Create the header row with evenly spaced columns
        header = f"{'charset dir'.ljust(max_dir_len)} | " + " | ".join([f"{'charsets'.ljust(max_file_len)}"] * 4)
        print(header)
        print("-" * len(header))  # Separator line to match the length of the header

        # Print each directory with its files, ensuring even spacing
        for dir_name, files in all_charsets.items():
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


# actualy crunch functionality 

        wordlist_name = input("enter wordlist name: ")
        options = input('\ninput parameters for crunch like ("xxxx,xxxxx" for ----> <min-len> <max-len> [PycatCmd/charsets/<charset dir/charset>] [options]): ')
        full_cmd = ["crunch"] + options.replace('"', "").split(",")

        try:
            print("running.......")
            output = subprocess.run(full_cmd, stdout=subprocess.PIPE)
            words = output.stdout.decode()
            #wordlist = words.split("\n", 1)[1]
            print(words)

            with open(f"PycatCmd/Wordlists/Custom/{wordlist_name}-{date}.txt", 'w') as f: 
                f.write(words)

        except Exception as e:
            print(f"An error occurred: {e}")

    else: 

        wordlist_name = input("enter wordlist name: ")
        options = input('\ninput parameters for crunch like ("xxxx,xxxxx" for ----> <min-len> <max-len> [PycatCmd/charsets/<charset dir/charset>] [options]): ')
        full_cmd = ["crunch"] + options.replace('"', "").split(",")

        try:
            print("running.......")
            output = subprocess.run(full_cmd, stdout=subprocess.PIPE)
            words = output.stdout.decode()
            #wordlist = words.split("\n", 1)[1]
            print(words)

            with open(f"PycatCmd/Wordlists/Custom/{wordlist_name}-{date}.txt", 'w') as f: 
                f.write(words)

        except Exception as e:
            print(f"An error occurred: {e}")


