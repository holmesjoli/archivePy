import git
import os
import re
import subprocess

def setup():
	"""
	Sets up the ability to make automated commits
	"""
	
	print("Running git to add and commit")
	os.environ["PATH"] += os.pathsep + "../PortableGit/bin/"
	g = git.cmd.Git(os.getcwd())
	return g

def git_commit(g, message):
	"""
	Adds and commits message then pushes to the branch it's on.
	:param message: the commit message
	:type message: string
	"""
	if not message:
		raise ValueError("--commit_message not set in arguments")
	g.add("--a")
	commit_result = g.commit("--m", message, "--allow-empty")
	g.push("origin", "master")
	return commit_result

def parse_commit_result(commit_result):
	"""
	Parses the commit result and returns the branch and commit id as a string
	:param commit_result: the commit result from the git push
	:type commit_result: string
	"""
	commit_branch = commit_result[commit_result.find("[")+1:commit_result.find("]")].split()
	branch = commit_branch[0]
	commit = commit_branch[1]
	commit_tag = "{}_{}".format(branch, commit)
	return commit_tag

if __name__ == "__main__":
	g = setup()
	cr = git_commit(g, "test message")
	ct = parse_commit_result(cr)
	print(ct)


