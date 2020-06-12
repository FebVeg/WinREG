import os
import subprocess
import sys
import time
import re

os.system("cls") # pulisco CMD

print("Register Key Finder & Destroyer - Version: 1.0beta\n")

username = os.getlogin() # Username Info
workDir = os.path.dirname(os.path.abspath(__file__)) + "\\" # WorkDire Info 
hostname = os.environ['COMPUTERNAME']

print("Version: 1.0alpha")
print("Username: " + username)
print("Target: " + hostname)
print("Working Directory: " + workDir)

searchKeys = input('Type a string that you want search: ')
searchSoftware = input("Need to search a program? [y/n]: ")

outputKeysNameHKLM = "regKeysHKLM_" + searchKeys + ".txt"
outputKeysNameHKCU = "regKeysHKCU_" + searchKeys + ".txt"

if searchSoftware == "y":
    searchSoftware = "\\Software"
elif searchSoftware == "n":
    searchSoftware = ""

if os.path.exists(workDir + outputKeysNameHKLM) and os.path.exists(workDir + outputKeysNameHKCU):
    print("File already existing")
    remove = input("Remove? [y/n]: ")
    if remove == "y":
        try:
            os.remove(workDir+outputKeysNameHKCU)
            os.remove(workDir+outputKeysNameHKLM)
        except Exception as error:
            print(error)
            print("Please, ignore this error, don't worry :)")
            
    elif remove == "n":
        sys.exit()
    else:
        print("Error")
        sys.exit()

print("Output file: " + workDir + outputKeysNameHKLM.replace('"', ''))

# Genero il comando CMD
cmdHKLM = 'REG Query HKLM%s /F %s /S > %s%s' % (searchSoftware, searchKeys, workDir, outputKeysNameHKLM)
cmdHKCU = 'REG Query HKCU%s /F %s /S > %s%s' % (searchSoftware, searchKeys, workDir, outputKeysNameHKCU)

# Inizio comando CMD
try: 
    print("\nSearching %s on HKLM.... Wait...." % (searchKeys))
    os.system(cmdHKLM)
    print("Done")
    print("\nSearching %s on HKCU.... Wait...." % (searchKeys))
    os.system(cmdHKCU)
    print("Done\n")
except Exception as error:
    print(error)  
# Fine comando CMD

# Edito il file di output e lo riscrivo senza nuove linee e spazi
#wait = input("Press [ENTER] to continue")

outputKeysNameHKCU = outputKeysNameHKCU.replace('"', '')
outputKeysNameHKLM = outputKeysNameHKLM.replace('"', '')

try:
    output_file_remastered = os.path.splitext(os.path.basename(outputKeysNameHKLM))[0] + "_mod.txt"
    keys = open(workDir + outputKeysNameHKLM).readlines()
    for line in keys:
        if line.startswith('HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print("Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue

        if line.startswith('    HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print("Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue
    a1 = "New output file: " + output_file_remastered
except Exception as error:
    print(error)

try:
    output_file_remastered = os.path.splitext(os.path.basename(outputKeysNameHKCU))[0] + "_mod.txt"
    keys = open(workDir + outputKeysNameHKCU).readlines()
    for line in keys:
        if line.startswith('HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print("Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue

        if line.startswith('    HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print("Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue
        
    a2 = "New output file: " + output_file_remastered

    try:
        new_file.close()
        print("Output saved: " + a1)
        print("Output saved: " + a2)
    except Exception as error:
        print("Nothing found, nothing to save")
    
    print("Research finished for: " + searchKeys)
except Exception as error:
    print(error)
