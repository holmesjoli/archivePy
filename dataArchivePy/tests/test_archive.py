import unittest

from gitToolPy.tools import extract_archive

class ExtractArchiveTestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):
 
        super(ExtractArchiveTestClass, self).__init__(*args, **kwargs)

        self.commit = "789hk4"
        self.pth = "./tests/test_archive"
        self.fl = "test_data.csv"
        self.ea = extract_archive(self.commit, self.pth, self.fl)

    def test_(self):

        self.assertTrue(hasattr(self.ea, "df"))
