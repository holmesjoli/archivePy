import os
import pandas as pd
import numpy as np

from dataArchivePy.etl import archive_etl

class main(object):

    def __init__(self):
        """
        Initiates the main function, which does data management and then calls 
        to autocommit and archive the data
        """

        self.output_dir = "./dataArchivePy/tests/test_archive"
        self.fls = ["./dataArchivePy/tests/test_archive/data.csv"]

        self.dm()

        archive_etl(self.output_dir, self.fls)

    def dm(self):
        """
        Performs data management steps
        """
        self.df = pd.DataFrame({"col1": [1,2,3,4],
                                "col2": ["a", "b", "c", "d"]})
        self.df["new_col"] = np.where(self.df["col1"] > 1, 1, 0)
        self.df.to_csv(os.path.join(self.fls[0]))

if __name__ == "__main__":

    main()