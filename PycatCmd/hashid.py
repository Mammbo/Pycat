def identify_hashes(hashes):
    import subprocess
#init HashID
# make sure to put this in the main.py
# identify if user inputed a file or multiple hashes, if just one hash its fine 
    if "" or '' in hashes:
        results = hashes.split(",")
    
        try: 
            #loop through the list that was split & run the hashid command with the args, prints out result 
            for hashes in results:
                results = subprocess.run(['hashid', "-e", "-m", "-j",  hashes.replace('"', "").replace(",", "")], stdout=subprocess.PIPE)
                print(results.stdout.decode())
            
        except FileNotFoundError:
            print(f"Error: File not found - {hashes}")
        except Exception as e:
            print(f"An error occurred: {e}")
                
    else: 
        try:
            results = subprocess.run(['hashid', "-e", "-m", "-j",  hashes], stdout=subprocess.PIPE)
            print(results.stdout.decode())
        
        except FileNotFoundError:
            print(f"Error: File not found - {hashes}")
        except Exception as e:
            print(f"An error occurred: {e}")


