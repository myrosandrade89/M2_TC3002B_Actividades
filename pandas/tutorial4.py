import pandas as pd
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print("Groupwise analysis:")
print(f"\n {reviews.groupby('points').points.count()}")
print(f"\n {reviews.groupby('points').price.min()}")
print(f"\n {reviews.groupby('winery').apply(lambda df: df.title.iloc[0])}")
print(f"\n {reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])}")
print(f"\n {reviews.groupby(['country']).price.agg([len, min, max])}")

print("\nMulti-indexes:")
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(f"\n {countries_reviewed}")
mi = countries_reviewed.index
print(f"\n {type(mi)}")
print(f"\n {countries_reviewed.reset_index()}")

print("\nSorting:")
countries_reviewed = countries_reviewed.reset_index()
print(f"\n {countries_reviewed.sort_values(by='len')}")
print(f"\n {countries_reviewed.sort_values(by='len', ascending=False)}")
print(f"\n {countries_reviewed.sort_index()}")
print(f"\n {countries_reviewed.sort_values(by=['country', 'len'])}")