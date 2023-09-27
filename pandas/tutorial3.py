import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
import numpy as np

print("Summary functions:")
print(f"\n {reviews.points.describe()}")
print(f"\n {reviews.taster_name.describe()}")
print(f"\n {reviews.points.mean()}")
print(f"\n {reviews.taster_name.unique()}")
print(f"\n {reviews.taster_name.value_counts()}")

print("\nMaps:")
review_points_mean = reviews.points.mean()
print(f"\n {reviews.points.map(lambda p: p - review_points_mean)}")
def remean_points(row):
    row.points = row.points - review_points_mean
    return row
print(f"\n {reviews.head(1)}")
review_points_mean = reviews.points.mean()
print(f"\n {reviews.points - review_points_mean}")
print(f"\n {reviews.country + ' - ' + reviews.region_1}")