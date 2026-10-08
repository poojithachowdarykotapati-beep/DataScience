import pandas as pd
dates=pd.to_datetime([
    '2026-02-10',
    '2026-02-11',
    '2026-02-12',
    '2026-02-13',
    '2026-02-14',
])
temparature=[25,27,26,29,30]
time_series=pd.Series(
    temparature,
    index=dates
)
print("Time Series")
print(time_series)