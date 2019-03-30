import requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

assert response.status_code == 200

print(response.cookies)
# To get the date of the Server details from the header fetched
print(response.headers.get('Date'))
print(response.headers.get('Server'))
print(response.encoding)
# Ferches the elapsed time
print(response.elapsed)

elapsedTime = response.elapsed

if elapsedTime.seconds < 1:
    print("Passed the PT")
else:
    print("Too Slow")