import numpy as np
from scipy import stats
data = np.random.normal(loc=50, scale=15, size=1000)
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True)[0][0]
std_dev = np.std(data)
variance = np.var(data)
confidence_interval = stats.norm.interval(0.95, loc=mean, scale=std_dev/np.sqrt(len(data)))
print(f"Mean: {mean:.2f}, Median: {median:.2f}, Mode: {mode:.2f}")
print(f"Std Dev: {std_dev:.2f}, Variance: {variance:.2f}")
print(f"95% Confidence Interval: {confidence_interval}")
import numpy as np
data = np.random.normal(loc=50, scale=15, size=1000)
sample = np.random.choice(data, size=100, replace=False)
print("Mean:", np.mean(sample))
print("Standard Deviation:", np.std(sample))

import pandas as pd
strata = pd.cut(data, bins=5)
stratified_sample = pd.Series(data).groupby(strata).apply(lambda x: x.sample(10)).values
print("Stratified Sample Mean:", np.mean(stratified_sample))

clusters = [data[i*100:(i+1)*100] for i in range(10)]
selected_clusters = np.random.choice(clusters, size=3, replace=False)
cluster_sample = np.concatenate(selected_clusters)
print("Cluster Sample Mean:", np.mean(cluster_sample))