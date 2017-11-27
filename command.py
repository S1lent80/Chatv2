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

# -----------------------------------------------------
class CommandUtils:

    def _help(self):
        pass


class Commands:

    def cmd(self):
        # Variables


        # Main console
        while True:
            try:
                cmd = raw_input(gs + "[ cmd ]> " + ce)
                pass
            except KeyboardInterrupt:
                print "\n"
                break
            str = cmd.split(' ')
            str1 = cmd.split(':')

            # Command ls
            if str[0] in ['ls', 'list']:
                try:
                    print "\n"
                    os.system("ls --color=auto " + str[1])
                    print "\n"
                except:
                    print ''
                    os.system('ls --color=auto')
                    print ''

            if cmd in ['exit','back']:
                print "\n"
                break


