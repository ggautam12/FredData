import csv
import requests

# Set the API endpoint URL and the API key
api_endpoint = 'https://api.stlouisfed.org/fred/series/observations?series_id='
api_key = "8078491c31e3e27d9742197720fd7182"


# Set the query parameters for the current category ID
query_params = {
    "api_key": '8078491c31e3e27d9742197720fd7182',
    'series_id': 'CUSR0000SAF116',
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
    seriesCUSR0000SAF116 = data['observations']
    print(seriesCUSR0000SAF116)
    # Write the series data to the CSV file
    # Open a CSV file for writing
    with open('alcohol.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['realtime_start', 'realtime_end', 'date', 'value'])
        for alcohol in seriesCUSR0000SAF116:
            print(alcohol)
            writer.writerow([alcohol['realtime_start'], alcohol['realtime_end'], alcohol['date'], alcohol['value']])

else:
    # The request was not successful, so we should handle the error
    print(f"An error occurred: {response.status_code}")

