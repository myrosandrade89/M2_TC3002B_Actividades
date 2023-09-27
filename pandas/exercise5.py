import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print("Exercise 1:")
dtype = reviews.points.dtype
print(dtype)

print("\nExercise 2:")
point_strings = reviews.points.astype('str')
print(point_strings.dtype)

print("\nExercise 3:")
n_missing_prices = pd.isnull(reviews.price).sum()
print(n_missing_prices)

print("\nExercise 4:")
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)