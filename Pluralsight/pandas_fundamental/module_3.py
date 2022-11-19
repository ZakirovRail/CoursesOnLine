import pandas as pd

df = pd.read_csv("artwork_data.csv", nrows=5)
print(df)
"""
     id  ...                                                url
0  1035  ...  http://www.tate.org.uk/art/artworks/blake-a-fi...
"""


df = pd.read_csv("artwork_data.csv", nrows=5, index_col="id")
print(df)

"""
     accession_number  ...                                                url
id                     ...                                                   
1035           A00001  ...  http://www.tate.org.uk/art/artworks/blake-a-fi...
1036           A00002  ...  http://www.tate.org.uk/art/artworks/blake-two-...
"""

df = pd.read_csv("artwork_data.csv", nrows=5, index_col="id", usecols=["id", "artist"])
print(df)

"""
              artist
id                  
1035   Blake, Robert
1036   Blake, Robert
1037   Blake, Robert
1038   Blake, Robert
1039  Blake, William
"""

COLS_TO_USE = ["id", "artist", "title", "medium", "year", "acquisitionYear", "height", "width", "units"]

df = pd.read_csv("artwork_data.csv", index_col="id", usecols=COLS_TO_USE)
print(df)



