# %%
"""Using one of the three datasets to demonstrate k-means clustering using the scikit learn package (50 points). 
Be sure to review the readings before you start on this assignment. 
Calculate the sum of least square error for each different values of 'k'. 
Using Matplotlib determine the optimal number of clusters (k) using the elbow method along with a brief explanation (50 points) . 
Finally plot the optimal clusters with their centroids along with a brief explanation (50 points). Comment your code as needed."""

# %%
#1. Use the arrhythmia data set found at https://archive.ics.uci.edu/dataset/5/arrhythmia. Demonstrate k-means clustering 
#using the scikit learn package

#import the packages I need
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# %%
#import data and clean it up before using

# According to UCI metadata: 279 attributes + 1 target column = 280 columns
col_count = 280
col_names = [f"attr_{i}" for i in range(1, col_count + 1)]
data = pd.read_csv("/Users/a14806/Desktop/arrhythmia.csv", header=None, names=col_names)





# %%
#clean the data/null values
# Replace '?' with NaN
data = data.replace('?', np.nan).astype(float)

# Drop rows with too many missing values 
data = data.dropna()

# %%
# need to normalize and split the data now: 
#split
X = data.iloc[:, :-1]  # All columns except last (class label)
y = data.iloc[:, -1]   # Actual arrhythmia classification label

#this splitting allows me to test some of the data to see if model is working correctly


# %%
#standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# %%
#demonstrate k-mean clustering with scikit
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# %%
# add cluster assignment to dataframe
data["cluster"] = clusters

#reduce size so we can visualize this data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

data["PC1"] = X_pca[:, 0]
data["PC2"] = X_pca[:, 1]

#Visualize the results
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=data,
    x="PC1",
    y="PC2",
    hue="cluster",
    palette="viridis",
    s=60
)
plt.title("K-Means Clusters (Arrhythmia Dataset, PCA 2D)")
plt.show()

# %%
#2 Calculate the sum of least square error for each different values of 'k'. 

#
sse = []                 # will store sum of squared errors for each k
#try k values 1 though 10
k_values = range(1, 11)  # try k = 1 to k = 10

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    #inertia_ is SSE that we need
    sse.append(kmeans.inertia_)  # inertia_ = SSE

    print (kmeans)

# %%
#3 Using Matplotlib determine the optimal number of clusters (k) using the elbow method along with a brief explanation (50 points) . 
#plot and visualize SSE vs. k from above (elbow method)
#The elbow method is a simple way to figure out how many clusters we should use in k-means. As we try different values of k, the total error gets smaller because the
#  data is being split into more groups. At first, each extra cluster helps a lot and really lowers the error. But eventually, adding more 
# clusters doesn’t make much of a difference anymore. That spot where the improvement levels off (the concept of diminishing returns) is the “elbow,” and it’s usually the best number of clusters to choose.

plt.figure(figsize=(10, 6))
plt.plot(k_values, sse, marker='o')
plt.xticks(k_values)
plt.xlabel("Number of clusters (k)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.title("Elbow Method: SSE for Different k")
plt.grid(True)
plt.show()

# print SSE values so we know exactly what graph is saying
for k, error in zip(k_values, sse):
    print(f"k = {k}, SSE = {error}")
    #k of three is the optimal number of clusters since after 3 increasing the number of clusters has little impact in lowering SSE (error)

# %%


# %%
#4 Plot the optimal clusters with their centroids along with a brief explanation
#k=3 is the optimal according to elbow chart
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# add clusters to data
data['cluster'] = clusters

PC1 = data['PC1']
PC2 = data['PC2']

# put the cluster centroids onto PCA space
centroids_pca = pca.transform(kmeans.cluster_centers_)

#plot my clusters and the centroids of each now in a graph

plt.figure(figsize=(10, 6))

sns.scatterplot(
    x=PC1,
    y=PC2,
    hue=data['cluster'],
    palette='viridis',
    s=60,
    edgecolor='black'
)

# Plot the centroids ( look at these cool shapes and colors!!! so cool:)
plt.scatter(
    centroids_pca[:, 0],
    centroids_pca[:, 1],
    c='pink',
    s=200,
    marker='X',
    label='Centroids'
)

plt.title(f"K-Means Clusters (k = {optimal_k}) with Centroids (PCA 2D)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()

# %%
"""Explanation of our K-means clusters and centroid: Once we figure out the best number of clusters using the elbow method (3), we run k-means again 
using that optimal value of k (3 in this case). The PCA step helps turn the high-dimensional data into 2 dimensions 
so we can actually see how the clusters look. Each point in the scatterplot represents a patient from the arrhythmia dataset, 
and the colors show which cluster they were assigned to. The pink “X” markers are the centroids, which are basically the average location 
of each cluster and represent the center of each group. Plotting everything together helps us check whether the clusters make sense."""


