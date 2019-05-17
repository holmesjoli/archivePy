import unittest
import os

from utilsPy.folder_structure import remove_dirs, create_files
from archivePy.archive import archive_setUp, archive_output


class ArchiveTestClass(unittest.TestCase, archive_setUp):

    def __init__(self, *args, **kwargs):

        super(ArchiveTestClass, self).__init__(*args, **kwargs)

        self.commit = "master_789hk4"
        self.zipped_fl = "{}.zip".format(self.commit)
        self.output_pth = "./archivePy/tests/test_archive/"
        self.fls = ["./archivePy/tests/test_data1.csv",
                    "./archivePy/tests/test_data2.csv"]

        archive_setUp.__init__(self, self.output_pth, self.fls)
        remove_dirs(self.archive_dirs)

    def test_create_archive_str(self):
        self.create_archive_str()
        self.assertTrue(all([os.path.exists(d) for d in self.archive_dirs]))
        remove_dirs(self.archive_dirs)

    def test_move_to_current(self):
        create_files(self.fls)
        self.assertTrue(all([os.path.exists(d) for d in self.fls]))
        self.create_archive_str()
        self.move_to_current()
        self.assertTrue(all([os.path.exists(os.path.join(self.current_dir, os.path.basename(d))) for d in self.fls]))

    def test_create_archive(self):
        create_files(self.fls)
        self.create_archive_str()
        self.move_to_current()

        ca = archive_output(self.commit, self.output_pth, self.fls)
        ca.create_archive()
        self.assertTrue(os.path.exists(os.path.join(self.archive_dir, self.zipped_fl)))
        