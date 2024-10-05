import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
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

# Range of alpha values to explore
alphas = np.linspace(0.01, 5, num=50)
cv_errs = []  # To store the mean squared errors for each alpha
coefs = []  # To store the coefficients for each alpha
MSE = 10  # Initialize MSE with 10
bestalpha = 0  # Initialize best alpha

# Loop over the alphas to find the best one
for a in alphas:
    # Define the Ridge Regression model within a pipeline
    ridgeReg = make_pipeline(StandardScaler(), Ridge(alpha=a))
    ridgeReg.fit(X_train, y_train)  # Fit the model
    y_pred = ridgeReg.predict(X_test)  # Predict on the testing set
    mse = mean_squared_error(y_test, y_pred)  # Calculate MSE
    cv_errs.append(mse)  # Append MSE to list
    coefs.append(ridgeReg['ridge'].coef_)  # Append coefficients to list
    if mse < MSE:  # Check if this is the best alpha so far
        MSE = mse
        bestalpha = a

# Print the best alpha
print(f"Best alpha: {bestalpha}")

# Create a DataFrame for storing coefficients
coefs_df = pd.DataFrame(coefs, index=alphas, columns=X.columns)
coefs_df.index.name = 'Alpha'
coefs_df.columns.name = 'Coefficient'
coefs_df.plot()

# Plotting
plt.figure(figsize=(14, 7))
# Mean Squared Error plot
plt.subplot(1, 2, 1)
plt.plot(alphas, cv_errs, marker='o')
plt.title('MSE vs. Alpha')
plt.xlabel('Alpha')
plt.ylabel('Mean Squared Error')

# Coefficients plot
plt.subplot(1, 2, 2)
plt.plot(coefs_df)
plt.title('Coefficients vs. Alpha')
plt.xlabel('Alpha')
plt.ylabel('Coefficient Value')
plt.legend(coefs_df.columns, loc='upper right', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()
