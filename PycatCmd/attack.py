
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
                    
            with open(f"~/Pycat/PycatCmd/Passwd-hashes/hashes.txt", 'w') as f: 
                f.write("\n".join(str(line) for line in data) + "\n")

    except Exception as e: 
        print(f"An error occured {e}")


def remove_hashes():
    # read the file .split(\n), append everything to a list, zip that fiel with a for loop and print the index + 1 and the hash, have user input determine line number or index in this case, go to that line with the content save and store that content into a variable, then use this code, specifally the for loop. 
    
    with open("~/Pycat/PycatCmd/Passwd-hashes/hashes.txt", "r+" ) as f:
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


class Hashcat:
    def __init__(self):
        import subprocess
        import threading
        #tracks the state of the project
        self.process = None
        self.running = False
        #allows use of the imports whereever I want inside the class
        self.subprocess = subprocess
        self.threading = threading


    def start_hashcat(self, command):
        try:
            print(f"Starting Hashcat with command: {command}")
            # Start Hashcat process and stracks the input and output
            self.process = self.subprocess.Popen(
                command,
                stdin=self.subprocess.PIPE,
                stdout=self.subprocess.PIPE,
                stderr=self.subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            self.running = True
            # Start a thread to read Hashcat output
            self.threading.Thread(target=self._read_output, daemon=True).start()
        except Exception as e:
            print(f"Error starting Hashcat: {e}")

    def _read_output(self):
        #Continuously read output from the Hashcat process. 
        if self.process and self.process.stdout:
            for line in self.process.stdout:
                print(line, end="", flush=True)  # Print Hashcat output to console
        self.running = False

    def send_command(self, command):
        """ Send a command to the running Hashcat process. """
        if self.process and self.running:
            try:
                self.process.stdin.write(command + "\n")
                self.process.stdin.flush()
                print(f"Sent command: {command}")
            except Exception as e:
                print(f"Error sending command: {e}")
        else:
            print("Hashcat process is not running.")

    def stop_hashcat(self):
        # Terminate the Hashcat process. 
        if self.process:
            try:
                self.process.terminate()
                print("Hashcat process terminated.")
            except Exception as e:
                print(f"Error terminating Hashcat: {e}")
    #control hashcat will running           
    def hash_cat_controller(self):
        while self.running:
            user_input = input("Enter commands (status=p, pause=p, resume=r, quit=q): ").strip().lower()
            if user_input in ("p", "r", "b", "s", "q"):
                self.send_command(user_input)
            if user_input == "q":
                self.stop_hashcat()
                break

def hashcat_man():
    import subprocess
    man = subprocess.run(['hashcat', '--help'], stdout=subprocess.PIPE)
    print(man.stdout.decode())


def view_cracked_hashes():
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Construct the full path dynamically
    relative_path = "Passwd-hashes/cracked-hashes.txt"
    file_path = os.path.join(BASE_DIR, relative_path)

    # Attempt to read the file with error handling
    try:
        with open(file_path, 'r') as f:
            cracked_hashes = f.read()
            print(cracked_hashes)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # display file names one last time
#executing attack 
#display files, display whats in those files option 

# upload hashes
#im thinkgin for loop and print out all the lines of the hashes with their 1. xxxxxxsxxx, click that number and it will remove that hash by writing "" over it
# remove hashes
