import unittest
import os

from utilsPy.folder_structure import remove_dirs, create_dirs
from dataArchivePy.archive import archive_files, extract_archive, archive_folders

class ArchiveTestClass(unittest.TestCase, archive_folders):
 
    def __init__(self, *args, **kwargs):
 
        super(ArchiveTestClass, self).__init__(*args, **kwargs)

        self.commit = "789hk4"
        self.output_pth = "./tests/test_archive/"
        self.archive_fls = ["test_data1.csv", "test_data2.csv"]
        self.fl = "test_data1.csv"

        self.af = archive_files(self.commit, self.output_pth, self.archive_fls)
        self.archive_dirs = self.af.archive_dirs
        self.ea = extract_archive(self.commit, self.pth, self.fl)

        self.setUp()

    def setUp(self):

        remove_dirs(self.archive_dirs)

    def test_create_archive_str(self):
        
        self.af.create_archive_str()
        self.assertTrue(all([os.path.exists(d) for d in self.archive_dirs]))
        

    def test_extract_archive(self):

        self.assertTrue(hasattr(self.ea, "df"))