import os
import sys
import re
import tqdm
import time
import command
from tqdm import tqdm
from time import sleep

sys.path.insert(0, "modules/python/config")
import config

sys.path.insert(0, "tools/common/notes");


## Chatv2 Remake: 2 - Version: 1 ##

# *******************************************************************************************************
# Variables
name = config.name
prompt_1 = config.prompt
# -> Colors
gs = "\033[32m"
rs = "\033[31m"
ys = "\033[33m"
blue = "\033[34m"
ce = "\033[0m"
# -> Patterns
plus = gs + "[+] " + ce
minus = rs + "[-] " + ce
astk = blue + "[*] " + ce

# *******************************************************************************************************
# Classes and functions
class MainCommand:

    def createHistFile(self, filename, prompt_object):
        with open(filename, "a+") as hist_file:
            hist_file.write(prompt_object + "\n")
            hist_file.close()

    def showHistFile(self, filename):
        print '\n'
        print ys + "Command history:" + ce
        print "=" * 16
        os.system('cat ' + filename)
        print '\n'
        pass


# *******************************************************************************************************
# Class declarations
cmd1 = MainCommand()
cmd2 = command.Commands()

# *******************************************************************************************************
# Loading bar
os.system('clear')
print "[ Loading... ]\n"
for x in tqdm(range(100)):
    sleep(0.05)
os.system('clear')

# *******************************************************************************************************
# Banners and greeters


# *******************************************************************************************************
# Main program
while True:
    # Give the user a prompt
    try:
        prompt = raw_input(gs + "[ " + ce + ys + prompt_1 + ce + gs + " ]: " + ce)
        pass
    except KeyboardInterrupt:
        # Print an exit message
        print '\n'
        break

    cmd1.createHistFile("/opt/chat/hist_file.txt", prompt)

    # ---------------------------------------------------------------------------------------------------
    # Regular expression: search
    cmd_exit = re.search("exit", prompt, re.I|re.M)
    cmd_command = re.search("cmd", prompt, re.I|re.M)
    cmd_command_alt = re.search("command", prompt, re.I|re.M)


    # ---------------------------------------------------------------------------------------------------
    # Commands
    if cmd_exit:
        # Print an exit message
        break

    elif prompt in ['show history', 'show_history', 'history']:
        cmd1.showHistFile("/opt/chat/hist_file.txt")
        pass

    elif cmd_command or cmd_command_alt:
        cmd2.cmd()
        pass


    else:
        print "\n" + gs + "I could not find the command/phrase [ " + ce + ys + prompt + ce + gs + " ]..." + ce + "\n"
        pass


    # ---------------------------------------------------------------------------------------------------
