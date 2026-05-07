import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
print(df.head())
sns.histplot(data=df, x='total_bill', bins=10, kde=True)
print(sns.histplot)
plt.show()
sns.boxplot(data=df, x='day', y='total_bill')
plt.show()
import matplotlib.pyplot as plt
sns.distplot(df['total_bill'], bins=10, kde=True)
plt.show()
import seaborn as sns
df = sns.load_dataset('tips')
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

corr = df.select_dtypes(include='number').corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.show()
