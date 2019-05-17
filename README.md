# Data Archive Py

<!-- badges: start -->
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/eb0770e299c0493e84c5054f441ac6b2)](https://www.codacy.com/app/holmesjoli/archivePy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=holmesjoli/archivePy&amp;utm_campaign=Badge_Grade)
[![Build status](https://travis-ci.org/holmesjoli/archivePy.svg?branch=master)](https://travis-ci.org/holmesjoli/archivePy)
[![Codecov test coverage](https://codecov.io/gh/holmesjoli/archivePy/branch/master/graph/badge.svg)](https://codecov.io/gh/holmesjoli/archivePy?branch=master)
<!-- badges: end -->

## Data Archiving and Versioning

One issue that I've often faced in analytics is how to connect output (data, visualizations, and reports) with the code used to generate that output. The team will deliver output to the client/partner and then continue to develop the code base. If the client/partner has a specific question then the team has to back-track to figure out which code was used to create that particular output. A lot of teams archive their output use timestamps, e.g. data_20171019_124590. While this can be a good method for data archiving for some teams, this method doesn't easily allow an analyst to be able to backtrack and see which code created that specific output. This can also create issues if data is created and then used as an input farther downstream because it means that the filename is changing whenever the data are re-processed.

The archivePy package combines several steps important to data archiving purposes into one package.

First, we commit our code and extract the branch, unique 6-character hash, and message to be used when naming the archive.

Next we run the archiving functions which create a directory structure that serves two functions a) easy access to the current data and b) an archive of data can be extracted using the unique 6-character hash.

### Example File Structure

```txt
Project/
|___Data/
|   |___Processed/
|       |___Current/
|              data.csv
|              summary_data.csv
|       |___Archive/
|                master_90r68d.zip
|___Deliverables/
|   |___Current/
|       fig1.png
|       fig2.png
|   |___Archive/
|       master_90r68d.zip
```

### Commit and Archive Sample Code

Sample Code is located `./archivePy/archivePy/sample_code.py`

1.  Navigate the repository's root directory, e.g. `cd archivepy`
2.  To write out data to the Current folder type `python archivePy/sample_code.py`
3.  To write out data to the Current folder and Archive the data type `python archivePy/sample_code.py -c "commit message"`

-   Adding the `--commit` (`-c`) command triggers the script to add the data/output to the Archive folder
-   Adding the `--add_branch` (`-b`) command is an optional argument. Including this command will add the branch name to the beginning of the archive zip filename.
-   Adding the `--add_message` (`-m`) command is an optional argument. Including this command will add the message to the end of the archive zip filename.
