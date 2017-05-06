'''validation.py
'''

from os import path, access, R_OK
from app_exceptions import ValidationError


class Validation():
    def __init__(self, file):
        self.file = file

    def validate(self):
        """ This method validates the input file on its existence,
        whether its file and whether its accessible.
        """
        self.validate_path_exists()
        self.validate_isfile()
        self.validate_is_accessible()

    def validate_path_exists(self):
        if not path.exists(self.file):
            raise ValidationError("File path does not exist :%s" % self.file)

    def validate_isfile(self):
        if not path.isfile(self.file):
            raise ValidationError("Input path is not a file :%s" % self.file)

    def validate_is_accessible(self):
        if not access(self.file, R_OK):
            raise ValidationError("File is not accessible :%s" % self.file)