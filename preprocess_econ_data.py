import json

# Path to the original dataset file
input_file_path = '/Users/mustafaelahi/Desktop/YELP OPEN DATASET/yelp_academic_dataset_business.json'
# Path to the new file with only restaurants and food places
output_file_path = 'yelp_restaurants_and_food_only.json'

def is_restaurant_or_food(categories):
    """Determine if the business is a restaurant or serves food based on its categories."""
    if not categories:
        return False
    food_related_keywords = ['Restaurants', 'Food', 'Cafes', 'Bakeries', 'Bars', 'Fast Food']
    return any(keyword in categories for keyword in food_related_keywords)

# Open the input file and the output file
with open(input_file_path, 'r', encoding='utf-8') as infile, \
     open(output_file_path, 'w', encoding='utf-8') as outfile:
    
    # Iterate over each line in the input file
    for line in infile:
        business = json.loads(line)
        # Check if the business is a restaurant or related to food
        if is_restaurant_or_food(business.get('categories', '')):
            # Write the business to the output file
            json.dump(business, outfile)
            outfile.write('\n')  # Add newline to separate JSON objects

print("Filtering complete. Output saved to:", output_file_path)
