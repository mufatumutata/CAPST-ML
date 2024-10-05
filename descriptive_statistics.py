import pandas as pd
import numpy as np

filtered_dataset_path = '/Users/mustafaelahi/Desktop/ECON1680_CODE/YELP_filtered_businesses.json'

# Load the filtered dataset
df_restaurants = pd.read_json(filtered_dataset_path, lines=True)

# Since the data is already filtered and cleaned, directly compute summary statistics for the variables of interest
variables_of_interest = ['stars', 'review_count', 'RestaurantsPriceRange2', 'is_open']
df_filtered = df_restaurants[variables_of_interest]

# Rename columns for clarity (if needed)
df_filtered.rename(columns={'stars': 'Ratings',
                            'review_count': 'Review Counts',
                            'RestaurantsPriceRange2': 'Price Level',
                            'is_open': 'Restaurant Open Status'}, inplace=True)

# Ensure correct data types
df_filtered['Price Level'] = pd.to_numeric(df_filtered['Price Level'], errors='coerce')
df_filtered['Restaurant Open Status'] = df_filtered['Restaurant Open Status'].astype(int)

# Compute summary statistics
summary_statistics = df_filtered.describe(include=[np.number]).T

# Add count of non-null for Restaurant Open Status manually 
summary_statistics.loc['Restaurant Open Status', 'count'] = df_filtered['Restaurant Open Status'].notnull().sum()

# Print the summary statistics
print(summary_statistics)


