import requests

# webhooks for zoho
def send_zoho_request(url, payload):
    response = requests.post(url, data=payload)
    return response.status_code