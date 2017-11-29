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
rhost = sys.argv[1:]
wordlist = sys.argv[1:]
port = 80

class SDirbMain():

    def _checkParam(self, rhost, wordlist, port):
        if len(rhost) and len(wordlist) and port == 0:
            print "\n" + rs + "[X] " + ce + gs + "Please supply the following paramters:" + ce
            print gs + "RHOST (Remote Host): i.e -> www.example.com  -  Current length: " + ce + ys + len(rhost) + ce
            print gs + "Wordlists: i.e -> /path/to/wordlist          -  Current dir: " + ce + ys + "None" + ce
            print gs + "Port: i.e -> 80                              -  Current port: " + ce + ys + str(port) + ce + "\n"
            sys.exit(1)


    def _checkHostConnection(self, rhost):
        print astk + gs + "Checking connection to RHOST: " + ce + ys,rhost,ce + gs + "..." + ce
	global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Check the connection
        try:
            stat = sock.connect_ex((str(rhost), int(port)))
            sock.close()
            if stat == 0:
                print plus + ys + "Successfully connected to rhost..." + ce
                pass
            else:
                print minus + gs + "Could not connect to rhost: " + ce + ys,rhost,ce + gs + "..." + ce
                sys.exit(1)
        except socket.error as e:
            print rs + "[X] " + ce + gs + "Program error: " + str(e) + ce
            sys.exit(1)

    def _readWordList(self, wordlist):
        print astk + gs + "Parsing wordlist: " + ce + ys,wordlist,ce + gs + "..." + ce
        # Open the file for reading
        try:
            with open(wordlist) as file:
		global chk_file
                chk_file = file.read().strip().split('\n')
            print plus + ys + "Successfully parsed wordlist..." + ce
        except IOError as e:
            print minus + gs + "Could not parse file: ",wordlist," - Error: " + str(e) + ce
            sys.exit(1)

    def webPathScrape(self, path):
        print astk + gs + "Init web response/request..." + ce + "\n"
        try:
            response = requests.get(rhost,"/" + path).status_code
        except Exception as e:
            print minus + gs + "Error -> " + ce + ys + str(e) + ce
            sys.exit(1)
        if response == 200:
            print gs + "[ VALID DIRECTORY ]: " + ce + ys + "%s - %s..." % (path, rhost)
            pass

    def _dirbMain(self):
        print "\n" + astk + gs + "Beginning web dir scan..." + ce
        try:
            for i in range(len(chk_file)):
                self.webPathScrape(chk_file[i])
            print "\n" + plus + ys + "Scan complete..." + ce + "\n"
        except KeyboardInterrupt:
            print "\n" + gs + "User interrupt..." + ce + "\n"
            sys.exit(1)

def main():
    sdirb = SDirbMain()
    sdirb._checkParam(rhost,wordlist,port)

    sdirb._checkParam(rhost, wordlist, port)
    sdirb._checkHostConnection(rhost)
    sdirb._readWordList(wordlist)
    sdirb._dirbMain()

if __name__ == '__main__':
    main()
