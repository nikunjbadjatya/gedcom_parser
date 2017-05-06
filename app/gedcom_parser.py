'''gedcom_parser.py

Contains class GedcomParser
'''

import sys
from app_exceptions import ValidationError
from validation import Validation


class GedcomParser():
    """GedcomParser class
    """

    def __init__(self, input_file):
        """Initialization of GedcomParser object.
        """

        Validation(input_file).validate()
        self.input_file = input_file


    def parse(self):
        """ This method is responsible for parsing the input gedcom format file.

        Returns a generator object
        """

        # 'with' in python makes sure that the 'enter' and 'exit' methods are called fror the underlying object.
        # Which in this case makes sure the file handler is opened and closed properly.
        with open(self.input_file) as f:
            prev_level = 0
            # This is python's way to read a file line by line. It does that in a way such that not entire file is loaded in memory.
            for line in f.readlines():
                line = line.strip()
                if line:
                    level, tag, value = self.parseline(line)
                    if level > prev_level + 1: #current level should not be greater than prev level by 1.
                        raise ValidationError("Invalid level. Current level should not be greater than prev level by 1.")
                    prev_level = level

                    # We want to use parse() method in a loop. 'yield' is python's way of acheiving this.
                    # Its basically making this function as a generator object.
                    yield (level, tag, value)


    def parseline(self, line):
        """ This method parses the passed line and returns the values of level, value and tag.

        Returns level, tag, value
        """

        parts = line.split()

        level = self.get_level(parts)
        tag = self.get_tag(parts)
        value = self.get_value(parts, tag)

        return level, tag, value

    def get_level(self, parts):
        try:
            level = int(parts[0])
            if level < 0: #level must be non negative int
                raise
        except:
            raise ValidationError("Invalid level found %s for line '%s'" % (level, parts))

        return level

    def get_tag(self, parts):
        try:
            tag = parts[1].lower()
        except:
            raise ValidationError("Couldnt find tag value. Invalid line passed %s" % parts)

        if not tag.startswith('@') and not (len(tag) in [3,4]):
            raise ValidationError("Tags should be 3 or 4 letters in length. %s" % parts[1])

        return tag

    def get_value(self, parts, tag):
        try:
            value = ' '.join(parts[2:])
        except:
            value = None

        if tag.startswith('@') and not value:
            raise ValidationError("An ID should have a value. %s" % parts)

        if tag.startswith('@') and not (len(value) in [3,4]):
            raise ValidationError("Tags should be 3 or 4 letters in length. %s" % parts)

        return value