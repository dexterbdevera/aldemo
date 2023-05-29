import requests
import json

def browse_api(url, api_key=None):
    headers = {}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)

# Example usage
api_url = "https://open-atms.airlab.aero/api/v1/"
api_key = "NfDGWCgOJdNQrBlDFmz0IYGarZGsbeCQuY3fTUvZRLxtcNwizO5NY2IRmD3db5vS"

api_data = browse_api(api_url, api_key)
print(json.dumps(api_data, indent=4))  # Print the API data in a formatted way
