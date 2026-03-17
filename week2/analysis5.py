import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('DSMH/example_data/sample_2/smartphone_usage_time.csv')

print('median = ', np.median(data)) #중앙값
print('min = ', np.min(data),'\n') #최솟값

plt.boxplot(data, vert=False) # 수평의 상자도형 (False의 F는 대문자로)
plt.show()