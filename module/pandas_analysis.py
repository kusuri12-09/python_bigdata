import pandas as pd
import matplotlib.pyplot as plt

path = r'D:\python\bigdata\asset\highschool_samples.xlsx'
data = pd.DataFrame(pd.read_excel(path))

plt.hist(data.height, label='bins=10', bins=10)
plt.legend()
plt.show()