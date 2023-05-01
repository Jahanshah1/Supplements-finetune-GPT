import csv
import json

with open('nutrition_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    prompt_completion_pairs = []
    for row in csv_reader:
        completion = f"{row['product_name']} by {row['brand_name']} is a {row['product_category']} that {row['product_description']}. It comes in {row['number_of_flavors']} different flavors, including {row['top_flavor_rated']}. The product has an overall rating of {row['overall_rating']}, based on {row['number_of_reviews']} reviews. The average flavor rating is {row['average_flavor_rating']}. The price is {row['price']} SAR, which is {row['price_per_serving']} SAR per serving. {row['verified_buyer_number']} verified buyers rated the product an average of {row['verified_buyer_rating']}."
        prompt = f"Can you give me a summary of {row['brand_name']} {row['product_name']}?"
        prompt_completion_pairs.append({"prompt": prompt, "completion": completion})

with open('prompt_completion_pairs.json', mode='w') as json_file:
    json.dump(prompt_completion_pairs, json_file, indent=4)
