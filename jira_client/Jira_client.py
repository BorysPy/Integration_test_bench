import requests
from requests.auth import HTTPBasicAuth
import json

class JiraLogin:
    def __init__(self, url, auth, headers, project_name):
        self.project_name = "ITB"
        self.url = 'https://doubledare.atlassian.net/rest/api/2/issue'
        self.auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF0hyibnD_Kj1g0wRUdrQrJq0uKTkNVgrATNYaC5y-4CN_p0T7XmGjLcj9OHFXBxd7Xv3ipo56eu8C9q9qi7ceEiLOoTOgwDTeyyYt78UypNVydEzU1Z4zD3udI0JGSoDk1JC-CrJB9MmBIy3cP1FWyFm1SJAGpeBxcX-RP-gKKxjQ=72A1CF0C")
        self.headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
