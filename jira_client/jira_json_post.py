import json
from urllib.request import HTTPBasicAuth
import requests

class JiraLogin:
    def __init__(self, url=None, auth=None, headers=None, project_name=None):
        self.project_name = "ITB"
        self.url = 'https://doubledare.atlassian.net/rest/api/2/issue'
        self.auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF0hyibnD_Kj1g0wRUdrQrJq0uKTkNVgrATNYaC5y-4CN_p0T7XmGjLcj9OHFXBxd7Xv3ipo56eu8C9q9qi7ceEiLOoTOgwDTeyyYt78UypNVydEzU1Z4zD3udI0JGSoDk1JC-CrJB9MmBIy3cP1FWyFm1SJAGpeBxcX-RP-gKKxjQ=72A1CF0C")
        self.headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

authenticator = JiraLogin()

payload = json.dumps(
{
    "fields": {
       "project":
       {
          "key": authenticator.project_name
       },
       "summary": "REST ye merry gentlemen. python",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "id": "10001"
       }
   }
}
)

response = requests.post(ulr=authenticator.url,headers = authenticator.headers,data = payload,auth =authenticator.auth)
print(response.text)