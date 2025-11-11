# -------------------------------------------------------------
# Clustering on the IRIS dataset using DBSCAN and Hierarchical Clustering
# -------------------------------------------------------------

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

# -------------------------------------------------------------
# Load the Iris dataset
# -------------------------------------------------------------
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print("Shape of dataset:", X.shape)
X.head()

# -------------------------------------------------------------
# Standardize the features
# -------------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------------------------------------
# 1️⃣ DBSCAN Clustering
# -------------------------------------------------------------
dbscan = DBSCAN(eps=0.8, min_samples=5)
db_labels = dbscan.fit_predict(X_scaled)

# Add cluster labels to the dataframe
X['DBSCAN_Cluster'] = db_labels

# Check number of clusters
print("\nDBSCAN Cluster Labels:", np.unique(db_labels))

# Evaluate using silhouette score (ignore -1 noise points)
valid_clusters = db_labels[db_labels != -1]
valid_points = X_scaled[db_labels != -1]
if len(np.unique(valid_clusters)) > 1:
    score = silhouette_score(valid_points, valid_clusters)
    print("Silhouette Score (DBSCAN):", score)
else:
    print("Not enough clusters for silhouette score.")

# Visualize DBSCAN Clusters
plt.figure(figsize=(8, 5))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=db_labels, cmap='plasma', s=60)
plt.title("DBSCAN Clustering on Iris Dataset")
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# -------------------------------------------------------------
# 2️⃣ Hierarchical Clustering (Agglomerative)
# -------------------------------------------------------------
# Perform Agglomerative Clustering
agg_cluster = AgglomerativeClustering(n_clusters=3, linkage='ward')
agg_labels = agg_cluster.fit_predict(X_scaled)

X['Agglomerative_Cluster'] = agg_labels

# Evaluate Hierarchical Clustering
score_agg = silhouette_score(X_scaled, agg_labels)
print("\nSilhouette Score (Hierarchical):", score_agg)

# Visualize Hierarchical Clusters
plt.figure(figsize=(8, 5))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=agg_labels, cmap='rainbow', s=60)
plt.title("Hierarchical Clustering on Iris Dataset")
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# -------------------------------------------------------------
# Dendrogram Visualization
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
Z = linkage(X_scaled, method='ward')
dendrogram(Z, truncate_mode='level', p=5)
plt.title("Dendrogram for Hierarchical Clustering")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()
