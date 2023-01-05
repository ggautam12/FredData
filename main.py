import csv
import requests

# Set the API endpoint URL and the API key
api_endpoint = 'https://api.stlouisfed.org/fred/category/children?'
api_key = "8078491c31e3e27d9742197720fd7182"

# Open a CSV file for writing
with open('children_categories.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['id:', 'name', 'parent_id'])

    # Iterate over the range of category IDs
    #this code gets all categories
    for category_id in range(0, 14):
    # for category_id in range(32990,32992):
        # Set the query parameters for the current category ID
        query_params = {
            "api_key": '8078491c31e3e27d9742197720fd7182',
            'category_id': category_id,
            'file_type': 'json'
        }

        # Make the API request
        response = requests.get(api_endpoint, params=query_params)

        if response.status_code == 200:
            data = response.json()
            categories = data['categories']

            # Write the category data to the CSV file
            for category in categories:
                writer.writerow([category['id'], category['name'], category['parent_id']])
        else:
            # The request was not successful, so we should handle the error
            print(f"An error occurred: {response.status_code}")

