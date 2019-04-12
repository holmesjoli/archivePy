import os
import shutil
import pandas as pd
import zipfile

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
		
		fls = os.listdir(pth)
		zip_archive = [fl for fl in fls if commit in fl][0]

		archive = zipfile.ZipFile(os.path.join(pth, zip_archive), 'r')

		if fl.endswith(".csv"):
			self.df = pd.read_csv(archive.open(fl))
		else:
			raise Exception("Expecting .csv file extension")

class archive_files(object):

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

		self.commit = commit
		self.output_pth = output_pth
		self.archive_fls = archive_fls
		
		self.zipped_fl = "{}.zip".format(self.commit)
		
		new_pth = os.path.join(self.output_pth, "Current")
		[os.remove(os.path.join(new_pth, fl)) for fl in os.listdir(new_pth)]
		[shutil.move(fl, os.path.join(new_pth, fl)) for fl in self.archive_fls]
		
		shutil.make_archive(base_name = self.commit, format = "zip", root_dir = new_pth)
		shutil.move(self.zipped_fl , os.path.join(self.output_pth, "Archive", self.zipped_fl))

	def create_archive_str(self, output_pth):
		"""
		Creates the Archive Structure
		"""

		dirs = ["Archive", "Current"]
		[os.mkdir(d) for d in dirs if not os.path.isdir(self.output_pth)]
