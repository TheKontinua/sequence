import pandas as pd
from random import randint

# Read the CSV and create a dataframe                                                                                           
df = pd.read_csv('bikes.csv', index_col="bike_id")

# Fix typos
df.loc[df['status'] == 'Available', 'status'] = 'available'
df.loc[df['status'] == 'Flat tire', 'status'] = 'broken'

# Which rows are missing statuses?
missing_mask = df['status'].isnull()

# List them
missing_ids = list(df[missing_mask].index)
print(f"These bikes have no status:{missing_ids}")

# Just keep the rows that do not have null statuses
df = df[~missing_mask]

# Show the shape of the dataframe
(row_count, col_count) = df.shape
print(f"*** Basics ***")
print(f"Bikes: {row_count:,}")
print(f"Columns: {col_count}")

# Purchase price stats
print("\n*** Purchase Price ***")
series = df["purchase_price"]
print(f"Lowest:{series.min()}")
print(f"Highest:{series.max()}")
print(f"Mean:{series.mean():.2f}")

# Brand stats
print("\n*** Brands ***")
series = df["brand"]
series_counts = series.value_counts()
print(f"{series_counts}")

print("\n*** First Bike ***")
row = df.iloc[0]
print(f"{row}")

print("\n*** Some Bike ***")                                                                                                    
brand = df['brand'][2969341]                                                                                         
print(f"{brand}") 

print("\n*** Status ***")
series = df["status"]
missing = series.isnull()
print(f"{missing.sum()} bikes have no status.")
series_counts = series.value_counts()
for value in series_counts.index:
    print(f"{series_counts.loc[value]} bikes are \"{value}\"")                                                                      

df.to_csv('bikes2.csv')