import os
import sys
import string

while True:
    # Prompt
    prompt = raw_input("\033[33mencode[\033[0m\033[32mhex\033[0m\033[33m]\033[0m> ")

    s = prompt
    
    if prompt == "exit":
        break

    try:
        print "\n\033[01;34m=>\033[00m\033[01;33m Encoded hex string:\033[00m\033[01;32m ",s.encode('hex'),"\033[00m\n"
        pass
    except:
        print "\n\033[01;31m=>\033[00m\033[01;32m Error...\033[00m\n"
        pass
