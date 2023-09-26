import pandas as pd

df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

print("DataFrames:")

print(df)

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

print(df)

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])

print(df)

print("\nSeries:")

s = pd.Series([1, 2, 3, 4, 5])

print(s)

s = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

print(s)

print("\nReading data files:")

wine_reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print(wine_reviews.shape)

print(wine_reviews.head())

