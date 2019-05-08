from dataArchivePy.archive import write_output, archive_output
from dataArchivePy.gitTools import auto_commit
from dataArchivePy.cli_args import parseArguments

class archive_etl(object):

    def __init__(self, output_dir, fls):
        """
        Initiates the ETL for archiving
        :param output_dir: the output directory
        :type output_dir: str
        :param fls: the files to move to Current folder
        :type fls: list
        """
        self.opts = parseArguments()
        self.output_dir = output_dir
        self.fls = fls

        if self.opts["commit_message"] is not None:
            self.message = self.opts["commit_message"]
            self.add_branch = self.opts["add_branch"]
            self.add_message = self.opts["add_message"]
            ac = auto_commit(self.opts)
            self.commit = ac.commit
            archive_output(self.commit, output_dir, fls).run()

        else:
            write_output(output_dir, fls).run()
