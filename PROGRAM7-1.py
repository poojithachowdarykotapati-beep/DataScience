import pandas as pd
data={
    'Name':['priya','kiran','Lakshmi','Ravi'],
    'Department':['CSE','DS','DS','CSE'],
    'Year':[4,3,4,3],
    'Marks':[98,89,95,94]
}
df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n1.Group by Department:")
group1=df.groupby('Department')
for name,group in group1:
    print("\nDepartment:",name)
    print(group)
print("\nAverage Marks by Department:")
print(df.groupby('Department')['Marks'].mean())
print("\n2.Group by Department and year:")
group2=df.groupby(['Department','Year'])
for name,group in group2:
    print("\nGroup:",name)
    print(group)
print("\nAverage Marks by Department and Year:")
print(df.groupby(['Department','Year'])['Marks'].mean())