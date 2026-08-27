import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.boxplot(data=np.random.randn(200,6))
plt.title("Box Plot")
plt.show()