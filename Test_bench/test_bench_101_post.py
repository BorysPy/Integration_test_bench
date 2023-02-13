import requests
from requests.auth import HTTPBasicAuth
import json


class JiraLogin:
    def __init__(self, url, auth, headers, project_name):
        self.project_name = project_name
        self.url = url
        self.auth = auth
        self.headers = headers

    project_name = "ITB"
    url = 'https://doubledare.atlassian.net/rest/api/2/issue'
    auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF0hyibnD_Kj1g0wRUdrQrJq0uKTkNVgrATNYaC5y-4CN_p0T7XmGjLcj9OHFXBxd7Xv3ipo56eu8C9q9qi7ceEiLOoTOgwDTeyyYt78UypNVydEzU1Z4zD3udI0JGSoDk1JC-CrJB9MmBIy3cP1FWyFm1SJAGpeBxcX-RP-gKKxjQ=72A1CF0C")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }


payload = json.dumps(
{
    "fields": {
       "project":
       {
          "key": "ITB"
       },
       "summary": "REST ye merry gentlemen. python",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "id": "10001"
       }
   }
}
)

response = requests.post(ulr = JiraLogin.url , headers = JiraLogin.headers, data = payload,auth = JiraLogin.auth)
print(response.text)