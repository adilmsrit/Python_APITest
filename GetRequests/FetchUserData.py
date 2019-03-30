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
for i in range(0, 3):
    firstName = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(firstName[0])
