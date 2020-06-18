import os
import subprocess
import sys
import time
import re
import itertools
import threading

os.system("cls") # pulisco CMD

username = os.getlogin() # Username Info
workDir = os.path.dirname(os.path.abspath(__file__)) + "\\" # WorkDire Info 
hostname = os.environ['COMPUTERNAME']

print("[i] Version: 1.0alpha")
print("[i] Username: " + username)
print("[i] Target: " + hostname)
print("[i] Working Directory: " + workDir)

searchKeys = input('\n[-] Type a string that you want search: ')
searchSoftware = input("[-] Need to search a program? [y/n]: ")

outputKeysNameHKLM = "regKeysHKLM_" + searchKeys + ".txt"
outputKeysNameHKCU = "regKeysHKCU_" + searchKeys + ".txt"

if searchSoftware == "y":
    searchSoftware = "\\Software"
elif searchSoftware == "n":
    searchSoftware = ""

if os.path.exists(workDir + outputKeysNameHKLM):
    print("[!] File %s already existing" % (outputKeysNameHKLM))
    sys.exit()

if os.path.exists(workDir + outputKeysNameHKCU):
    print("[!] File %s already existing" % (outputKeysNameHKCU))
    sys.exit()

print("[i] Output file: " + workDir + outputKeysNameHKLM.replace('"', ''))
print("[i] Output file: " + workDir + outputKeysNameHKCU.replace('"', ''))

def searching_function():
    # Genero il comando CMD
    cmdHKLM = 'REG Query HKLM%s /F %s /S > %s%s' % (searchSoftware, searchKeys, workDir, outputKeysNameHKLM)
    cmdHKCU = 'REG Query HKCU%s /F %s /S > %s%s' % (searchSoftware, searchKeys, workDir, outputKeysNameHKCU)

    # Inizio comando CMD
    try: 
        os.system(cmdHKLM)
        os.system(cmdHKCU)
    except SystemError as error:
        print(error)  
    # Fine comando CMD

done = False
def animate():
    print("-"*50)
    #for c in itertools.cycle(['|', '/', '-', '\\']):
    for c in itertools.cycle(['[i] Searching...',
                              '[i] sEarching...',
                              '[i] seArching...',
                              '[i] seaRching...',
                              '[i] searChing...',
                              '[i] searcHing...',
                              '[i] searchIng...',
                              '[i] searchiNg...',
                              '[i] searchinG...',
                              '[i] searchiNg...',
                              '[i] searchIng...',
                              '[i] searcHing...',
                              '[i] searChing...',
                              '[i] seaRching...',
                              '[i] seArching...',
                              '[i] sEarching...',
                              ]):
        if done:
            break
        sys.stdout.write('\r' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone            ')

t = threading.Thread(target=animate)
t.start()

searching_function()
time.sleep(1)
done = True

# Edito il file di output e lo riscrivo senza nuove linee e spazi
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
            print("[!] Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue

        if line.startswith('    HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print("[!] Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue
    a1 = "[i] New output file: " + output_file_remastered
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
            print("[!] Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue

        if line.startswith('    HK'):
            line = line.strip()
            line = re.sub(r' \s.*$', '', line)
            string = line.replace("\n", "")
            print("[!] Key found: " + str(string))
            new_file = open(workDir + output_file_remastered, "a+")
            new_file.write(str(line) + "\n")
        else:
            continue
        
    a2 = "[i] New output file: " + output_file_remastered

    try:
        new_file.close()
        if os.path.isfile(workDir + a1) and os.path.isfile(workDir + a2):
            print("[i] Output saved: " + a1)
            print("[i] Output saved: " + a2)
    except Exception as error:
        print("[i] Nothing found, nothing to save")
    
    print("[-] Research finished for: " + searchKeys)
except Exception as error:
    print(error)
