#CLUSTERING
import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("petals_sepals.csv")
print(df.head())
print()
fig = px.scatter(df, x = "petal_size", y = "sepal_size")
fig.show()
X = df.iloc[:, [0, 1]].values
print()
print(X)
WCSS = []
for i in range(1, 11):
  kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
  kmeans.fit(X)
  WCSS.apend(kmeans.inertia_)