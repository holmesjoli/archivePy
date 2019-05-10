import git
from git import Repo
import os

class options(object):

	def __init__(self, opts):
		"""
		Initiates the options class
		Initiates the options class
        :param opts: a dictionary of options
        :type opts: dct
		"""
		self.message = opts["commit_message"]
		self.add_branch = opts["add_branch"]
		self.add_message = opts["add_message"]

class auto_commit(options):

	def __init__(self, opts):
		"""
		Initiates the auto commit class
		:param opts: a dictionary containing the options
		:type opts: dct
		"""
		options.__init__(self, opts)
		os.environ["PATH"] += os.pathsep + "../PortableGit/bin/"

		self.g = git.cmd.Git(os.getcwd())
		self.repo = Repo(os.getcwd())
		self.check_master()
		if self.ui == '1':
			self.add_commit()
			self.parse_commit_result()
		else:
			print("Exiting. Please switch to master branch.")

	def check_master(self):
		"""Checks to see if the master branch is active"""
		self.branch = self.repo.active_branch.name

		if self.branch != "master":
			self.ui = input("Master branch is not active. Continue? \n1:Yes \n2:No\n")

			while(self.ui not in ['1', '2']):
				self.ui = input("Please select 1 or 2")
		else:
			self.ui = '1'

	def add_commit(self):
		"""Adds and commits message then pushes to the branch it's on."""
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
