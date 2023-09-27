import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("./wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print("Exercise 1:")
median_points = reviews.points.median()
print(f"\n {median_points}")

print("\nExercise 2:")
countries = reviews.country.unique()
print(f"\n {countries}")

print("\nExercise 3:")
reviews_per_country = reviews.country.value_counts()
print(f"\n {reviews_per_country}")

print("\nExercise 4:")
centered_price = reviews.price - reviews.price.mean()
print(f"\n {centered_price}")

print("\nExercise 5:")
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(f"\n {bargain_wine}")

print("\nExercise 6:")
tropical = reviews.description.map(lambda desc: "tropical" in desc).sum()
fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([tropical, fruity], index=['tropical', 'fruity'])
print(f"\n {descriptor_counts}")

print("\nExercise 7:")
def stars(row):
    if row.country == 'Canada' or row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
print(f"\n {star_ratings}")