import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
iris.head()

sns.pairplot(iris, diag_kind='hist')
plt.show()