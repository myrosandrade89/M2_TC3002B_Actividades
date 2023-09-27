import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print("Exercise 1:")
reviews_written = reviews.groupby('taster_twitter_handle').size()

print("\nExercise 2:")
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

print("\nExercise 3:")
price_extremes = reviews.groupby('variety')['price'].agg([min, max])

print("\nExercise 4:")
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

print("\nExercise 5:")
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()

print("\nExercise 6:")
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)