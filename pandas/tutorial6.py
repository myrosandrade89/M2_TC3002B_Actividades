import pandas as pd
pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print("Renaming:")
print(f"\n {reviews.rename(columns={'points': 'score'})}")
print(f"\n {reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})}")
print(f"\n {reviews.rename_axis('wines', axis='rows').rename_axis('fields', axis='columns')}")

print("\nCombining:")
canadian_youtube = pd.read_csv("./CAvideos/CAvideos.csv")
british_youtube = pd.read_csv("./GBvideos/GBvideos.csv")
print(f"\n {pd.concat([canadian_youtube, british_youtube])}")
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
print(f"\n {left.join(right, lsuffix='_CAN', rsuffix='_UK')}")