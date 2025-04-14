import requests
import os
import sys

# Get values from environment variables
sonar_host = os.environ.get('SONAR_HOST', 'https://your-sonarqube-instance.com')
sonar_token = os.environ.get('SONAR_TOKEN')
project_key = os.environ.get('SONAR_PROJECT_KEY', 'my-app')

if not sonar_token:
    print("SONAR_TOKEN environment variable is required")
    sys.exit(1)

# Configure API request
url = f"{sonar_host}/api/qualitygates/project_status?projectKey={project_key}"
headers = {'Authorization': f'Bearer {sonar_token}'}

# Make request
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Error fetching quality gate status: {response.text}")
    sys.exit(1)

# Parse response
data = response.json()
status = data.get('projectStatus', {}).get('status')

print(f"Quality Gate status: {status}")

# Exit with non-zero status if quality gate failed
if status != 'OK':
    print("Quality Gate failed!")
    sys.exit(1)

print("Quality Gate passed!")
