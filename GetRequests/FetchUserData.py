import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

# Parse response to Json Format
json_response = json.loads(response.text)
print(json_response)

# Fetch response using Json Path
pages = jsonpath.jsonpath(json_response,'total_pages')
# We get the repsonse as List so we print the first item sa below.
print(pages[0])

assert pages[0]==4
