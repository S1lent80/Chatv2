import os
import sys
import string

while True:
    # Give the user a prompt
    prompt = raw_input("\033[33mprompt[\033[0m\033[32mhex\033[0m\033[33m]\033[0m> ")
    
    s = prompt 

    if prompt == "exit":
        break

    if prompt == "clear":
        os.system('clear')

    if not all(c in string.hexdigits for c in s):
        print "\n\033[01;31m=>\033[00m\033[01;32m Please enter a hex string...\033[00m\n"
    else:
        try:
	    print "\n\033[01;34m=>\033[00m\033[01;33m Decoded string:\033[00m\033[01;32m ",s.decode('hex'),"\033[00m\n"
            pass
        except:
            print "\n\033[01;31m=>\033[00m\033[01;32m Error...\033[00m\n"
            pass
