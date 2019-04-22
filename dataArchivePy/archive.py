import os
import shutil
import pandas as pd
import zipfile

from utilsPy.folder_structure import create_dirs, remove_files
from utilsPy.config import read_yaml

class archive_setUp(object):

    def __init__(self, output_dir, fls):
        """
        The folders to create in the archiving process
        """
        
        self.output_dir = output_dir
        self.fls = fls

        self.pth = os.path.abspath(os.path.dirname(__file__))
        config = read_yaml(os.path.join(self.pth, "../config.yaml"))

        self.archive_dir = os.path.join(self.output_dir, config["archive_dirs"]["Archive"])
        self.current_dir = os.path.join(self.output_dir, config["archive_dirs"]["Current"])
        self.archive_dirs = [self.archive_dir, self.current_dir]

    def create_archive_str(self):
        """Creates the archive structure"""

        create_dirs(self.archive_dirs)
    
    def move_to_current(self):
        """Moves the files to the Current folder"""

        [os.remove(os.path.join(self.current_dir, fl)) for fl in os.listdir(self.current_dir)]
        [shutil.move(fl, os.path.join(self.current_dir, os.path.basename(fl))) for fl in self.fls]

class write_output(archive_setUp):

    def __init__(self, output_dir, fls):
        """
        Writes archive fls out to the Current folder
        :param output_dir: the path to create the file archive
        :type output_dir: str
        :param fls: a list of the files to archive
        :type fls: list
        """

        archive_setUp.__init__(self, output_dir, fls)

    def run(self):
        """
        Writes out files to the current folder
        """

        self.create_archive_str()
        self.move_to_current()

class archive_output(archive_setUp):
    
    def __init__(self, commit, output_dir, fls):
        """
        Writes archive fls out to the Current folder and archives the same files with a commit id
        :param commit: the commit id
        :type commit: str
        :param output_dir: the path to create the file archive
        :type output_dir: str
        :param fls: a list of the files to archive
        :type fls: list
        """
        
        archive_setUp.__init__(self, output_dir, fls)
        self.commit = commit
            
    def create_archive(self):
        """
        Copies files from the Current folder
        Adds them to the archive
        Zips files using the commit id as the filename
        """
        
        self.zipped_fl = "{}.zip".format(self.commit)
        shutil.make_archive(base_name = self.commit, format = "zip", root_dir = self.current_dir)
        shutil.move(self.zipped_fl , os.path.join(self.archive_dir, self.zipped_fl))

    def run(self):
        """Combines all the archiving steps"""

        self.create_archive_str()
        self.move_to_current()
        self.create_archive()

class extract_archive(object):

	def __init__(self, commit, archive_dir, fl):
		"""
		Parses an archive to extract a specific commit
		:param commit: the commit id 
		:type commit: str
		:param archive_dir: the path to the data archives
		:type archive_dir: str
		:param fl: the file to extract from the archive
		:type fl: str
		"""

		fls = os.listdir(archive_dir)
		zip_archive = [fl for fl in fls if commit in fl][0]

		archive = zipfile.ZipFile(os.path.join(archive_dir, zip_archive), 'r')

		if fl.endswith(".csv"):
			self.df = pd.read_csv(archive.open(fl))
		else:
			raise Exception("Expecting .csv file extension")

