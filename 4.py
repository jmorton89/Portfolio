import requests
import os

# method 1: check url response, if not ok will print the error code

# response = requests.get("https://www.google.com")
# if not response.ok:
#     raise Exception("GET failed with status code {}".format(response.status_code))

# method 2: will raise an HTTPError exception only if the response wasn’t successful

# response = requests.get("https://www.google.com")
# response.raise_for_status()

# prints a html search request for the indicated website with the pre-defined parameters

# p = {"search": "LA Lakers", "max_results": 15}
# response = requests.get("https://www.google.com", params=p)
# response.request.url
# print(response.request.url)

# contains the data that will be sent as part of the POST request

# p = {"description": "basketball player", "name": "michael jordan", "age": 30}
# response = requests.post("https://www.google.com", data=p)
# response.request.url
# print(response.request.url)
# print(response.request.body)

# export parameters list as json format

# response = requests.post("https://www.google.com", json=p)
# print(response.request.url)
# print(response.request.body)

# import files from a directory and export parsed data to indicated IP

# files = os.listdir('/directory/')
# for file in files:
#         x = open('/directory/'+file)
#         data = x.read()
#         data = data.split('\n')
#         dictionary = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
#         response = requests.post('http://IP/feedback/', json=dictionary)
#         print(response.status_code)

# https://www.bing.com/search?q=la+lakers
# https://www.bing.com/search?q=test
# https://search.yahoo.com/search?p=la+lakers

#p = {"search": "LA Lakers", "max_results": 15}
p = {"q": "LA Lakers"}
response = requests.get("https://www.bing.com", params=p)
x=response.request.url
response2=requests.get(x)
print(x)
print(response2)
print(response2.request.body)





