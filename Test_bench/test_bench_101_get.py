import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://doubledare.atlassian.net/rest/api/3/issue/createmeta"
auth = HTTPBasicAuth("boryspiasny@gmail.com", "ATATT3xFfGF0hyibnD_Kj1g0wRUdrQrJq0uKTkNVgrATNYaC5y-4CN_p0T7XmGjLcj9OHFXBxd7Xv3ipo56eu8C9q9qi7ceEiLOoTOgwDTeyyYt78UypNVydEzU1Z4zD3udI0JGSoDk1JC-CrJB9MmBIy3cP1FWyFm1SJAGpeBxcX-RP-gKKxjQ=72A1CF0C")
headers = {
  "Accept": "application/json"
}

response = requests.request(
    "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))