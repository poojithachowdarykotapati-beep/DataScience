import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({'category':['A','B','C'], 'values':[30, 50, 40]})
df.plot(kind='bar', x='category', y='values',)
plt.title("Bar Plot")
plt.show()