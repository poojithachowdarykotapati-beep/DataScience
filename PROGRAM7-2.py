import pandas as pd
data={
    'Department':['DS','DS','CS','IT','IT','CS'],
    'Marks':[80,85,90,95,89,98],
    'Attendance':[90,85,80,75,95,88]
}
df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)
result=df.groupby('Department').aggregate({
    'Marks':['sum','mean','std'],
    'Attendance':['sum','mean','std']
})
print("\nSummary Statistics:")
print(result)