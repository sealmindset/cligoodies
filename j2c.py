# The scripts automate the process of extracting structured information from OpenAPI specifications 
# in JSON (swagger) format and converts into a CSV files.

import json
import csv

# Load the JSON file
with open('openapi_connect_api.json', 'r') as file:
    data = json.load(file)

# Prepare CSV headers based on identified entities and elements
headers = ['Entity', 'Operation ID', 'Methods', 'Parameters', 'Responses']

# Initialize rows list for CSV
rows = []

# Function to extract operation details from paths
def extract_operations(methods):
    operations = []
    if isinstance(methods, dict):  # Ensure methods is a dictionary
        for method, details in methods.items():
            if isinstance(details, dict):  # Ensure details are also a dictionary
                operation_id = details.get('operationId', 'N/A')
                method_name = method.upper()
                parameters = ', '.join([param['name'] for param in details.get('parameters', [])]) if 'parameters' in details else 'N/A'
                responses = ', '.join(details.get('responses', {}).keys()) if 'responses' in details else 'N/A'
                operations.append([operation_id, method_name, parameters, responses])
    return operations

# Iterate through paths in the JSON data
for path, methods in data.get('paths', {}).items():
    # Determine entity based on path name
    entity = path.split('/')[2] if len(path.split('/')) > 2 else 'Unknown Entity'
    # Extract operation details for each method in the path
    operations = extract_operations(methods)
    for operation in operations:
        # Append entity to each operation detail for the CSV row
        rows.append([entity] + operation)

# Write to CSV
with open('openapi_json_entities.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(headers)  # Write headers
    csv_writer.writerows(rows)    # Write rows
