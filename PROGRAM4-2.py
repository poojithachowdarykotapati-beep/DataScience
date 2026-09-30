import pandas as pd
index=pd.MultiIndex.from_tuples(
    [
        ('Computing','Aiml'),
        ('Computing','Ds'),
        ('Science','Physics'),
        ('Science','Biology')
    ],
    name=['Department','Branch']
)
data=pd.DataFrame(
    {
        '2025':[58,87,29,88],
        '2026':[80,83,59,96]
    },
    index=index
)
print("Original Tabular Data:")
print(data)
unstacked_data=data.unstack()
print("\nData after unstack():")
print(unstacked_data)
stacked_data=unstacked_data.stack()
print("\nData after stack():")
print(stacked_data)