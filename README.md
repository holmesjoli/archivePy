# dataArchivePy

## Data Archiving and Versioning

One issue that I've often faced in analytics is how to connect output (data, visualizations, and reports) with the code used to generate that output. The team will deliver output to the client/partner and then continue to develop the code base. If the client/partner has a specific question then the team has to back-track to figure out which code was used to create that particular output. A lot of teams archive their output use timestamps, e.g. data_20171019_124590. While this can be a good method for data archiving for some teams, this method doesn't easily allow an analyst to be able to backtrack and see which code created that specific output. This can also create issues if data is created and then used as an input farther downstream because it means that the filename is changing whenever the data are re-processed. 

The dataArchivePy package combines several steps important to data archiving purposes into one package.

First, we commit our code and extract the branch, unique 6-character hash, and message to be used when naming the archive. 

Next we run the archiving functions which create a directory structure that serves two functions a) easy access to the current data and b) an archive of data can be extracted using the unique 6-character hash. 

### Example File Structure

```
Data/
    Processed/
        Current/
            data.csv
            summary_data.csv
        Archive/
            master_90r68d.zip
Deliverables/
    Current/
        fig1.png
        fig2.png
    Archive/
        master_90r68d.zip
```

### Commit and Archive Sample Code

```
import os
import pandas as pd
import numpy as np

from dataArchivePy.archive import archive_files, extract_archive
from dataArchivePy.gitTools import auto_commit
from dataArchivePy.cli_args import parseArguments

class main(object):

    def __init__(self, opts):
        """
        Initiates the main function, which does data management and then calls 
        to autocommit and archive the data
        """

        self.df = pd.DataFrame({"col1": [1,2,3,4],
                                "col2": ["a", "b", "c", "d"]})

        self.output_dir = "./dataArchivePy/tests/test_archive"
        self.archive_fls = ["./dataArchivePy/tests/test_archive/data.csv"]

        self.dm()

        ac = auto_commit(opts)
        archive_files(ac.commit, self.output_dir, self.archive_fls).archive()

    def dm(self):
        """
        Performs data management steps
        """

        self.df_copy = self.df.copy()
        self.df_copy["new_col"] = np.where(self.df_copy["col1"] > 1, 1, 0)
        self.df_copy.to_csv(os.path.join(self.archive_fls[0]))

if __name__ == "__main__":

    opts = parseArguments()
    main(opts)
```

1. Naviate the repository's root directory
2. In the command line type: `python dataArchivePy/test.py -ab -am -c "April Monthly"`

* Adding `-c "Commit Message"` is mandatory, otherwise the script will throw an error message
* `--add_branch` (`-ab`) is an optional argument. Adding `-ab` will add the branch to the beginning of the archive zip filename. 
* `--add_message` (`-am`) is an option argument. Adding `-am` will add the commit message to the end of the archive zip filename.