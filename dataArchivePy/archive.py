import os
import shutil
import pandas as pd
import zipfile

from utilsPy.folder_structure import create_dirs, remove_files

class archive_folders(object):

    def __init__(self, output_pth):
        """
        The folders to create in the archiving process
        """
        
        self.archive_dir = os.path.join(output_pth, "Archive")
        self.current_dir = os.path.join(output_pth, "Current")
        self.archive_dirs = [self.archive_dir, self.current_dir]

class archive_files(archive_folders):
    
    def __init__(self, commit, output_pth, archive_fls):
        """
        Writes archive fls out to the Current folder and archives the same files with a commit id
        :param commit: the commit id
        :type commit: str
        :param output_pth: the path to create the file archive
        :type output_pth: str
        :param archive_fls: a list of the files to archive
        :type archive_fls: list
        """
        
        archive_folders.__init__(self, output_pth)
        self.commit = commit
        self.output_pth = output_pth
        self.archive_fls = archive_fls
    
    def create_archive_str(self):
        """Creates the archive structure"""

        create_dirs(self.archive_dirs)
    
    def move_to_current(self):
        """Moves the files to the Current folder"""
        
        [os.remove(os.path.join(self.current_dir, fl)) for fl in os.listdir(self.current_dir)]
        [shutil.move(fl, os.path.join(self.current_dir, os.path.basename(fl))) for fl in self.archive_fls]
        
    def create_archive(self):
        """
        Copies files from the Current folder, adds them to the archive, and zips files using the commit id as the filename
        """
        
        self.zipped_fl = "{}.zip".format(self.commit)
        shutil.make_archive(base_name = self.commit, format = "zip", root_dir = self.current_dir)
        shutil.move(self.zipped_fl , os.path.join(self.archive_dir, self.zipped_fl))

    def archive(self):
        """Combines all the archiving steps"""

        self.create_archive_str()
        self.move_to_current()
        self.create_archive()

class extract_archive(object):

	def __init__(self, commit, pth, fl):
		"""
		Parses an archive to extract a specific commit
		:param commit: the commit id 
		:type commit: str
		:param pth: the path to the data archives
		:type pth: str
		:param fl: the file to extract from the archive
		:type fl: str
		"""
		# import pdb; pdb.set_trace()
		fls = os.listdir(pth)
		zip_archive = [fl for fl in fls if commit in fl][0]

		archive = zipfile.ZipFile(os.path.join(pth, zip_archive), 'r')

		if fl.endswith(".csv"):
			self.df = pd.read_csv(archive.open(fl))
		else:
			raise Exception("Expecting .csv file extension")

