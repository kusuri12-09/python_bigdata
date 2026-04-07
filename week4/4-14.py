import pandas as pd

df = pd.DataFrame([
   ['20225001','A', 77],
   ['20225001','B', 80],
   ['20225002','A', 85],
   ['20225002','B', 82],
   ['20225003','A', 95],
   ['20225003','B', 90]],
    columns=['ID_num','Subject', 'Score'])

print(df, '\n')
group_mean = df.groupby(by='Subject').mean(numeric_only=True)
print(group_mean)
