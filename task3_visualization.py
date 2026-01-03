import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset .csv")
df = df[['Aggregate rating', 'Cuisines', 'City', 'Votes']]
df.dropna(inplace=True)

# Histogram of ratings
plt.figure(figsize=(8,5))
plt.hist(df['Aggregate rating'], bins=10)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Rating count bar plot
rating_counts = df['Aggregate rating'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=rating_counts.index, y=rating_counts.values)
plt.title("Count of Each Rating")
plt.show()

# Cuisine-wise average rating
df['Cuisines'] = df['Cuisines'].str.split(', ')
df_explode = df.explode('Cuisines')

avg_rating_cuisine = (
    df_explode.groupby('Cuisines')['Aggregate rating']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
sns.barplot(x=avg_rating_cuisine.values, y=avg_rating_cuisine.index)
plt.title("Top 10 Cuisines by Average Rating")
plt.show()

# City-wise average rating
avg_rating_city = (
    df.groupby('City')['Aggregate rating']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
sns.barplot(x=avg_rating_city.values, y=avg_rating_city.index)
plt.title("Top 10 Cities by Average Rating")
plt.show()

# Votes vs Rating
plt.figure(figsize=(8,5))
sns.scatterplot(x='Votes', y='Aggregate rating', data=df)
plt.title("Votes vs Rating")
plt.show()
