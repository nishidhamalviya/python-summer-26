import numpy as np
import time
np_array = np.arange(1000000)
start = time.time()
np_array = np_array * 2
print("numpy array time", time.time() - start)

import sys
import numpy as np
py_list = list(range(1000))
np_array = np.arange(1000)
print("list memory:", sys.getsizeof(py_list))
print("array memory:", np_array.nbytes)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a * b
print("Array a:", a)
print("Array b:", b)
print("Element-wise multiplication:", result)

import numpy as np
import pandas as pd
df = pd.read_csv("stock_prices.csv")
prices = df['close'].to_numpy()
returns = (prices[1:] - prices[-1]) / prices[:-1]
print("Daily return:", returns) #file nhi h isme

import numpy as np
temps = np.array([22.5, 23.0, 21.8, 24.1,22.9])
print("max temp:", np.max(temps))
print("min temp:", np.min(temps))
print("mean temp:", np.mean(temps))

