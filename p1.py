import pandas as pd
import numpy as np
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

print(df_cleaned_outliers.head())