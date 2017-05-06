'''main.py

Main driver file for GEDCOM parser.
'''

import sys
from xml_writer import XMLWriter, prettify
from gedcom_parser import GedcomParser

def main():
    filename = sys.argv[1]
    parser = GedcomParser(filename)
    xmlwriter = XMLWriter(parser.parse())
    print(prettify(xmlwriter.write()))


if __name__ == '__main__':
    main()