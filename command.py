import os
import sys
import re

## Command line module: 1 - Version: 1 ##

# Variables
dir_main = os.getcwd()
gs = "\033[32m"
rs = "\033[31m"
ys = "\033[33m"
blue = "\033[34m"
ce = "\033[0m"
# -> Patterns
plus = gs + "[+] " + ce
minus = rs + "[-] " + ce
astk = blue + "[*] " + ce

def main():
    while True:
        # Command line prompt
        try:
            cmd = raw_input(gs + "[ " + ce + ys + "cmd" + ce + gs + " ]> " + ce)
            pass
        except KeyboardInterrupt:
            print '\n'
            break

        # ----------------------------------------------------------------------------------------------
        # Regular expression: search
        cmd_ls = re.search("list", cmd, re.I | re.M)

        # ----------------------------------------------------------------------------------------------
        # Commands
        if cmd_ls:
            os.system('ls /' + cmd[6:])
            pass


        # ----------------------------------------------------------------------------------------------
