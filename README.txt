About:
======
Python program for Gedcom Parser.


Requirements:
=============
1. Python2.7 or greater. Tested on python2.7 on MacOS 10.11.6
2. Python's pep8 module to be installed. This is for style check.

Directories and Files:
======================
~/aconex    $ tree
.
├── README.txt
├── __init__.py
├── __pycache__
├── app
│   ├── __init__.py
│   ├── __pycache__
│   ├── app_exceptions.py
│   ├── app_settings.py
│   ├── gedcom_parser.py
│   ├── main.py
│   ├── sample_input.txt
│   ├── sample_output.xml
│   ├── validation.py
│   └── xml_writer.py
└── tests
    ├── ThisFileIsntReadable.txt
    ├── ThisIsNotAFile
    ├── __init__.py
    ├── __pycache__
    ├── invalid_sample_data.txt
    ├── invalid_sample_data_tag_length.txt
    ├── invalid_sample_data_tag_length2.txt
    ├── sample_data_empty.txt
    ├── test_parser.py
    ├── test_settings.py
    ├── valid_sample_data.txt
    └── valid_sample_output.xml

6 directories, 21 files


How to Run:
============

1. Unzip and go to aconex/app folder. Start the app as:

~/aconex    $ python app/main.py app/sample_input.txt

<?xml version="1.0" ?>
<gedcom>
  <indi id="@i0001@">
    <name>Elizabeth Alexandra Mary /Windsor/</name>
    <sex>F</sex>
    <birt>
      <date>21 Apr 1926</date>
      <plac>17 Bruton Street, London, W1</plac>
    </birt>
    <occu>Queen</occu>
....
....


In this case the output will be shown in the terminal itself. You can also run as:

~/aconex    $ python app/main.py app/sample_input.txt > sample_output.txt

2. You can also run the tests as:

~/aconex/   $ python -m unittest tests.test_parser
Running test_file_doesnt_exist
.Running test_file_is_not_file
.Running test_file_is_not_readable
.Running test_invalid_format_file
.Running test_invalid_tag_length_1
.Running test_invalid_tag_length_2
.Running test_pep8
.Running test_valid_file
.Running test_valid_file_output
.
----------------------------------------------------------------------
Ran 9 tests in 0.083s

OK


Performed tests:
================
1. Python PEP8 style and consistency check.
2. Whether input file exists, is available and is accessible.
3. Current level should not be greater than previous level by 1 in the input gedcom file.
4. Level should be an int and greater than 0. Leading zeroes are parsed naturally.
5. Every line in the file should have level and tag.
6. Empty lines in a file doesnt make any difference.
7. Whitespaces within a line will not make any difference.
8. Xml output of a valid gedcom file.
9. Tags should be 3 or 4 characters in length.

Algorithm:
===========
1. main.py is the driver file. We first initialize the parser which validates the input file as well.
2. Once GedcomParser object is initialized, we pass the parser object to xml writer.
3. xml writer, based on gedcom format, starts writing the xml file.


Author:
=======
Nikunj Badjatya (nikunjbadjatya@gmail.com)
Date: May 1st, 2017
India
