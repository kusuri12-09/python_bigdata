import numpy as np
import pandas as pd
from scipy import stats

path = r'D:\python\bigdata\sample_data\elm_students_tall_weight.xlsx'
x = pd.read_excel(path)

# 평균 계산
print('mean = ', np.average(x), '\n')

# 중앙값 계산
print('median =', np.median(x),'\n')

# 최빈값 계산
print('mode =', stats.mode(x))