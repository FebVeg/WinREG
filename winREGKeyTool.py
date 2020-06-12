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

print("Username: " + username)
print("Target: " + hostname)
print("Working Directory: " + workDir)

searchKeys = input("Type a string that you want search: ")
outputKeysNameHKLM = "regKeysHKLM_" + searchKeys + ".txt"
outputKeysNameHKCU = "regKeysHKCU_" + searchKeys + ".txt"

if os.path.exists(workDir + outputKeysNameHKLM) or os.path.exists(workDir + outputKeysNameHKCU):
    print("File already existing")
    remove = input("Remove? [y/n]: ")
    if remove == "y":
        try:
            os.remove(workDir+outputKeysNameHKCU)
            os.remove(workDir+outputKeysNameHKLM)
        except Exception as error:
            print(error)
            print("Continue")
            pass
    elif remove == "n":
        sys.exit()
    else:
        print("Error")
        sys.exit()

print("Output file: " + workDir + outputKeysNameHKLM)

# Genero il comando CMD
cmdHKLM = 'REG Query HKLM\Software /F %s /S > %s%s' % (searchKeys, workDir, outputKeysNameHKLM)
cmdHKCU = 'REG Query HKCU\Software /F %s /S > %s%s' % (searchKeys, workDir, outputKeysNameHKCU)

# Inizio comando CMD
try: 
    print("\nsearching on HKLM.... Wait....")
    os.system(cmdHKLM)
    print("\nsearching on HKCU.... Wait....")
    os.system(cmdHKCU)
except Exception as error:
    print(error)  
print("Done\n")
# Fine comando CMD

# Edito il file di output e lo riscrivo senza nuove linee e spazi
print("Overwriting output without new lines or other special characters..")

try:
    output_file_remastered = os.path.splitext(os.path.basename(outputKeysNameHKLM))[0] + "_mod.txt"
    print("New file that will remastered: " + output_file_remastered)
    keys = open(workDir + outputKeysNameHKLM).readlines()
    for line in keys:
        if line.startswith('HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print(str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            print("No DATA Found")
        if line.startswith('    HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print(str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            print("No DATA Found")

    print("Done")
    new_file.close()
except Exception as error:
    print(error)

try:
    output_file_remastered = os.path.splitext(os.path.basename(outputKeysNameHKCU))[0] + "_mod.txt"
    print("New file that will remastered: " + output_file_remastered)
    keys = open(workDir + outputKeysNameHKCU).readlines()
    for line in keys:
        if line.startswith('HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print(str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            print("No DATA found")
        if line.startswith('    HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print(str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            print("No DATA Found")

    print("Done")
    new_file.close()
except Exception as error:
    print(error)