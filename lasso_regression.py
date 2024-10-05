import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.pipeline import make_pipeline


data_path = '/Users/mustafaelahi/Desktop/ECON1680_CODE/YELP_filtered_businesses.json'
# Load JSON data
with open(data_path, 'r') as file:
    data = [json.loads(line) for line in file]

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

X = df[['stars', 'review_count', 'RestaurantsPriceRange2']]  # Features
y = df['is_open']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

# Define the Lasso Regression pipeline
lassoReg = make_pipeline(StandardScaler(), Lasso())

# Define the range of alphas to search over
alphas = np.logspace(-6, 0, 50) * np.sqrt(X.shape[0])  # Logarithmic scale
params = {'lasso__alpha': alphas}

# Set up the grid search with cross-validation
gsLasso = GridSearchCV(lassoReg, params, n_jobs=-1, cv=10, scoring='neg_mean_squared_error')

# Fit the grid search to the data
gsLasso.fit(X, y)

# Find the best alpha value and print it, adjusted for the training set size
best_alpha = gsLasso.best_params_['lasso__alpha'] / np.sqrt(X_train.shape[0])
print(f"Best alpha: {best_alpha}")

# Run Lasso regression using the best found alpha value
lassoReg = make_pipeline(StandardScaler(), Lasso(alpha=best_alpha))
lassoReg.fit(X_train, y_train)

# Extract coefficients and add to the dataframe
df_results = pd.DataFrame({'Variable': X.columns, 'Coeff LASSO': lassoReg.named_steps['lasso'].coef_})
print(df_results)


