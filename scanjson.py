# This script is a test harness to leverage VulnAPI - an API REST endpoint vuln scanner. https://github.com/cerberauth/vulnapi
# The vulnerable API REST endpoint this is designed to test against. https://github.com/erev0s/

import subprocess
from openapi_parser import parse

# Parse the OpenAPI specification
specification = parse('openapi.json')

# Extract URLs from paths
urls = [path.url for path in specification.paths]  # Adjust if 'path.url' is incorrect
proxy = 'http://127.0.0.1:8080'

# Token securely stored (use environment variables or a secure storage)
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTYyNDI2MjIsImlhdCI6MTUxNjIzOTAyMiwibmFtZSI6IkpvaG4gRG9lIiwic3ViIjoiMmNiMzA3YmEtYmI0Ni00MTk0LTg1NGYtNDc3NDA0NmQ5YzliIn0.SCC35SSgMSMr0kV1i_TuPAhiSGtsC1cFGCfvaus5GyU'

# Predefined usernames and book titles to test
usernames = ['name1', 'name2', 'admin']
book_titles = ['bookTitle77', 'bookTitle85', 'bookTitle47']

# Debugging: Print extracted URLs
print("Extracted URLs:", urls)

# Scan each URL using vulnapi with curl
for url in urls:
    # Check if the URL contains the placeholder '{username}' or '{book_title}'
    if '{username}' in url and '{book_title}' in url:
        # Handle URLs with both placeholders
        for username in usernames:
            for book_title in book_titles:
                formatted_url = url.replace('{username}', username).replace('{book_title}', book_title)
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
    elif '{username}' in url:
        # Handle URLs with only the '{username}' placeholder
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
    elif '{book_title}' in url:
        # Handle URLs with only the '{book_title}' placeholder
        for book_title in book_titles:
            formatted_url = url.replace('{book_title}', book_title)
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
        # Handle URLs without placeholders
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

# Perform a file-based scan with openapi instead of curl
file_scan_command = f"echo '{token}' | vulnapi scan openapi http://127.0.0.1:5001/openapi.json --proxy {proxy}"
print(f"Executing file scan: {file_scan_command}")
try:
    # Execute the file scan command
    file_scan_result = subprocess.run(file_scan_command, shell=True, check=True, text=True, capture_output=True)
    print(f"File Scan Output:\n{file_scan_result.stdout}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while executing file scan: {e}")
    print(f"Error Output:\n{e.stderr}")
