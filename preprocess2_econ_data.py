import json

# Paths to input and output JSON files
input_file_path = '/Users/mustafaelahi/Desktop/ECON1680_CODE/yelp_restaurants_and_food_only.json'
output_file_path = '/Users/mustafaelahi/Desktop/ECON1680_CODE/YELP_filtered_businesses.json'

def is_valid_business(business):
    """
    Determine if a business entry should be included in the filtered output.
    
    A business is considered valid if:
    - It is open (is_open is not None).
    - It has a star rating (stars is not None).
    - It has a review count (review_count is not None).
    - It has a dictionary of attributes (to ensure 'RestaurantsPriceRange2' can be checked).
    - It has a 'RestaurantsPriceRange2' attribute that is a digit string (indicating a valid price range).
    - It belongs to a category related to food or restaurants.
    
    Parameters:
    - business: A dictionary representing a business entry.
    
    Returns:
    - True if the business meets all the criteria; False otherwise.
    """
    # Check for mandatory fields and attributes dictionary presence
    if business.get('is_open') is None or business.get('stars') is None or \
       business.get('review_count') is None or not isinstance(business.get('attributes'), dict):
        return False
    
    # Check for valid 'RestaurantsPriceRange2' attribute
    price_range_str = business['attributes'].get('RestaurantsPriceRange2')
    if price_range_str is None or not price_range_str.isdigit():
        return False
    
    # List of keywords indicating a food-related business
    food_related_keywords = ['Restaurants', 'Food', 'Cafes', 'Bakeries', 'Bars', 'Fast Food']
    categories = business.get('categories', '')
    
    # Check if any of the food-related keywords are in the categories
    return any(keyword in categories for keyword in food_related_keywords)

# Open the input and output files
with open(input_file_path, 'r', encoding='utf-8') as infile, \
     open(output_file_path, 'w', encoding='utf-8') as outfile:
    # Iterate over each line (business entry) in the input file
    for line in infile:
        business = json.loads(line)  # Convert JSON string to dictionary
        
        # Check if the business is valid according to our criteria
        if is_valid_business(business):
            # Convert 'RestaurantsPriceRange2' to integer and remove it from attributes
            price_range = int(business["attributes"].pop("RestaurantsPriceRange2"))
            
            # Add 'RestaurantsPriceRange2' as a separate column
            business["RestaurantsPriceRange2"] = price_range
            
            # Write the modified business dictionary as a JSON string to the output file
            json.dump(business, outfile)
            outfile.write('\n')  # Ensure each business entry is on a new line

# Notify user of completion and output file location
print("Filtering complete. Output saved to:", output_file_path)
