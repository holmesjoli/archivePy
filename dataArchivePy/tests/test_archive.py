import unittest
import os

from utilsPy.folder_structure import remove_dirs, create_files
from dataArchivePy.archive import archive_files, extract_archive, archive_folders

class ArchiveTestClass(unittest.TestCase, archive_folders):
 
    def __init__(self, *args, **kwargs):
 
        super(ArchiveTestClass, self).__init__(*args, **kwargs)

        self.commit = "master_789hk4"
        self.output_pth = "./tests/test_archive/"
        self.archive_fls = ["./tests/test_data1.csv", "./tests/test_data2.csv"]
        self.fl = ".test_data1.zip"

        self.af = archive_files(self.commit, self.output_pth, self.archive_fls)
        self.archive_dirs = self.af.archive_dirs
        self.current_dir = self.af.current_dir
        self.archive_dir = self.af.archive_dir
        self.zipped_fl = "{}.zip".format(self.commit)

        self.setUp()

        import pdb; pdb.set_trace()

    def setUp(self):

        remove_dirs(self.archive_dirs)

    def test_create_archive_str(self):
        
        self.af.create_archive_str()
        self.assertTrue(all([os.path.exists(d) for d in self.archive_dirs]))
        remove_dirs(self.archive_dirs)

    def test_move_to_current(self):
        
        create_files(self.archive_fls)
        self.assertTrue(all([os.path.exists(d) for d in self.archive_fls]))
        self.af.create_archive_str()
        self.af.move_to_current()
        self.assertTrue(all([os.path.exists(os.path.join(self.current_dir, os.path.basename(d))) for d in self.archive_fls]))

    def test_create_archive(self):
        create_files(self.archive_fls)
        self.af.create_archive_str()
        self.af.move_to_current()
        self.af.create_archive()
        self.assertTrue(os.path.exists(os.path.join(self.archive_dir, self.zipped_fl)))