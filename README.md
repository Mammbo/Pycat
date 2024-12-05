# Pycat
Python program to utilize hashcat and password cracking


TodoList: 

make a password cracker with python and hashcat to automate commmon word sets rulesets and attacks make it generate rulelists and wordlists(crunch and cewl)

make a gui and commandline version 

*GUI Design* 
[] : Main Window
[] : Pycat with SVG Logo 
[] : Hashcat Attack Tab
- [] File selection buttons: Hash file, wordlist, rules file.
- [] Dropdowns: Hash type, attack type.
- [] Start attack button.
- [] Terminal output display.
[] : Display cracked passwords in real-time.
[] : Word Munging Tab 
- Crunch and Cewl buttons.
[] : Potfile Viewer Tab
[] : Hash Identification Tab
- [] : Text box for manual input.
- [] : Button to identify hash.
- [] Display hash type result.

*Hashcat Attack* 
[] run_hashcat_attack(): Execute Hashcat with selected options from user selections.
[] display_output(): Append Hashcat output to GUI terminal.
[] add hashcat functionality like when you are running hashcat
(more buttons basically, and when you clicke them subprocess will execute something to do what you said)

*File Uploading*
[] file uploading(): opens up box for you to add files to the specific folders. 
File Handling Functions
[] select_hash_file(): Open file dialog to select a hash file.
[] select_wordlist(): Open file dialog for wordlist.
[] select_rules_file(): Open file dialog for rules.

Wordlist munging
[] run_crunch(min_len, max_len, charset): Generate custom wordlists with Crunch.
[] run_cewl(url): Scrape a website to generate a wordlist.

Hash Identification
[] identify_hash(hash_input): Use HashID to detect the hash type and display the result.

*Potfile Viewing* 
[] : reads hashcat potfile and displays results

[] pacakge binary to be run on every system
[] make a requirements.txt with python dependencies 
[] make a command-line version