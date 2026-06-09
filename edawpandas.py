import pandas as pd
df = pd.DataFrame({
 'student_id': [1, 2],
 'math': [85, 90],
 'science': [88, 92]
})
melted_df = pd.melt(df, id_vars=['student_id'], value_vars=['math', 'science'])
print(melted_df)
 #use of melt fucntion defines
import pandas as pd
df = pd.DataFrame({
 'student_id': [1, 1, 2, 2],
 'subject': ['math', 'science', 'math', 'science'],
 'marks': [85, 88, 90, 92]
})
pivoted_df = df.pivot(index='student_id', columns='subject', values='marks')
print(pivoted_df)

import pandas as pd
df_csv = pd.read_csv('student_dataset.csv')
print(df_csv.isnull().sum())
df_mean = df_csv[grade].mean() # type: ignore
print(df_mean)
