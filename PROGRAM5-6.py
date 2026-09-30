import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data={
    'Department':[
        'DS','DS','DS','DS','DS',
        'ECE','ECE','ECE','ECE','ECE',
        'CS','CS','CS','CS','CS'
    ],
    'Marks':[
        80,85,90,75,87,
        65,75,82,70,80,
        60,68,72,76,85
    ]
}
df=pd.DataFrame(data)
print("Data:")
print(df)
plt.figure(figsize=(8,5))
sns.boxplot(
    x='Department',
    y='Marks',
    data=df
)
plt.title("Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.grid(axis='y',linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()