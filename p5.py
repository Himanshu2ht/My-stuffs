import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

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

# 5. Apply simple K-means algorithm for clustering
data_cluster = X_cls

# a) Compare performance by varying K (1 to 10) and plot MSE (Inertia)
mse_values = []
k_range = range(1, 11)
for k in k_range:
    # We first calculate the overall inertia for the elbow method
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(data_cluster)
    mse_values.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_range, mse_values, marker='o')
plt.title('MSE (Inertia) vs. Number of Clusters (K)')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (Lower is Better)')
plt.grid(True)
plt.show()

# b) Comparing performance by varying algorithm parameters (e.g., K=2 vs K=3)
# Optimal K often appears at the 'elbow' of the plot, let's compare K=2 and K=3
kmeans_2 = KMeans(n_clusters=2, n_init=10, random_state=42)
labels_2 = kmeans_2.fit_predict(data_cluster)
score_2 = silhouette_score(data_cluster, labels_2)

kmeans_3 = KMeans(n_clusters=3, n_init=10, random_state=42)
labels_3 = kmeans_3.fit_predict(data_cluster)
score_3 = silhouette_score(data_cluster, labels_3)

print("\n--- K-means Comparison (K=2 vs K=3) ---")
print(f"K=2 | Inertia: {kmeans_2.inertia_:.2f} | Silhouette Score: {score_2:.4f}")
print(f"K=3 | Inertia: {kmeans_3.inertia_:.2f} | Silhouette Score: {score_3:.4f}")

# c) Plot a line graph depicting MSE obtained after each iteration for a given K (e.g., K=3)
# Custom function to track and plot inertia per iteration
def track_inertia_and_plot(X, k, max_iterations=10):
    # Initialize KMeans with n_init=1 and warm_start=True to enable iterative fitting
    # We must ensure max_iter is 1 for the loop to control the total iterations
    kmeans_tracker = KMeans(n_clusters=k, init='k-means++', n_init=1, max_iter=1, random_state=42)
    kmeans_tracker.warm_start = True # Enable warm start for incremental fitting

    inertia_per_iter = []

    # Run loop to manually control iterations
    for i in range(max_iterations):
        # We only call fit() here, and the warm_start=True ensures it continues from previous state
        kmeans_tracker.fit(X)
        inertia_per_iter.append(kmeans_tracker.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_iterations + 1), inertia_per_iter, marker='o')
    plt.title(f'K-means (K={k}) Convergence: MSE vs. Iteration')
    plt.xlabel('Iteration Number')
    plt.ylabel('MSE (Inertia)')
    plt.grid(True)
    plt.show()

# Plotting the convergence for K=3
track_inertia_and_plot(data_cluster, k=3, max_iterations=10)