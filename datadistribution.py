import numpy as np
data = [10, 20, 30, 40, 50, 60, 70]
#quarties,quantiles,percentiles
quartiles = np.percentile(data, [25, 50, 75])
print("Quartiles:", quartiles)
quantiles = np.quantile(data, np.linspace(0.1, 0.9, 9))
print("Quantiles:", quantiles)
percentiles = np.percentile(data, np.arange(10, 100, 10))
print("Percentiles:", percentiles)
pentiles = np.percentile(data, [20, 40, 60, 80])
print("Pentiles:", pentiles)
deciles = np.percentile(data, np.arange(10, 100, 10))
print("Deciles:", deciles)
min_val = np.min(data)
print("Minimum:", min_val)
q1 = np.percentile(data, 25)
print("First Quartile (Q1):", q1)
median = np.median(data)
print("Median:", median)
q3 = np.percentile(data, 75)
print("Third Quartile (Q3):", q3)
max_val = np.max(data)
print("Maximum:", max_val)
five_number_summary = [min_val, q1, median, q3, max_val]
print("Five-number summary:", five_number_summary)

import numpy as np
data = np.random.normal(loc=50, scale=15, size=1000)
data = np.array(data)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
outliers = data[(data < (q1 - 1.5 * iqr)) | (data > (q3 + 1.5 * iqr))]
print(outliers)
