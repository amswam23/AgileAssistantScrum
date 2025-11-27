import requests

class SlackClient:
    def __init__(self, token):
        self.token = token

    def fetch_channel_messages(self, channel_id):
        url = "https://slack.com/api/conversations.history"
        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.get(url, headers=headers).json()
