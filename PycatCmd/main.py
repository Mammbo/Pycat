#imports 
import os
import subprocess
import time
import sys 
import platform
import hashid 

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
print(
    """   _____                _____                    _____                    _____                _____                  
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
                                                                                                                             """) 
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
            # print everything in charsets, rulles, and wordlists
            pass
        case "3":
            # upload various files to the charsets, rules, or wordlists directory so users can make their own. 
            pass
        case "4":
            # copy and paste a hash and have the program identify what type of hash it is 
            hashes = input('Enter hashes in quotes ("xxxxxx, xxxxxx", ......) or enter hashes file from inside the program: ')
            hashid.identify_hashes(hashes)
            
        case "5":
            # use crunch and cewl to munge wordlists together 
            pass
        case "6":
            # view potfile  
            pass
        case "7":
            sys.exit(0)
        case _:
            pass