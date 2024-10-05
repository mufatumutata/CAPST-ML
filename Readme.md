Title/Research Q: "Impact of Online Consumer Feedback on Restaurant Longevity"

Description: 

preprocess_econ_data.py :- This file preprocesses the data by removing all entries of businesses that aren't restaurants; we do this so we are only evaluating restaurants.

preprocess2_econ_data.py :- This file preprocesses the data by making sure the restaurants in our dataset have complete data (nothing from the necessary independent variables and dependent variable is missing). It also extracts a datapoint called "RestaurantsPriceRange2" from 'attributes' and puts it in a new column as an integer (it was initially a string).

descriptive_statistics.py :- This file provides the descriptice statistics of the entire dataset (used for the data and description section).

lasso_regression.py:- Runs a LASSO regression on our data.

logistic_regression.py:- Runs a logistic regression on our data.

ridge_regression.py:- Runs a Ridge regression on our data.

YELP_filtered_businesses:- the final preprocessed dataset we are working with

Bugs: None