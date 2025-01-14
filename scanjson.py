# This script is a test harnest levage VulnAPI - an API REST endpoint scanner. https://github.com/cerberauth/vulnapi
# The vulnerable API REST endpoint. https://github.com/erev0s/VAmPI

import subprocess
from openapi_parser import parse

# Parse the OpenAPI specification
specification = parse('openapi.json')

# Extract URLs from paths
urls = [path.url for path in specification.paths]  # Adjust if 'path.url' is incorrect
proxy = 'http://127.0.0.1:8080'

# Token securely stored (use environment variables or a secure storage)
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTYyNDI2MjIsImlhdCI6MTUxNjIzOTAyMiwibmFtZSI6IkpvaG4gRG9lIiwic3ViIjoiMmNiMzA3YmEtYmI0Ni00MTk0LTg1NGYtNDc3NDA0NmQ5YzliIn0.SCC35SSgMSMr0kV1i_TuPAhiSGtsC1cFGCfvaus5GyU'

# Predefined usernames to test
usernames = ['name1', 'name2', 'admin']

# Debugging: Print extracted URLs
print("Extracted URLs:", urls)

# Scan each URL using vulnapi
for url in urls:
    # Check if the URL contains the placeholder '{username}'
    if '{username}' in url:
        # Iterate over each username and replace the placeholder
        for username in usernames:
            formatted_url = url.replace('{username}', username)
            command = (
                f"vulnapi scan curl 'http://localhost:5001{formatted_url}' "
                f"-H 'accept: application/json' "
                f"-H 'Authorization: Bearer {token}' "
                f"--proxy {proxy}"
            )
            print(f"Executing: {command}")
            try:
                # Execute the command
                result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
                print(f"Output for {formatted_url}:\n{result.stdout}")
            except subprocess.CalledProcessError as e:
                print(f"Error occurred while executing command for {formatted_url}: {e}")
                print(f"Error Output:\n{e.stderr}")
    else:
        # If no placeholder, process the URL as is
        command = (
            f"vulnapi scan curl 'http://localhost:5001{url}' "
            f"-H 'accept: application/json' "
            f"-H 'Authorization: Bearer {token}' "
            f"--proxy {proxy}"
        )
        print(f"Executing: {command}")
        try:
            # Execute the command
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(f"Output for {url}:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while executing command for {url}: {e}")
            print(f"Error Output:\n{e.stderr}")

# Perform a file-based scan with vulnapi
file_scan_command = f"echo '{token}' | vulnapi scan openapi http://127.0.0.1:5001/openapi.json --proxy {proxy}"
print(f"Executing file scan: {file_scan_command}")
try:
    # Execute the file scan command
    file_scan_result = subprocess.run(file_scan_command, shell=True, check=True, text=True, capture_output=True)
    print(f"File Scan Output:\n{file_scan_result.stdout}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while executing file scan: {e}")
    print(f"Error Output:\n{e.stderr}")
