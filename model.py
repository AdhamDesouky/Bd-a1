from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd

def k_means_clustering(data):
    # Load and preprocess the data
    preprocessed_data = data[['thumbsUpCount']].dropna()

    num_clusters = 3

    X = preprocessed_data.values

    kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)

    clusters = kmeans.fit_predict(X)

    silhouette_avg = silhouette_score(X, clusters)

    # Save the cluster assignments to a text file
    np.savetxt('clusters.txt', clusters, fmt='%d', header='Cluster Assignments')

    # Save the silhouette score to a text file
    with open('silhouette_score.txt', 'w') as file:
        file.write(f'Silhouette Score: {silhouette_avg}')

    print("K-means clustering completed.")
    print("Cluster Assignments:", clusters)
    print("Silhouette Score:", silhouette_avg)

# Ensure the script is only executed when run directly, not when imported
if __name__ == "__main__":
    # Assuming dataset is passed as an argument to this script
    import sys
    if len(sys.argv) != 2:
        print("Usage: python model.py <path_to_dataset>")
        sys.exit(1)

    # Load dataset from file
    dataset = pd.read_csv(sys.argv[1])

    # Call the k_means_clustering function with dataset as an argument
    k_means_clustering(dataset)
