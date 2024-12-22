import requests
from pprint import pprint
api_url = "https://learncodethehardway.com/api/course"

# get one course
r = requests.get(api_url, params= {
    "course_id": 1, "full": "true"
})

data = r.json()
pprint(data)