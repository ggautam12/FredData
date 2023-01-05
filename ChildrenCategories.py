import csv

# Open a CSV file for writing
with open('children_categories.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['id', 'name', 'parent_id'])

    # Insert the values
    categories = [{'id': 32262, 'name': 'Business Cycle Expansions & Contractions', 'parent_id': 1}, {'id': 33936, 'name': 'Business Surveys', 'parent_id': 1}, {'id': 32436, 'name': 'Construction', 'parent_id': 1}, {'id': 33940, 'name': 'Emissions', 'parent_id': 1}, {'id': 33955, 'name': 'Expenditures', 'parent_id': 1}, {'id': 33490, 'name': 'Finance Companies', 'parent_id': 1}, {'id': 32216, 'name': 'Health Insurance', 'parent_id': 1}, {'id': 97, 'name': 'Housing', 'parent_id': 1}, {'id': 3, 'name': 'Industrial Production & Capacity Utilization', 'parent_id': 1}, {'id': 32429, 'name': 'Manufacturing', 'parent_id': 1}, {'id': 33959, 'name': 'Patents', 'parent_id': 1}, {'id': 6, 'name': 'Retail Trade', 'parent_id': 1}, {'id': 33441, 'name': 'Services', 'parent_id': 1}, {'id': 33492, 'name': 'Technology', 'parent_id': 1}, {'id': 33202, 'name': 'Transportation', 'parent_id': 1}, {'id': 33203, 'name': 'Wholesale Trade', 'parent_id': 1}]
    print(categories)

    for category in categories:
        print(category)
        writer.writerow([category['id'], category['name'], category['parent_id']])