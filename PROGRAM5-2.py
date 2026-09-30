import pandas as pd
import matplotlib.pyplot as plt
data={
    'Python':[80,78,95,85],
    'Java':[73,80,85,82],
    'C++':[70,75,85,90]
}
df=pd.DataFrame(
    data,
    index=['Student1','Student2','Student3','Student4']
)
print("DataFrame:")
print(df)
df.plot(
    kind='bar',
    figsize=(8,5)
)
plt.title("Student Marks in Different Programming Languages")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.tight_layout()
plt.show()