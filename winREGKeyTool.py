import os
import subprocess
import sys
import time
import re
import threading

os.system("cls") # pulisco CMD

print("Register Key Finder & Destroyer\n")

if os.name == "posix":
    print("This script is for Windows System")
    sys.exit()

username = os.getlogin() # Username Info
workDir = os.path.dirname(os.path.abspath(__file__)) + "\\" # WorkDire Info 
hostname = os.environ['COMPUTERNAME']

print("[i] Version: 1.0alpha")
print("[i] Username: " + username)
print("[i] Target: " + hostname)
print("[i] Working Directory: " + workDir)

searchKeys = input('\n[?] Type a string that you want search: ')
searchSoftware = input("[?] Need to search from another dir (Es. /software)? [y/n]: ")

outputKeysNameHKLM = "regKeysHKLM_" + searchKeys + ".txt"
outputKeysNameHKCU = "regKeysHKCU_" + searchKeys + ".txt"

if searchSoftware == "y":
    searchSoftware = input("[?] Dir: ")
    searchSoftware = "\\"+searchSoftware
elif searchSoftware == "n":
    searchSoftware = ""

if os.path.exists(workDir + outputKeysNameHKLM):
    print("[!] File %s already existing" % (outputKeysNameHKLM))
    print("[!] File %s already existing" % (outputKeysNameHKCU))
    sys.exit()

print("\n[i] CMD output File: " + workDir + outputKeysNameHKLM.replace('"', ''))
print("[i] CMD output File: " + workDir + outputKeysNameHKCU.replace('"', ''))

# Genero il comando CMD
cmdHKLM = 'REG Query HKLM%s /F %s /S > %s%s' % (searchSoftware, searchKeys, workDir, outputKeysNameHKLM)
cmdHKCU = 'REG Query HKCU%s /F %s /S > %s%s' % (searchSoftware, searchKeys, workDir, outputKeysNameHKCU)
print("\n[CMD] " + cmdHKLM + "\n[CMD] " + cmdHKCU)

# Inizio comando CMD
try: 
    print("\n[+] Searching '%s' on HKLM.... Wait...." % (searchKeys))
    os.system(cmdHKLM)
    print("[+] Searching '%s' on HKCU.... Wait...." % (searchKeys))
    os.system(cmdHKCU)
    print("[+] Searching finished\n")
except Exception as error:
    print("Errore comando: " + error)
    sys.exit()
# Fine comando CMD

# Edito il file di output e lo riscrivo senza nuove linee e spazi
outputKeysNameHKCU = outputKeysNameHKCU.replace('"', '')
outputKeysNameHKLM = outputKeysNameHKLM.replace('"', '')

try:
    if os.path.isfile(workDir + outputKeysNameHKLM):
        output_file_remastered = os.path.splitext(os.path.basename(outputKeysNameHKLM))[0] + "_mod.txt"
        keys = open(workDir + outputKeysNameHKLM).readlines()
        for line in keys:
            if line.startswith('HK'):
                line = line.strip()
                line = re.sub(r' \s.*$', '', line)
                string = line.replace("\n", "")
                #print("[!] Key found: " + str(string))
                new_file = open(workDir + output_file_remastered, "a+")
                new_file.write(str(line) + "\n")
                new_file.close()
            else:
                continue

            if line.startswith('    HK'):
                line = line.strip()
                line = re.sub(r' \s.*$', '', line)
                string = line.replace("\n", "")
                #print("[!] Key found: " + str(string))
                new_file = open(workDir + output_file_remastered, "a+")
                new_file.write(str(line) + "\n")
                new_file.close()
            else:
                continue
    if os.path.exists(workDir + output_file_remastered):
        print("Check the output: " + output_file_remastered)
except Exception as error:
    print(error)

try:
    if os.path.isfile(workDir + outputKeysNameHKCU):
        output_file_remastered = os.path.splitext(os.path.basename(outputKeysNameHKCU))[0] + "_mod.txt"
        keys = open(workDir + outputKeysNameHKCU).readlines()
        for line in keys:
            if line.startswith('HK'):
                line = line.strip()
                line = re.sub(r' \s.*$', '', line)
                string = line.replace("\n", "")
                #print("[!] Key found: " + str(string))
                new_file = open(workDir + output_file_remastered, "a+")
                new_file.write(str(line) + "\n")
                new_file.close()
            else:
                continue

            if line.startswith('    HK'):
                line = line.strip()
                line = re.sub(r' \s.*$', '', line)
                string = line.replace("\n", "")
                #print("[!] Key found: " + str(string))
                new_file = open(workDir + output_file_remastered, "a+")
                new_file.write(str(line) + "\n")
                new_file.close()
            else:
                continue
    if os.path.exists(workDir + output_file_remastered):
        print("Check the output: " + output_file_remastered)

    print("\n[-] All processes are done for: " + searchKeys)
except Exception as error:
    print(error)    
