#imports 
import sys 
import platform
import hashid 
import word_munging
import file_management
import attack

# Gettting the OS platform to make sure if we need to run exe in Windows.
plat = platform.system()

if plat == "Windows":
    hcat = "hashcat.exe"
else:
    hcat = "hashcat"

options = ["\nAvailable Options:", "1. Attack", "2. View Available Wordlists/Rules/Charsets/Masks", "3. Upload Files", "4. Hash Identification", "5. Wordlist Munging", "6. View Potfile", "7. Exit"]

# Pycat ASCII Art along with the several options needed 
title = r"""
          _____                _____                    _____                    _____                _____          
         /\    \              |\    \                  /\    \                  /\    \              /\    \         
        /::\    \             |:\____\                /::\    \                /::\    \            /::\    \        
       /::::\    \            |::|   |               /::::\    \              /::::\    \           \:::\    \       
      /::::::\    \           |::|   |              /::::::\    \            /::::::\    \           \:::\    \      
     /:::/\:::\    \          |::|   |             /:::/\:::\    \          /:::/\:::\    \           \:::\    \     
    /:::/__\:::\    \         |::|   |            /:::/  \:::\    \        /:::/__\:::\    \           \:::\    \    
   /::::\   \:::\    \        |::|   |           /:::/    \:::\    \      /::::\   \:::\    \          /::::\    \   
  /::::::\   \:::\    \       |::|___|______    /:::/    / \:::\    \    /::::::\   \:::\    \        /::::::\    \  
 /:::/\:::\   \:::\____\      /::::::::\    \  /:::/    /   \:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \ 
/:::/  \:::\   \:::|    |    /::::::::::\____\/:::/____/     \:::\____\/:::/  \:::\   \:::\____\    /:::/  \:::\____\
\::/    \:::\  /:::|____|   /:::/~~~~/~~      \:::\    \      \::/    /\::/    \:::\  /:::/    /   /:::/    \::/    /
 \/_____/\:::\/:::/    /   /:::/    /          \:::\    \      \/____/  \/____/ \:::\/:::/    /   /:::/    / \/____/ 
          \::::::/    /   /:::/    /            \:::\    \                       \::::::/    /   /:::/    /          
           \::::/    /   /:::/    /              \:::\    \                       \::::/    /   /:::/    /           
            \::/____/    \::/    /                \:::\    \                      /:::/    /    \::/    /            
             ~~           \/____/                  \:::\    \                    /:::/    /      \/____/             
                                                    \:::\    \                  /:::/    /                           
                                                     \:::\____\                /:::/    /                            
                                                      \::/    /                \::/    /                             
                                                       \/____/                  \/____/                              
                                                                                                                     
                                
"""
print(title)

