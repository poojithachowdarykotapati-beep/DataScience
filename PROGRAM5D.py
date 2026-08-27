import numpy as np
import matplotlib.pyplot as plt
X=np.random.rand(70)
Y=np.random.rand(70)
plt.scatter(X,Y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("scatter_plot.png")
plt.show()