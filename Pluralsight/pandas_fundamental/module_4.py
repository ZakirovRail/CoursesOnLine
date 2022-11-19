import pandas as pd


COLS_TO_USE = ["id", "artist", "title", "medium", "year", "acquisitionYear", "height", "width", "units"]

df = pd.read_csv("artwork_data.csv", index_col="id", usecols=COLS_TO_USE)
print(df)

df.to_pickle("data_frame.pickle")

# *********************************************************************************************************
# count how many arts were created by Francis Bacon
s = df["artist"] == "Bacon, Francis"
print(s.value_counts())
print("*"*40)
"""
False    69151
True        50
Name: artist, dtype: int64
"""

# other way
artist_counts = df["artist"].value_counts()
print(artist_counts["Bacon, Francis"])  # -> 50
# *********************************************************************************************************
# df.loc[Row indexer, Column indexer]

print(df.loc[1035, "artist"])    # get result for particular row

print(df.loc[df["artist"] == "Bacon, Francis", :])    # get results from all rows

# *********************************************************************************************************
# df.iloc[Row indexer, Column indexer]
print(df.iloc[100:300, [0, 1, 4]])
"""
                                  artist  ... acquisitionYear
id                                        ...                
1737   Burne-Jones, Sir Edward Coley, Bt  ...          1927.0
1738   Burne-Jones, Sir Edward Coley, Bt  ...          1927.0
1739   Burne-Jones, Sir Edward Coley, Bt  ...          1927.0
20231  Burne-Jones, Sir Edward Coley, Bt  ...          1927.0
1740   Burne-Jones, Sir Edward Coley, Bt  ...          1927.0
...                                  ...  ...             ...
7329                       Jones, George  ...          1888.0
7330                       Jones, George  ...          1888.0
7331                       Jones, George  ...          1888.0
7332                       Jones, George  ...          1888.0
7333                       Jones, George  ...          1888.0

[200 rows x 3 columns]
"""
# *********************************************************************************************************
print("*-"*40)
print(type[df["height"]])





