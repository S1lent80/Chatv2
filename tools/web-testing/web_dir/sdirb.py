import os
import sys
import re
import socket
import requests
import config

sys.path.insert(0, "modules")

## Variables:Config ##
# dir = config.web_dir
# host = config.main_rhost
# wordlist = config.main_wordlist

## Variables ##
gs = "\033[32m"
rs = "\033[31m"
ys = "\033[33m"
blue = "\033[34m"
ce = "\033[0m"
# -> Patterns
plus = gs + "[+] " + ce
minus = rs + "[-] " + ce
astk = blue + "[*] " + ce

## Variables:Main ##
rhost = sys.argv[1]
wordlist = sys.argv[2]
port = sys.argv[3]

class SDirbMain():

    def _checkParam(self, rhost, wordlist, port):
        if len(rhost) and len(wordlist) and port == 0:
            print "\n" + rs + "[X] " + ce + gs + "Please supply the following paramters:" + ce
            print gs + "RHOST (Remote Host): i.e -> www.example.com  -  Current length: " + ce + ys + len(rhost) + ce
            print gs + "Wordlists: i.e -> /path/to/wordlist          -  Current dir: " + ce + ys + "None" + ce
            print gs + "Port: i.e -> 80                              -  Current port: " + ce + ys + str(port) + ce + "\n"
            sys.exit(1)
    

    def _checkHostConnection(self, rhost):
        print astk + gs + "Checking connection to RHOST: " + ce + ys + rhost + ce + gs + "..." + ce
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global sock

        # Check the connection
        try:
            stat = sock.connect_ex((rhost, port))
            sock.close()
            if stat == 0:
                print plus + ys + "Successfully connected to rhost..." + ce
                pass
            else:
                print minus + gs + "Could not connect to rhost: " + ce + ys + rhost + ce + gs + "..." + ce
                sys.exit(1)
        except socket.error as e:
            print rs + "[X] " + ce + gs + "Program error: " + str(e) + ce
            sys.exit(1)

    def _readWordList(self, wordlist):
