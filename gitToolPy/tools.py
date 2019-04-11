import git
from git import Repo
import os
import re
import subprocess

class auto_commit(object):

	def __init__(self, message, opts):
		"""

		Initiates the auto commit class
		:param message: the commit message
		:type message: string
		"""
		os.environ["PATH"] += os.pathsep + "../PortableGit/bin/"

		self.message = message
		self.add_message = opts["add_message"]

		self.g = git.cmd.Git(os.getcwd())
		self.repo = Repo(os.getcwd())
		self.auto_commit()
		self.parse_commit_result()

	def check_master(self):
		"""Checks to see if the master branch is active"""

		self.branch = self.repo.active_branch.name
		
		if self.branch != "master":
			ui = int(input("Master branch is not active. Continue? \n1:Yes \n2:No\n"))

			while(ui not in [1,2]): 
				ui = input("Please select 1 or 2")
		
	def auto_commit(self):
		"""Adds and commits message then pushes to the branch it's on."""

		self.check_master()
		self.g.add("--a")
		self.commit_result = self.g.commit("--m", self.message, "--allow-empty")
		self.g.push("origin", self.branch)

	def parse_commit_result(self):
		"""Parses the commit result and returns the branch and commit id as a string."""

		self.hash = self.commit_result[self.commit_result.find("[")+1:self.commit_result.find("]")].split()[1]

		if self.add_message: 
			self.commit = "{}_{}_{}".format(self.branch, self.hash, self.message)
		else:
			self.commit = "{}_{}".format(self.branch, self.hash)
