import csv
import requests

# Set the API endpoint URL and the API key
api_endpoint = 'https://api.stlouisfed.org/fred/series/observations?series_id='
api_key = "8078491c31e3e27d9742197720fd7182"


# Set the query parameters for the current category ID
query_params = {
    "api_key": '8078491c31e3e27d9742197720fd7182',
    'series_id': 'CUUR0000SEFR',
    'file_type': 'json',
    'realtime_start': '2013-08-14',
    'realtime_end': '2023-01-02',
    'count': '84'
}
# Make the API request
response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    data = response.json()
    print(data)
    seriesCUUR0000SEFR = data['observations']
    print(seriesCUUR0000SEFR)
    # Write the series data to the CSV file
    # Open a CSV file for writing
    with open('sweets.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['realtime_start', 'realtime_end', 'date', 'value'])
        for sweets in seriesCUUR0000SEFR:
            print(sweets)
            writer.writerow([sweets['realtime_start'], sweets['realtime_end'], sweets['date'], sweets['value']])

else:
    # The request was not successful, so we should handle the error
    print(f"An error occurred: {response.status_code}")

