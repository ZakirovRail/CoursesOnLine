import pandas as pd

COLS_TO_USE = ["id", "artist", "title", "medium", "year", "acquisitionYear", "height", "width", "units"]

df = pd.read_csv("artwork_data.csv", index_col="id", usecols=COLS_TO_USE)

# print(df)

small_df = df.iloc[49980:50019, :].copy()
grouped = small_df.groupby('artist')
print(type(grouped))

for name, group_df in grouped:
    print(name)
    print('*'*50)
    print(group_df)
