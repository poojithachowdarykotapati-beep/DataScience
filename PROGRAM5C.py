import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data=np.random.randn(2000)
sns.histplot(data, kde=True)
plt.title("Histogram and density")
plt.show()