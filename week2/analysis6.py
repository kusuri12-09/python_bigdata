import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

path = r'D:\python\bigdata\dataset\elm_students_tall_weight.xlsx'
data = pd.DataFrame(pd.read_excel(path))

plt.scatter(data.height, data.weight)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()