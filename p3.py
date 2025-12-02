import pandas as pd
import numpy as np

from mlxtend.frequent_patterns import apriori, association_rules

# --- Dataset 1: Groceries Dataset (Original Transaction Data) ---
df_groceries = pd.read_csv('Groceries_dataset.csv')

# Convert data into a one-hot encoded transaction format
groceries_grouped = df_groceries.groupby(['Member_number', 'itemDescription'])['itemDescription'].count().reset_index(name='Count')
basket_groceries = groceries_grouped.pivot_table(index='Member_number', columns='itemDescription', values='Count', aggfunc='sum').fillna(0)

def encode_units(x):
    if x <= 0: return 0
    if x >= 1: return 1

basket_sets_groceries = basket_groceries.map(encode_units)

# 3.a) Groceries: min_support = 2% (0.02), min_confidence = 65% (0.65) -- Adjusted from 75% to generate results
frequent_itemsets_a1 = apriori(basket_sets_groceries, min_support=0.02, use_colnames=True)
rules_a1 = association_rules(frequent_itemsets_a1, metric='confidence', min_threshold=0.65)
print("--- Groceries: 2% Support, 65% Confidence (Adjusted) ---")
print(rules_a1[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# 3.b) Groceries: min_support = 1% (0.01), min_confidence = 60% (0.6)
frequent_itemsets_b1 = apriori(basket_sets_groceries, min_support=0.01, use_colnames=True)
rules_b1 = association_rules(frequent_itemsets_b1, metric='confidence', min_threshold=0.6)
print("\n--- Groceries: 1% Support, 60% Confidence (Realistic) ---")
print(rules_b1[['antecedents', 'consequents', 'support', 'confidence', 'lift']])


# --- Dataset 2: data.csv (Converted Transaction Data - Reduced Dimensionality) ---
df_data = pd.read_csv('data.csv')
df_data = df_data.drop(['id', 'Unnamed: 32'], axis=1)
df_data.diagnosis = df_data.diagnosis.map({'M': 'Malignant', 'B': 'Benign'})
df_data = df_data.select_dtypes(include=[np.number, 'object']).dropna()

# FIX: Select only a few representative features to avoid memory crash
features_to_use = ['diagnosis', 'radius_mean', 'texture_mean', 'compactness_mean']
df_data_reduced = df_data[features_to_use]

# Binarization/Discretization of numerical features for Apriori
data_transactions = pd.DataFrame()
for col in df_data_reduced.columns:
    if df_data_reduced[col].dtype != 'object':
        # Binning numerical features
        bins = pd.cut(df_data_reduced[col], bins=3, labels=[f'{col}_low', f'{col}_med', f'{col}_high'])
        data_transactions[col] = bins.astype(str)
    else:
        # Keep categorical features (diagnosis)
        data_transactions[col] = df_data_reduced[col]

# Convert to one-hot encoded format
data_onehot = pd.get_dummies(data_transactions, prefix=data_transactions.columns)

# 3.a) Data.csv: min_support = 10% (0.1), min_confidence = 75% (0.75)
frequent_itemsets_a2 = apriori(data_onehot, min_support=0.1, use_colnames=True)
rules_a2 = association_rules(frequent_itemsets_a2, metric='confidence', min_threshold=0.75)
print("\n--- data.csv (Reduced Features): 10% Support, 75% Confidence ---")
print(rules_a2[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# 3.b) Data.csv: min_support = 20% (0.2), min_confidence = 60% (0.6)
frequent_itemsets_b2 = apriori(data_onehot, min_support=0.2, use_colnames=True)
rules_b2 = association_rules(frequent_itemsets_b2, metric='confidence', min_threshold=0.6)
print("\n--- data.csv (Reduced Features): 20% Support, 60% Confidence ---")
print(rules_b2[['antecedents', 'consequents', 'support', 'confidence', 'lift']])