import csv
import requests
import socket
from requests.exceptions import ConnectionError

def get_ip_address(subdomain):
    try:
        ip_address = socket.gethostbyname(subdomain)
    except socket.gaierror:
        ip_address = None
    return ip_address

def check_status(subdomain):
    ip_address = get_ip_address(subdomain)

    try:
        http_response = requests.get(f'http://{subdomain}', timeout=3)
        http_status = http_response.status_code
    except ConnectionError:
        http_status = None

    try:
        https_response = requests.get(f'https://{subdomain}', timeout=3)
        https_status = https_response.status_code
    except ConnectionError:
        https_status = None

    return subdomain, ip_address, http_status, https_status

def read_subdomains_and_check_status(input_csv, output_csv):
    results = []

    with open(input_csv, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            subdomain = row[0]
            result = check_status(subdomain)
            results.append(result)

    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subdomain', 'IP Address', 'HTTP Status', 'HTTPS Status'])
        writer.writerows(results)

# Replace 'subdomains.csv' with your input CSV file path
input_csv = 'subdomains.csv'
# Replace 'results.csv' with your desired output CSV file path
output_csv = 'results.csv'
read_subdomains_and_check_status(input_csv, output_csv)
