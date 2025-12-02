import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)

# Data Loading and Pre-processing (from Q1 and Q2)
df = pd.read_csv('data.csv')
df = df.drop(['id', 'Unnamed: 32'], axis=1)
df.diagnosis = df.diagnosis.map({'M': 1, 'B': 0})
df = df.replace('?', np.nan)
df = df.dropna()

X = df.drop('diagnosis', axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_cls = pd.DataFrame(X_scaled, columns=X.columns)

# 6. Perform density-based clustering (DBSCAN)
data_cluster = X_cls

# Define parameter ranges to test
eps_values = [0.5, 1.0, 1.5, 2.0]
min_samples_values = [3, 5, 7]
dbscan_results = []

# Evaluate cluster quality by changing the algorithm's parameters
for eps_val in eps_values:
    for min_samples_val in min_samples_values:
        db = DBSCAN(eps=eps_val, min_samples=min_samples_val)
        labels = db.fit_predict(data_cluster)

        # Calculate number of clusters (excluding noise points, labeled -1)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

        # Calculate Silhouette Score only if more than one cluster (and not all noise) is found
        score = -1
        if n_clusters > 1:
            score = silhouette_score(data_cluster, labels)
        elif n_clusters == 1:
            # If only one cluster is found (excluding noise), score is 0
            score = 0

        noise_points = list(labels).count(-1)

        dbscan_results.append({
            'eps': eps_val,
            'min_samples': min_samples_val,
            'Clusters Found': n_clusters,
            'Noise Points': noise_points,
            'Silhouette Score': score
        })

print("--- DBSCAN Cluster Quality Evaluation ---")
dbscan_df = pd.DataFrame(dbscan_results)
print(dbscan_df)