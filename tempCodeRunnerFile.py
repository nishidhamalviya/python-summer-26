import pandas as pd
strata = pd.cut(data, bins=5)
stratified_sample = pd.Series(data).groupby(strata).apply(lambda x: x.sample(10)).values
print("Stratified Sample Mean:", np.mean(stratified_sample))