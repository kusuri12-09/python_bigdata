import pandas as pd

# 리스트로 DataFrame 객체 생성
data = [['A', 1], ['B', 2], ['C', 3]]
df = pd.DataFrame(data, columns=['col1', 'col2'])
print(df)

# 딕셔너리로 DataFrame 객체 생성
data = {'col1': ['A', 'B', 'C'], 'col2': [1, 2, 3]}
df = pd.DataFrame(data)
print(df)

# CSV 파일로 DataFrame 객체 생성
df = pd.read_csv(r'D:\python\bigdata\make-up-work-class\pandas\data.csv')
print(df)
