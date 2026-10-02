import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ==========================================
# TASK 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

# 1. Generate movie data structure for the project
np.random.seed(42)
data = {
    "Title": [f"Movie {i}" for i in range(1, 101)],
    "Genre": np.random.choice(
        ["Action", "Drama", "Comedy", "Sci-Fi", "Horror"], 100
    ),
    "Release_Year": np.random.randint(2010, 2026, 100),
    "IMDb_Rating": np.random.uniform(5.5, 9.5, 100),
    "Gross_Revenue_Millions": np.random.uniform(10, 500, 100),
}
df = pd.DataFrame(data)

print("--- 1. Data Structure & Summary ---")
print(df.info())
print("\n--- 2. Missing Values Check ---")
print(df.isnull().sum())
print("\n--- 3. Statistical Insights ---")
print(df.describe())

# 4. Answering a meaningful question: What is the average rating per genre?
print("\n--- 4. Average IMDb Rating by Genre ---")
genre_ratings = df.groupby("Genre")["IMDb_Rating"].mean().sort_values(ascending=False)
print(genre_ratings)


# ==========================================
# TASK 3: DATA VISUALIZATION
# ==========================================

# Set style for visuals
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 5))

# Chart 1: Distribution of IMDb Ratings (Histogram)
plt.subplot(1, 2, 1)
sns.histplot(df["IMDb_Rating"], kde=True, color="purple", bins=15)
plt.title("Distribution of IMDb Ratings", fontsize=14, pad=10)
plt.xlabel("IMDb Rating")
plt.ylabel("Count of Movies")

# Chart 2: Revenue vs IMDb Rating (Scatter Plot)
plt.subplot(1, 2, 2)
sns.scatterplot(
    data=df,
    x="IMDb_Rating",
    y="Gross_Revenue_Millions",
    hue="Genre",
    palette="deep",
    alpha=0.8,
)
plt.title("IMDb Rating vs Gross Revenue", fontsize=14, pad=10)
plt.xlabel("IMDb Rating")
plt.ylabel("Revenue (in Millions $)")

# Adjust layout and save the visualization dashboard image
plt.tight_layout()
plt.savefig("imdb_insights_dashboard.png", dpi=300)
plt.show()

print("\n🎉 EDA and Visualization completed successfully!")
print("📊 Dashboard saved as 'imdb_insights_dashboard.png' in your folder.")
