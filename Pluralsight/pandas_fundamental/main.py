import pandas as pd
import numpy as np


my_numpy_array = np.random.rand(3)
# print(my_numpy_array)

my_first_series = pd.Series(np.random.rand(3))
print(my_first_series)

my_first_df = pd.DataFrame(np.random.rand(3, 2))
print(my_first_df)




