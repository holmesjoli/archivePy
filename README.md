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

### Example Code

```
import pandas as pd
import numpy as np

df = pd.DataFrame({"col1": [1,2,3,4],
                   "col2": ["a", "b", "c", "d"]})

df_copy = df.copy()
df_copy["new_col"] = np.where(df_copy["col1"] > 1, 1, 0)



```

1. Naviate the repositories root
2. `python dataArchivePy/test.py -ab -am -c "April Monthly"`