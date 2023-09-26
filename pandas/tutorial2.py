import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

print("Native accessors:")
print(reviews)
print(f"\n {reviews.country}" )
print(f"\n {reviews['country']}")
print(f"\n {reviews['country'][0]}")

print("\nIndexing in pandas:")
print(f"\n {reviews.iloc[0]}")
print(f"\n {reviews.iloc[:, 0]}")
print(f"\n {reviews.iloc[:3, 0]}")
print(f"\n {reviews.iloc[1:3, 0]}")
print(f"\n {reviews.iloc[[0, 1, 2], 0]}")
print(f"\n {reviews.iloc[-5:]}")
print(f"\n {reviews.loc[0, 'country']}")
print(f"\n {reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]}")

print("\nManipulating the index:")
print(f"\n {reviews.set_index('title')}")

print("\nConditional selection:")
print(f"\n {reviews.country == 'Italy'}")
print(f"\n {reviews.loc[reviews.country == 'Italy']}")
print(f"\n {reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]}")
print(f"\n {reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]}")
print(f"\n {reviews.loc[reviews.country.isin(['Italy', 'France'])]}")
print(f"\n {reviews.loc[reviews.price.notnull()]}")

print("\nAssigning data:")
reviews['critic'] = 'everyone'
print(f"\n {reviews['critic']}")
reviews['index_backwards'] = range(len(reviews), 0, -1)
print(f"\n {reviews['index_backwards']}")