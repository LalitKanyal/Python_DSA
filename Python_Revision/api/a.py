import requests
from pprint import pprint

api_url = "http://learncodethehardway.com/api/course"

r = requests.get(api_url)
data = r.json()
pprint(data)

