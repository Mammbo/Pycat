#imports 
import os
import subprocess
import time
import sys 
import platform
import hashid 
import word_munging
import file_management

#Location of the wifi h2000 file
wificap= "Path\\To\\Wifi\\Capture"
# Directory where all the wordlist are located
wordlistdir = "Pycat/PycatCmd/Wordlists"
#Directory whee hashcat is located. Only for Windows users
hashcatdir = "Path\\To\\Password\\Hashcat"
#Directory where rules file ae located
rulesdir = "Pycat/PycatCmd/Rules"
#If for hashcat.hctune is located in a different directory than hashcat. This is needed if you get an error about hashtune is not found.
hashtunedir = ""
# Boolean value
displayresults = True


# Gettting the OS platform to make sure if we need to run exe in Windows.
plat = platform.system()

if plat == "Windows":
    hcat = "hashcat.exe"
else:
    hcat = "hashcat"

options = ["\nAvailable Options:", "1. Attack", "2. View Available Wordlists/Rules/Charsets", "3. Upload Files", "4. Hash Identification", "5. Wordlist Munging", "6. View Potfile", "7. Exit"]

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
            #hash cat attack and view the attack 
            pass
        case "2":
            file_management.list_files("PycatCmd/wordlists")
            file_management.list_files("PycatCmd/rules")
            file_management.list_files("PycatCmd/charsets")
            while True: 
                choice = input("Enter file to inspect or 0 to exit: ").strip()
                if choice != '0':
                    file_management.list_files("PycatCmd/wordlists")
                    file_management.list_files("PycatCmd/rules")
                    file_management.list_files("PycatCmd/charsets")
                    file_management.inspect_files(choice)
                elif choice == '0':
                    break 
                else:
                    print("invalid choice.")
        case "3":
            file_management.upload_files()
            pass
        case "4":
            # copy and paste a hash and have the program identify what type of hash it is 
            hashes = input('Enter hashes in quotes ("xxxxxx, xxxxxx", ......) or enter hashes file from inside the program: ')
            hashid.identify_hashes(hashes)
            
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
            pass
        case "7":
            sys.exit(0)
        case _:
            pass