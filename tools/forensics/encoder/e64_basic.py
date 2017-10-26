import os
import sys
import base64

while True:
    # Prompt
    prompt = raw_input("\033[33mprompt[\033[0m\033[32mbase64\033[0m\033[33m]\033[0m> ")

    s = prompt
    
    if prompt == "exit":
        break

    try:
        print "\n\033[01;34m=>\033[00m\033[01;33m Encoded base64 string:\033[00m\033[01;32m ",base64.b64encode(s),"\033[00m\n"
        pass
    except:
        print "\n\033[01;31m=>\033[00m\033[01;32m Error...\033[00m\n"
        pass

