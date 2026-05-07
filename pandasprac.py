import pandas as pd
marks = pd.Series([85, 90, 78, 92], index=['Alice', 'Bov', 'CHrlie', 'David'])
print(marks)

data = [['Alice',25],['Bob',34],['Charlie',43]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
df.insert(1,'grades',[80,90,70])
print(df)


import pandas as pd
library = pd.DataFrame({
    'book title': ['python 101', 'data science handbook','AI for beginners'],
    'Author': ['John Doe','John Smith','AI'],
    'year': [2019,2021,2023],
    'available':[True, False, True]
})
library['Genre'] = ['Programming','Data Science','AI']
library = library.drop('year', axis=1)
library['Is Recent'] = [False, True, True]

print(library)