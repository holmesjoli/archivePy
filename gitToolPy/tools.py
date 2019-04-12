import git
from git import Repo
import os
import shutil
import re
import subprocess
import zipfile

import pandas as pd

class auto_commit(object):

	def __init__(self, message, add_message, add_branch):
		"""

		Initiates the auto commit class
		:param message: the commit message
		:type message: string
		:param add_message: indicator for if the message should be added to the commit
		:type add_message: boolean
		:param add_branch: indicator for if the branch name should be added to the commit
		:type add_branch: boolean
		"""
		
		os.environ["PATH"] += os.pathsep + "../PortableGit/bin/"

		self.message = message
		self.add_message = add_message
		self.add_branch = add_branch

		self.g = git.cmd.Git(os.getcwd())
		self.repo = Repo(os.getcwd())
		self.add_commit()
		self.parse_commit_result()

	def check_master(self):
		"""Checks to see if the master branch is active"""

		self.branch = self.repo.active_branch.name
		
		if self.branch != "master":
			ui = int(input("Master branch is not active. Continue? \n1:Yes \n2:No\n"))

			while(ui not in [1,2]): 
				ui = input("Please select 1 or 2")
		
	def add_commit(self):
		"""Adds and commits message then pushes to the branch it's on."""

		self.check_master()
		self.g.add("--a")
		self.commit_result = self.g.commit("--m", self.message, "--allow-empty")
		self.g.push("origin", self.branch)

	def parse_commit_result(self):
		"""Parses the commit result and returns the branch and commit id as a string."""

		self.hash = self.commit_result[self.commit_result.find("[")+1:self.commit_result.find("]")].split()[1]

		self.commit = "{}".format(self.hash)
		if self.add_message:
			self.commit = "{}_{}".format(self.commit, self.message)
		if self.add_branch:
			self.commit = "{}_{}".format(self.branch, self.commit)


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
