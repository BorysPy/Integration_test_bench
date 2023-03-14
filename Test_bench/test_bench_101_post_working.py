import requests
from requests.auth import HTTPBasicAuth
import json

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

response = requests.post(url,headers = headers,data = payload,auth = auth)
print(response.text)

class JiraIssueApi:
   def __init__(self, auth):
      self.auth = auth
  
   def get_list_jira_issues(self, url):
      pass

   def create_jira_issue(self, url):
      pass

   def read_jira_issue(self, url):
      pass

   def update_jira_issue(self, url):
      pass

   def delete_jira_issue(self, url):
      pass

jira_issue_api_object = JiraIssueApi(auth = auth)
jira_issue_api_object.get_list_jira_issues(url = url) #endpoint

