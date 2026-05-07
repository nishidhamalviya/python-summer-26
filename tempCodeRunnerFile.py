import numpy as np

data = np.random.normal(loc=50, scale=15, size=1000)

data = np.array(data)

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1

outliers = data[(data < (q1 - 1.5 * iqr)) | (data > (q3 + 1.5 * iqr))]

print(outliers)