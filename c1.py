# Hierarchical clustering
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv(r"C:\Users\HP\Desktop\MSX-INT-Python-012\DataScience\datasets\seeds-less-rows.csv")

# remove the grain species from the DataFrame, save for later
# ['Kama Wheat', 'Rosa Wheat', 'Canadian Wheat']
varieties = list(ds.pop('grain_variety'))

# extract the measurements as a NumPy array
samples = ds.values

# Perform hierarchical clustering on samples using the
# linkage() function with the method='complete' keyword argument.
# Assign the result to mergings.

mergings = linkage(samples, method='complete')

# Plot a dendrogram using the dendrogram() function on mergings,
# specifying the keyword arguments labels=varieties, leaf_rotation=90,
# and leaf_font_size=6.

plt.figure(figsize=(12,6))
dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=13,
           )
plt.title('Heirarchical Clustering on Wheat Vraieties',fontsize=20)
plt.show()

# Plot based on Class
for i in range(0, pca_2d.shape[0]):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2', 'Noise'])
plt.title('DBSCAN finds 2 clusters and a Noise')
plt.show()