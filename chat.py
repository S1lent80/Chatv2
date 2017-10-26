import os
import sys
import re
import tqdm
import time
from tqdm import *
from time import sleep

sys.path.insert(0,"modules/python/config")
import sys_config

## Chat main module - Version: 1-1.8.9 ##

# =========================================================================================================
# Variables - Program
console_prompt = sys_config.chat_prompt
version = ""
file_store = "/opt/chat/file_store.txt"
main_dir = sys_config.dir_main
# -> Colors
gs = "\033[32m"
rs = "\033[31m"
ys = "\033[33m"
blue = "\033[34m"
ce = "\033[0m"
# Colors:Patterns
plus = gs + "[+] " + ce
minus = rs + "[-] " + ce
astk = blue + "[*] " + ce
# =========================================================================================================
# Classes and functions
class Command:
    ## Command class ##

    def _cmdCreateHistFile(self,filename, prompt_object):
        with open(filename, "a+") as hist_file:
            hist_file.write(prompt_object + "\n")
            hist_file.close()

    def _cmdHistFile(self,filename):
        print "\n" + ys + "Command history:" + ce
        print "=" * 16,"\n"
        os.system("cat " + filename)
        print "\n"

# =========================================================================================================
# Loading bar
os.system('clear')
print "[ Loading ]...\n"
for x in tqdm(range(100)):
    sleep(0.05)
os.system('clear')
# =========================================================================================================
# Banners and greeters


# =========================================================================================================
# Class declarTION
cmd = Command()

# =========================================================================================================
# Main program
while True:
    # Give the user a prompt
    try:
        prompt = raw_input(blue + "[ " + ce + gs + console_prompt + ce + blue + " ]" + ce + ": ")
    except KeyboardInterrupt:
        # Print a message then exit the program
        print "\n"
        sys.exit(1)

    ## History file ##
    cmd._cmdCreateHistFile(file_store, prompt)


    # -----------------------------------------------------------------------------------------------------
    # Reg->cmd
    cmd_exit = re.search("exit",prompt,re.I|re.M)
    cmd_list = re.search("list",prompt,re.I|re.M)
    cmd_ehx = re.search("encode",prompt,re.I|re.M)
    cmd_dhx = re.search("decode",prompt,re.I|re.M)
    dhx_hex = re.search("hex",prompt,re.I|re.M)
    dhx_64 = re.search("base64",prompt,re.I|re.M)


    if cmd_exit:
        # Print a message then exit
        sys.exit(0)
    # -----------------------------------------------------------------------------------------------------
    # Show history command
    if prompt in ['show history','show_history','command_history','cmd_history']:
        cmd._cmdHistFile(file_store)
        pass

    # -----------------------------------------------------------------------------------------------------
    # System commands (altered)
    if cmd_list:
        os.system('ls /' + prompt[6:])
        pass

    # -----------------------------------------------------------------------------------------------------
    if cmd_ehx and dhx_hex:
        os.system('python ' + sys_config.e_hex_file)
        pass


    else:
        print "\n" + gs + "I cannot find the command: [ " + ce + ys + prompt + ce + gs + " ]..." + ce + "\n"
        pass
