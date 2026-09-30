import pandas as pd
df1=pd.DataFrame(
    {
        'Name':['Ravi','gita','Anu'],
        'Marks':[None,78,85],
        'Grade':['A','B',None]
    },
    index=[101,102,103]
)
df2=pd.DataFrame(
    {
        'Name':['Ravi','gita','Kiran'],
        'Marks':[82,98,85],
        'Grade':[None,'A','B']
    },
    index=[101,102,104]
)
print("First DataFrame:")
print(df1)
print("\nSecond DataFrame:")
print(df2)
merged=pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True,
    how='outer',
    suffixes=('_DF1','_DF2')
    )
print("\nMerged DataFrame:")
print(merged)
combined=df1.combine_first(df2)
print("\nDataFrame after combine_first():")
print(combined)