while True: 
    # prints all the options 
    for i in options:
        print("{}".format(i))
    option = input("\nChoice: ")
    match option:
        case "1":
            #atttack
            while True: 
                #hash cat attack and view the attack
                print("\nHashcat Cracking Options:\n1. Attack\n2. Upload Hashes\n3. Remove Hashes\n4. Hashcat Manual\n5. List Files\n6. Exit")
                option = input("\nChoice: ").strip()
                if option == '1':
                    hashcat = attack.Hashcat()

                    hash_type = input("Enter Hash Type: ")
                    attack_type = input("\nAttack Modes:\n1. -a 0 Straight\n2. -a 1 Combination attack\n3. Brute-force\n4. Hybrid Wordlist + Mask\n5. Hybrid Mask + Wordlist\nChoice: ").strip()

                    if attack_type == '1':
                        attack_type = '0'
                        wordlist = input('Path to Wordlist: ')
                        
                        rulesCheck = input("Do you want to use rules? (y/n): ").lower().strip()

                        if rulesCheck == 'y':
                            rule1 = input('Enter Rules 1: ')
                            rule2 = input('Enter Rules 2: (click enter for nothing): ')
                            if rule2 == '':
                                hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type,  # Hash type (e.g., MD5)
                                    "-a", attack_type,  # Attack mode (e.g., dictionary)
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt",  # Input hash file
                                    "-r", rule1,
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                                    
                                ]
                                hashcat.start_hashcat(hashcat_cmd)
                                hashcat.hash_cat_controller()
                            else: 
                                hashcat_cmd = [ 
                                    "hashcat", 
                                    "-m", hash_type, 
                                    "-a", attack_type, 
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt", 
                                    "-r", rule1, 
                                    "-r", rule2,
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                                ]
                                hashcat.start_hashcat(hashcat_cmd)
                                hashcat.hash_cat_controller()
                        elif rulesCheck == 'n':
                            # Example Hashcat command (adjust as needed)
                            hashcat_cmd = [
                                "hashcat",
                                "-m", hash_type,  # Hash type (e.g., MD5)
                                "-a", attack_type,  # Attack mode (e.g., dictionary)
                                "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt",  # Input hash file
                                wordlist,
                                '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                                
                            ]
                            hashcat.start_hashcat(hashcat_cmd)
                            hashcat.hash_cat_controller()
                        else: 
                            print("Invalid input: ")\

                    if attack_type == '2':
                        attack_type = '1'
                        wordlist1 = input('Path to Wordlist: ')
                        wordlist2 = input('Path to Wordlist2: ')

                        hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type,  # Hash type (e.g., MD5)
                                    "-a", attack_type,  # Attack mode (e.g., dictionary)
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt",  # Input hash file
                                    wordlist1, wordlist2,
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt'                                 
                                ]
                        hashcat.start_hashcat(hashcat_cmd)
                        hashcat.hash_cat_controller()
                    if attack_type =='3':
                        attack_type = '3'

                        incrementCheck = input("Do you want to increment attack ?(y/n): ")
                        if incrementCheck == 'y':
                            mask = input('Enter mask or mask file: ')
                            hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type,  # Hash type (e.g., MD5)
                                    "-a", attack_type,  # Attack mode (e.g., dictionary)
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt",  # Input hash fil
                                    mask, '--increment',
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                            ]
                            hashcat.start_hashcat(hashcat_cmd)
                            hashcat.hash_cat_controller()
                        elif incrementCheck == 'n':
                            mask = input('Enter mask or mask file: ')
                            hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type,  # Hash type (e.g., MD5)
                                    "-a", attack_type,  # Attack mode (e.g., dictionary)
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt",  # Input hash fil
                                    mask,
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                            ]
                            hashcat.start_hashcat(hashcat_cmd)
                            hashcat.hash_cat_controller()
                        else: 
                            print("Invalid Input")

                    if attack_type =='4':
                        attack_type = '6'
                        incrementCheck = input("Do you want to increment attack ?(y/n): ")
                        if incrementCheck == 'y':
                            mask = input('Enter mask or mask file: ')
                            wordlist = input('Enter Wordlist: ')

                            hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type,  
                                    "-a", attack_type,  
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt", 
                                    wordlist, mask, '--increment',
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                            ]
                            hashcat.start_hashcat(hashcat_cmd)
                            hashcat.hash_cat_controller()
                        elif incrementCheck == 'n':
                            mask = input('Enter mask or mask file: ')
                            wordlist = input('Enter Wordlist: ')

                            hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type,  
                                    "-a", attack_type,  
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt", 
                                    wordlist, mask,
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                            ]
                            hashcat.start_hashcat(hashcat_cmd)
                            hashcat.hash_cat_controller()
                    if attack_type =='5':
                        attack_type = '7'
                        incrementCheck = input("Do you want to increment attack ?(y/n): ")
                        if incrementCheck == 'y':
                            mask = input('Enter mask or mask file: ')
                            wordlist = input('Enter Wordlist: ')

                            hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type ,  
                                    "-a", attack_type,  
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt", 
                                    mask, wordlist, '--increment',
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                            ]
                            hashcat.start_hashcat(hashcat_cmd)
                            hashcat.hash_cat_controller()
                        elif incrementCheck == 'n':
                            mask = input('Enter mask or mask file: ')
                            wordlist = input('Enter Wordlist: ')

                            hashcat_cmd = [
                                    "hashcat",
                                    "-m", hash_type,  
                                    "-a", attack_type,  
                                    "~/Pycat/PycatCmd/Passwd-hashes/hashes.txt", 
                                    mask, wordlist,
                                    '-o', '~/Pycat/PycatCmd/Passwd-hashes/cracked-hashes.txt' 
                            ]

                            hashcat.start_hashcat(hashcat_cmd)
                            hashcat.hash_cat_controller()

                    # Allow user interaction
                                #upload hashes
                elif option == '2':
                    attack.upload_hashes()
                                #remove hashes
                elif option == '3':
                     attack.remove_hashes()
                                #hashcat man page
                elif option == '4':
                    attack.hashcat_man()
                elif option == '5':
                    file_management.list_files("~/Pycat/PycatCmd/wordlists")
                    file_management.list_files("~/Pycat/PycatCmd/rules")
                    file_management.list_files("~/Pycat/PycatCmd/charsets")
                elif option == '6':
                    break
                else: 
                    print("Invalid Choice")
                    
        case "2":
            # Call list_files for each subdirectory
            sub_dirs = ["wordlists", "rules", "charsets", "masks"]

            for sub_dir in sub_dirs:
                file_management.list_files(sub_dir)
            
            while True: 
                choice = input("Enter file to inspect or 0 to exit: ").strip()
                if choice == '0':
                    break
                else:
                    # Re-display the list of files
                    for sub_dir in sub_dirs:
                        file_management.list_files(sub_dir)
                    file_management.inspect_files(choice)
        case "3":
            file_management.upload_files()
        case "4":
            # copy and paste a hash and have the program identify what type of hash it is 
            import os 
            BASE_DIR = os.path.abspath(os.path.dirname(__file__))
            try: 
                hashes_file = f"{BASE_DIR}/Passwd-hashes/hashes.txt"
                print('\nOptions:')
                choice = input('1. Paste Hashes\n2. Identify Hashes from hashes.txt\nChoice: ')
                if choice == "1": 
                    hashes = input('Enter hashes in quotes ("xxxxxx, xxxxxx, ......): ')
                    hashid.identify_hashes(hashes)
                elif choice == "2":
                    hashid.identify_hashes(hashes_file)   

            except Exception as e:
                print(f"An exception occured: {e}")
                
        case "5":
            # use crunch and cewl to munge wordlists together
            try: 
                choice = input("crunch(1) or cewl(2)?: ")
                if choice == "1":
                    word_munging.crunch_munging()

                elif choice =="2":
                    url = input("paste url to scrape from: ")
                    wordlist = input("wordlist name: ")
                    word_munging.cewl_munging(url, wordlist)

            except Exception as e:
                print(f"An error occurred: {e}")
            
        case "6":
            # view potfile  
            attack.view_cracked_hashes()
        case "7":
            sys.exit(0)
        case _:
            pass