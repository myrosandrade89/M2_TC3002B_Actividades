import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

print("Dtypes:")
print(f"\n {reviews.price.dtype}")
print(f"\n {reviews.dtypes}")
print(f"\n {reviews.points.astype('float64')}")
print(f"\n {reviews.index.dtype}")

print("\nMissing data:")
print(f"\n {reviews[pd.isnull(reviews.country)]}")
print(f"\n {reviews.region_2.fillna('Unknown')}")
print(f"\n {reviews.taster_twitter_handle.replace('@kerinokeefe', '@kerino')}")