import os
import sys
import urllib2
import requests
import platform
import configparser

# Variables
gs = "\033[32m"
rs = "\033[31m"
ys = "\033[33m"
blue = "\033[34m"
ce = "\033[0m"
# -> Patterns
plus = gs + "[+] " + ce
minus = rs + "[-] " + ce
astk = blue + "[*] " + ce


class SPM:

    def _testConnection(self, url):
        a = requests.get(url)
        if a.status_code == 200 or a.status_code == requests.codes.ok:
            print blue + "=> " + ce + gs + "Successfully established connection to: " + str(url) + "..." + ce + "\n"
            pass
        elif a.status_code == 404:
            print "\n" + rs + "[X] " + ce + gs + "Could not connect to \"" + str(url) + "\", returned 404..." + ce
            sys.exit(1)
        elif a.status_code == requests.codes['temporary_redirect']:
            print ys + "=> " + ce + gs + "Site: " + str(url) + " - Init -> temp_redirect..." + ce + "\n"
            pass

    def _genMainConfig(self, filename):
        # Shorten things up
        file1 = filename

        # Check if the file exists
        if os.path.isfile(file1):
            print astk + gs + "Using config file: " + file1 + "..." + ce
            pass
        else:
            print minus + gs + "Config file: " + file1 + " doesn't exist..." + ce
            sys.exit(1)

        # Generate the config file
        config = configparser.ConfigParser()
        config['Default:'] = {'MainUrl': 'http://127.0.0.1/s1',
                              'MainPort': 80,
                              'MainOS': '',
                              'Arch': 'amd64'
                              }
        if platform.dist() in ['Kali', 'Debian']:
            config['Default:']['MainOS'] = 'debian'
            pass
        elif platform.dist() in ['Ubuntu', 'Mint', 'Linux Mint']:
            config['Default:']['MainOS'] = 'ubuntu'
            pass
        else:
            # Give the user a prompt for the dist name
            pass

        # Write to the config file
        with open("config.spm", "w") as configfile:
            config.write(configfile)
            pass

    """
    Grab the package and get package arch compression type
    This can be: .deb, .tar.<ARCH>, .rpm
    Then if it is a .tar.<ARCH>, then extract the archive and look for these files:
    -> configure, Makefile
    -> autogen
    -> Rakefile, Gemfile
    If the package is a python related package, look for the required file and pull contents from it
    If there are dependencies that need to be resolved get the error with dependencies and try to install them
    """
    