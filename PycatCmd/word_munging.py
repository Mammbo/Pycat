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
    import file_management
    import datetime

    date = datetime.datetime.now()
    date = date.strftime("%m-%d-%Y")

    help_menu = (subprocess.run(["man", "crunch"], stdout=subprocess.PIPE))
    print(help_menu.stdout.decode())

    list_charsets = input("list charsets?(y/n): ")

    if list_charsets == 'y':
        file_management.list_files("PycatCmd/charsets")
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


