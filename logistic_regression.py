import pandas as pd
import statsmodels.api as sm
import json

# Path to JSON data file
data_path = '/Users/mustafaelahi/Desktop/ECON1680_CODE/YELP_filtered_businesses.json'

# Load JSON data
with open(data_path, 'r') as file:
    data = [json.loads(line) for line in file]

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Add a constant to the model for the intercept
df['intercept'] = 1.0

# Specify the independent variables (features) and the dependent variable (target)
X = df[['intercept', 'stars', 'review_count', 'RestaurantsPriceRange2']]  # Independent variables
y = df['is_open']  # Dependent variable

# Perform logistic regression
logit_model = sm.Logit(y, X)
result = logit_model.fit(method='newton')

# Print the summary of the regression results
print(result.summary())
