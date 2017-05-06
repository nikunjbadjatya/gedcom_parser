'''test_parser.py

Contains the tests for various functionalities.

Note: test_file_is_not_readable is commented deliberately.
Create a file with no read permission in tests folder as
tests/ThisFileIsntReadable.txt name and then uncomment the test.

'''

import unittest
import pep8
import os
import subprocess

from app.gedcom_parser import GedcomParser
from app.app_exceptions import ValidationError
from test_settings import *

class GedcomParserTest(unittest.TestCase):

    def setup(self):
        pass

    def test_pep8(self):
        """ Test to check python style and syntax in all py modules.
        Run PEP8 on all files in this directory and subdirectories.
        """

        def ignore(dir):
            """Should the directory be ignored?"""
            # ignore stuff in virtualenvs or version control directories
            ignore_patterns = ('.git', 'bin', 'lib' + os.sep + 'python')
            for pattern in ignore_patterns:
                if pattern in dir:
                    return True
            return False
        print("Running test_pep8")
        style = pep8.StyleGuide(quiet=True)
        style.options.ignore += ('E111',)  # 4-spacing is just too much
        style.options.max_line_length = 120  # Line length 120. Because its 21st century

        errors = 0
        for root, _, files in os.walk('.'):
            if ignore(root):
                continue

        python_files = [f for f in files if f.endswith('.py')]
        errors += style.check_files(python_files).total_errors

        self.assertEqual(errors, 0, 'PEP8 style errors: %d' % errors)

    def test_file_doesnt_exist(self):
        """ Test for checking whether a non existent file raises exception or not.
        """
        print("Running test_file_doesnt_exist")
        with self.assertRaises(Exception) as context:
            GedcomParser("ThisFileDoesntExist.txt")
        self.assertTrue('File path does not exist :ThisFileDoesntExist.txt' in context.exception)

    def test_file_is_not_file(self):
        """ Test for checking input file is actually not a file.
        """
        print("Running test_file_is_not_file")
        with self.assertRaises(Exception) as context:
            GedcomParser("tests/ThisIsNotAFile")
        self.assertTrue('Input path is not a file :tests/ThisIsNotAFile' in context.exception)

    #def test_file_is_not_readable(self):
    #    """ Test for checking input file is actually readable.
    #    """
    #    print("Running test_file_is_not_readable")
    #    with self.assertRaises(Exception) as context:
    #        GedcomParser("tests/ThisFileIsntReadable.txt")
    #    self.assertTrue('File is not accessible :tests/ThisFileIsntReadable.txt' in context.exception)

    def test_valid_file(self):
        """ Test for valid file. i.e. the file should exist, it should be a file and it should be readable.
        """
        print("Running test_valid_file")
        ret = GedcomParser("tests/valid_sample_data.txt")
        self.assertIsInstance(ret, GedcomParser)

    def test_valid_file_output(self):
        """ Test the program output when passed a valid file.
        """
        print("Running test_valid_file_output")
        result = subprocess.Popen(["python", "app/main.py", "tests/valid_sample_data.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        with open("tests/valid_sample_output.xml") as f:
            self.assertEqual(f.read(), stdout)

    def test_invalid_format_file(self):
        """ Test for invalid file. The current level is more than one than the previous level.
        """
        print("Running test_invalid_format_file")
        with self.assertRaises(Exception) as context:
            ret = GedcomParser("tests/invalid_sample_data.txt")
            for data in ret.parse():
                pass
        self.assertTrue('Invalid level. Current level should not be greater than prev level by 1.' in context.exception)

    def test_invalid_tag_length_1(self):
        """ Test for invalid tag length.
        """
        print("Running test_invalid_tag_length_1")
        with self.assertRaises(Exception) as context:
            ret = GedcomParser("tests/invalid_sample_data_tag_length.txt")
            for data in ret.parse():
                pass
        self.assertTrue("Tags should be 3 or 4 letters in length. ['0', '@I0001@', 'INDIII']" in context.exception)

    def test_invalid_tag_length_2(self):
        """ Test for invalid tag length.
        """
        print("Running test_invalid_tag_length_2")
        with self.assertRaises(Exception) as context:
            ret = GedcomParser("tests/invalid_sample_data_tag_length2.txt")
            for data in ret.parse():
                pass
        self.assertTrue("Tags should be 3 or 4 letters in length. NAMEEE" in context.exception)

if __name__ == '__main__':
    unittest.main()
