import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print("Exercise 1:")
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})

print("\nExercise 2:")
reindexed = reviews.rename_axis('wines', axis='rows')

print("\nExercise 3:")
gaming_products = pd.read_csv("./top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("./top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
combined_products = pd.concat([gaming_products, movie_products])

print("\nExercise 4:")
powerlifting_meets = pd.read_csv("./powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("./powerlifting-database/openpowerlifting.csv")
powerlifting_combined = powerlifting_meets.set_index('MeetID').join(powerlifting_competitors.set_index('MeetID'))