import subprocess
from openapi_parser import parse

# Parse the OpenAPI specification
specification = parse('openapi.json')

# Extract URLs from paths
urls = [path.url for path in specification.paths]  # Adjust if 'path.url' is incorrect
proxy = 'http://127.0.0.1:8080'

# Token securely stored (use environment variables or a secure storage)
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTYyNDI2MjIsImlhdCI6MTUxNjIzOTAyMiwibmFtZSI6IkpvaG4gRG9lIiwic3ViIjoiMmNiMzA3YmEtYmI0Ni00MTk0LTg1NGYtNDc3NDA0NmQ5YzliIn0.SCC35SSgMSMr0kV1i_TuPAhiSGtsC1cFGCfvaus5GyU'

# Debugging: Print extracted URLs
print("Extracted URLs:", urls)

# Scan each URL using vulnapi
for url in urls:
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
        print(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing command: {e}")
        print(f"Error Output:\n{e.stderr}")
