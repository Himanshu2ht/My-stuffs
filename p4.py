import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Data Loading and Pre-processing (from Q1 and Q2)
df = pd.read_csv('data.csv')
df = df.drop(['id', 'Unnamed: 32'], axis=1)
df.diagnosis = df.diagnosis.map({'M': 1, 'B': 0})
df = df.replace('?', np.nan)
df = df.dropna()

X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
X_cls = X_scaled_df
y_cls = y

models = {
    'NaiveBayes': GaussianNB(),
    'KNearest': KNeighborsClassifier(),
    'DecisionTree': DecisionTreeClassifier(random_state=42)
}

metrics_results = []
metrics_list = ['accuracy', 'precision', 'recall', 'f1']

def evaluate_classifier_holdout(model, X_train, X_test, y_train, y_test, method, split):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    metrics_results.append([model.__class__.__name__, method, split, acc, prec, rec, f1])

def evaluate_classifier_cv(model_name, model, X, y, method, split, folds):
    for metric in metrics_list:
        scores = cross_val_score(model, X, y, cv=folds, scoring=metric)
        avg_score = scores.mean()
        metrics_results.append([model_name, method, split,
                                avg_score if metric == 'accuracy' else 0,
                                avg_score if metric == 'precision' else 0,
                                avg_score if metric == 'recall' else 0,
                                avg_score if metric == 'f1' else 0])

# i. Using Holdout method (Random sampling)
# i.a) Training set = 80% Test set = 20%
X_train_80, X_test_20, y_train_80, y_test_20 = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)
for name, model in models.items():
    evaluate_classifier_holdout(model, X_train_80, X_test_20, y_train_80, y_test_20, 'Holdout', '80/20')

# i.b) Training set = 66.6% (2/3rd of total), Test set = 33.3%
X_train_66, X_test_33, y_train_66, y_test_33 = train_test_split(X_cls, y_cls, test_size=0.334, random_state=42)
for name, model in models.items():
    evaluate_classifier_holdout(model, X_train_66, X_test_33, y_train_66, y_test_33, 'Holdout', '66.6/33.3')

# ii. Using Cross-Validation
# ii.a) 10-fold
for name, model in models.items():
    evaluate_classifier_cv(name, model, X_cls, y_cls, 'Cross-Validation', '10-fold', 10)

# ii.b) 5-fold
for name, model in models.items():
    evaluate_classifier_cv(name, model, X_cls, y_cls, 'Cross-Validation', '5-fold', 5)


results_df = pd.DataFrame(metrics_results, columns=['Model', 'Method', 'Split', 'Accuracy', 'Precision', 'Recall', 'F1'])
results_agg = results_df.groupby(['Model', 'Method', 'Split']).max().reset_index()

# Display the comparison table
print("--- Classification Comparison Results ---")
print(results_agg)