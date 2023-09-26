import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

print("Exercise 1:")
desc = reviews.description
print(desc)

print("\nExercise 2:")
first_description = reviews.description.iloc[0]
print(first_description)

print("\nExercise 3:")
first_row = reviews.iloc[0]
print(first_row)

print("\nExercise 4:")
first_descriptions = reviews.description.iloc[:10]
print(first_descriptions)

print("\nExercise 5:")
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]
print(sample_reviews)

print("\nExercise 6:")
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]
print(df)

print("\nExercise 7:")
df = reviews.loc[0:99, ['country', 'variety']]
print(df)

print("\nExercise 8:")
italian_wines = reviews.loc[reviews.country == 'Italy']
print(italian_wines)

print("\nExercise 9:")
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]
print(top_oceania_wines)