import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, Binarizer
from scipy import stats

df = pd.read_csv('data.csv')

df = df.drop(['id', 'Unnamed: 32'], axis=1)
df.diagnosis = df.diagnosis.map({'M': 1, 'B': 0})
df = df.replace('?', np.nan)
df = df.dropna()

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df_cleaned_outliers = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

X = df_cleaned_outliers.drop('diagnosis', axis=1)

# Standardization/Normalization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
print("--- Standardized Data Head ---")
print(X_scaled_df.head())

# Discretization/Binarization
# Binarize 'radius_mean': 1 if radius_mean > 15, 0 otherwise
binarizer = Binarizer(threshold=0.08)
compactness_mean_binned = binarizer.fit_transform(X[['compactness_mean']])
X_scaled_df['compactness_mean_bin'] = compactness_mean_binned.flatten()
print("\n--- Binarized Feature Head ---")
print(X_scaled_df[['compactness_mean', 'compactness_mean_bin']].head())

# Aggregation (Creating a new feature by calculating mean of 'mean' features)
mean_features = [col for col in X.columns if 'mean' in col]
X_scaled_df['aggregated_mean_feature'] = X_scaled_df[mean_features].mean(axis=1)
print("\n--- Aggregated Feature Head ---")
print(X_scaled_df[['aggregated_mean_feature']].head())