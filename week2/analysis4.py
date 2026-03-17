import pandas as pd
from matplotlib import pyplot as plt

path = r'D:\python\bigdata\sample_data\gasoline_milk_price.xlsx'
data = pd.DataFrame(pd.read_excel(path))

x = data.year
y1 = data.gasoline
y2 =data.milk

plt.plot(x, y1, linestyle='solid', label='gasoline')  # x와 y1 그래프 작성
plt.plot(x, y2, linestyle='dashed', label='milk')  # x와 y2 그래프 작성

plt.legend(loc='best', ncol=2) # 레이블 표시 방법 
plt.title('change of price')   
plt.show()	              
