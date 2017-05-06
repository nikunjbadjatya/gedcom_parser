'''xml_writer.py

Contains class and methods to write XML specifically for Gedcom format files.
'''

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom


class XMLWriter():
    """ Class for writing XMl file spefically for Gedcom format file.
    """

    def __init__(self, parser):
        """ Initializes the XMLWriter with the parse method.
        """
        self.parser = parser

    def write(self):
        """ Write method to write the xml file.
        """

        top = Element('gedcom')

        # we use this to keep track of possible parents only in current tree.
        element = {-1: top}

        for row in self.parser:
            current_level, tag, value = row

            # Create subelements for the xml based on the current level and tag value.
            if current_level != 0:
                child = SubElement(element[current_level-1], tag)
                child.text = value
            elif current_level == 0 and tag.startswith('@'):
                child = SubElement(top, value.lower(), {'id': tag})

            element[current_level] = child

        return top

def prettify(element):
    """Return a pretty-printed XML string for the Element.
    """

    rough_string = tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")