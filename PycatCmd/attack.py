
def upload_hashes():
    #option selection
    print("Paste Hashes below, Press Enter to Finish: ")
    data = []
    try: 
        while True:
            line = input()
            if not line.strip(): 
                break
            data.append(line.strip())
                    
            with open(f"PycatCmd/Passwd-hashes/hashes.txt", 'w') as f: 
                f.write("\n".join(str(line) for line in data) + "\n")

    except Exception as e: 
        print(f"An error occured {e}")


def remove_hashes():
    # read the file .split(\n), append everything to a list, zip that fiel with a for loop and print the index + 1 and the hash, have user input determine line number or index in this case, go to that line with the content save and store that content into a variable, then use this code, specifally the for loop. 
    
    with open("PycatCmd/Passwd-hashes/hashes.txt", "r+" ) as f:
        lines = f.readlines()           # Get a list of all lines                     
    
        for line_num, data in enumerate(lines):
            print(f"{line_num + 1}: {data.replace('\n', '')}")
            
        try: 

    
            delete_hash = int(input("Inpute Line Number to delete: ")) - 1
            
            if 0 <= delete_hash < len(lines):
                lines.pop(delete_hash)
    
                f.seek(0)
                f.truncate()                    # Stop processing now                         
                                                # because len(file_lines) > len( lines ) 
                f.writelines(lines)           # write back
            else: 
                print("invalid Line number!")
        
        except ValueError:
            print("Enter Valid Number")

def attack():
    pass

def hashcat_man():
    import subprocess
    man = subprocess.run(['hashcat', '--help'], stdout=subprocess.PIPE)
    print(man.stdout.decode())

def view_cracked_hashes():
    pass

    # display file names one last time
#executing attack
#display files, display whats in those files option 

# upload hashes
#im thinkgin for loop and print out all the lines of the hashes with their 1. xxxxxxsxxx, click that number and it will remove that hash by writing "" over it
# remove hashes
