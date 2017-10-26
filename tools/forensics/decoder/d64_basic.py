import os
import sys
import base64
import string

class Command:
    def cmd(self,str):
	if str == 'exit':
	    sys.exit()
	if str == 'clear':
	    os.system('clear')


# Classes
cmd = Command()

while True:
    # Give the user a prompt
    prompt = raw_input("\n\033[33mprompt[\033[0m\033[32mbase64\033[0m\033[33m]\033[0m> ")

    s = prompt
    
    cmd.cmd(s)
    
    try:
        print "\n\033[01;34m=>\033[00m\033[01;33m String (base64) decoded:\033[00m"
        print "\033[01;32m>> [\033[00m " + base64.b64decode(s) + "\033[32m ]\033[0m"
        pass
    except:
        print "\n\033[01;31m=>\033[00m\033[01;32m Error...\033[00m\n"
        pass

