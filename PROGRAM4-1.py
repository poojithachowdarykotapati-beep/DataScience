import pandas as pd
index=[
    ['Computing','Computing','Science','Science'],
    ['Aiml','Ds','Physics','Biology']
]
multi_index=pd.MultiIndex.from_arrays(
    index,
    names=['Department','Branch']
)
marks=pd.Series(
    [78,98,88,95],
    index=multi_index
)
print("Original Series:")
print(marks)
print("\nData for Computing:")
print(marks.loc['Computing'])
print("\nData for Aiml:")
print(marks.loc[('Computing','Aiml')])
print("\nData for Science:")
print(marks.loc['Science'])