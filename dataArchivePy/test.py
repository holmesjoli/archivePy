import pandas as pd
import numpy as np

from dataArchivePy.archive import archive_files, extract_archive
from dataArchivePy.gitTools import auto_commit
from dataArchivePy.cli_args import parseArguments

class main(object):

    def __init__(self, opts):
        """
        """

        self.df = pd.DataFrame({"col1": [1,2,3,4],
                                "col2": ["a", "b", "c", "d"]})

        self.dm()

        auto_commit(opts)

    def dm(self):
        """
        Performs data management steps
        """

        self.df_copy = self.df.copy()
        self.df_copy["new_col"] = np.where(self.df_copy["col1"] > 1, 1, 0)

if __name__ == "__main__":

    opts = parseArguments()

    main(opts)

    import pdb; pdb.set_trace()