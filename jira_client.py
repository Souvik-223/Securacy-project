import requests
from requests.auth import HTTPBasicAuth

class JiraClient:
    def __init__(self, base_url, email, api_token):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(email, api_token)
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }


    def create_issue(self, payload):
        url = f"{self.base_url}/rest/api/3/issue"

        response = requests.post(
            url,
            headers=self.headers,
            auth=self.auth,
            json=payload
        )
        if response.status_code >= 400:
            print("JIRA ERROR RESPONSE:")
            print(response.text)
            response.raise_for_status()


        return response.json()
