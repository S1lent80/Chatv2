import os
import sys
import re
import optparse
from optparse import OptionParser

'''
This program was just something I designed as just for fun
I just added it for the heck of it since there will be a 
GUI version written in Java (using JavaFX)
'''

# Variables
__version__ = '1.0.0'
gs = "\033[32m"
rs = "\033[31m"
ys = "\033[33m"
blue = "\033[34m"
ce = "\033[0m"
# -> Patterns
plus = gs + "[+] " + ce
minus = rs + "[-] " + ce
astk = blue + "[*] " + ce
# ************************************************************************************

class NotesCommon:

    def _co_checkNoteExists(self, filename):
        if os.path.isfile(filename):
            print "\n" + plus + ys + "Note \"" + filename + "\" exists..." + ce + "\n"
            pass
        else:
            print "\n" + minus + gs + "Note \"" + filename + "\" doesn't exist..." + ce + "\n"
            pass

    def _co_writeNote(self, filename, dir, note):
        note = dir + "/" + filename
        try:
            with open(note, "a+") as note_file:
                note_file.write(note + "\n")
                note_file.close()
                print "\n" + gs + "Successfully written to: " + ce + ys + note + ce + gs + "..." + ce + "\n"
                pass
        except Exception, e:
            print "\n" + minus + gs + "I ran into an error: " + ce + ys + str(e) + ce + gs + "..." + ce + "\n"
            pass

    def _co_generateConfig(self, filename):
        pass


def main():
    # Class setup
    notes = NotesCommon()

    parser = OptionParser(usage="notes.py -n <FILENAME> -d <DIR> -w <NOTE_CONTENT>", conflict_handler="resolve")
    parser.add_option('-n', '--name', dest="note_name", default="note.txt", help="Set the filename for the note")
    parser.add_option('-d', '--dir', dest="note_dir", default="/opt/chat", help="Specify a directory to store the note in")
    parser.add_option('-w', '--write', dest="write_note", help="What is the note that you want me to save to the file")
    parser.add_option('-i', '--interactive', dest="note_interactive", help="Launch application interactive wizard")
    parser.add_option('-c', '--check', dest="check_note", help="Check if a note exists")
    parser.add_option('-s', '--setdir', dest="set_default_dir", help="Set default note directory")

    (options, args) = parser.parse_args()

    # If [ '-n', '-w', '-d' ] are used
    if options.note_name and options.note_dir and options.write_note:
        notes._co_writeNote(options.note_name, options.note_dir, options.write_note)
        pass

    if options.check_note:
        notes._co_checkNoteExists(options.check_note)
        pass

if __name__ == '__main__':
    main()
