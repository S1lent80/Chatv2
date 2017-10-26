import os
import sys
from sys import platform as osid

## Config file: 1 ##

# -> Main (home) dir file - /opt/chat/config
dir_main = open("/opt/chat/config/dir_main.txt").read().strip('\n')

# -> Prompt file
chat_prompt = open(dir_main + "/chat/modules/python/config/text_files/prompt.txt").read().strip('\n')

# -> Main files
e_hex_file = dir_main + "/chat/tools/forensics/encoder/ehx_basic.py"
e_64_file = dir_main + "/chat/tools/forensics/encoder/e64_basic.py"
d_hex_file = dir_main + "/chat/tools/forensics/decoder/dhx_basic.py"
d_64_file = dir_main + "/chat/tools/forensics/decoder/d64_basic.py"
