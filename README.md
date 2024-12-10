# Pycat

A Python wrapper for Hashcat that allows full password cracking capablitlities all in one spot, including word list creation, managing files, hashcat attacks, and hash identification.

# Prequisites

There are a few prequisites that you will need. Those are:

- Install Python
- Install Hashcat
- Install Crunch and Cewl (Linux and Mac Only)
- Install Python dependencies

## Installing Python
Python.org has a Wiki page that is best on how to install Python itself. 

[Python Install Docs](https://wiki.python.org/moin/BeginnersGuide/Download)

## Installing Hashcat

### Windows(Currently not supported havent added the couple lines of code will do soon):
Download the 7zip that contains everything you need from [Hashcat's website](https://hashcat.net/hashcat/). Once the files are downloaded, extract them. In the directory that the files were extracted to there will be a hashcat.exe file.

### Linux
Install Hashcat with your local repo manager.  For Debian users, such as Kali, Ubuntu, etc use the following:
```
sudo apt install hashcat
```

### MacOS
Install Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Then install Hashcat 
```
brew install hashcat
```

## Installing Crunch 

### Linux 
Install Crunch with your local repo manager. For Debian users, such as Kali, Ubuntu, etc use the following: 

```
sudo apt install crunch
```
### MacOS 

Install Crunch: 

```
brew install crunch
```
## Installing Cewl

### Linux 
Install Cewl with you local repo manager. For Debian Users, such as Kali, Ubuntu, etc use the following: 

```
sudo apt install cewl 
```
### MacOS

Follow the Installation guide on the Repo: [https://github.com/digininja/CeWL/?tab=readme-ov-file]

Rename the Executable after: 

```
mv ./cewl.rb cewl 
```

Turn into a binary: 
```
sudo mv cewl /usr/local/bin
```

## Install Python Dependencies

Install hashid: 

```
pip install hashid
```

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
[] make window either automatically resize or disable it 


------------------------------------------------------------

*CMD Program* 
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

*Hashcat Attack* 
[] run_hashcat_attack(): Execute Hashcat with selected options from user selections.
[] add hashcat functionality like when you are running hashcat
(more buttons basically, and when you clicke them subprocess will execute something to do what you said)