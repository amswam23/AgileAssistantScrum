import requests

class JiraClient:
    def __init__(self, base_url, email, api_token):
        self.base_url = base_url
        self.auth = (email, api_token)

    def search(self, jql):
        url = f"{self.base_url}/rest/api/3/search"
        response = requests.get(url, params={"jql": jql}, auth=self.auth)
        return response.json()
