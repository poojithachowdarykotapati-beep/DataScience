import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=[40,45,50,55,58,60,62,65,68,70,73,75,77,80,83,86,88,90,95,97]
df=pd.DataFrame({'Marks':data})
print("Observed Data:")
print(df)
plt.figure(figsize=(8,5))
sns.histplot(df['Marks'],bins=6,kde=False)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8,5))
sns.kdeplot(df['Marks'],fill=True)
plt.title("Density plot of Marks")
plt.xlabel("Marks")
plt.ylabel("Density")
plt.tight_layout()
plt.show()