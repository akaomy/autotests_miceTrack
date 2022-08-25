# import pytest
import requests

# GET
r = requests.get('http://localhost:5000')
# r2 = requests.get('http://localhost:5000/track-mice')

# test cases - positive / negative / boundary
# check if accessing r status code is 200
# check if accessing r2 status code is 200
# check if accessing r2 content is not empty

# get individual mice and check
#   female_mouse_manual_id (empty/not empty)
#   mating_date (certain format)


# POST
# test cases - positive / negative / boundary
# check after creating a single mouse
#       female_mouse_manual_id
#       mating_date
# etc.


print(r.status_code)
# print(r.content)
# print(r.request)
# print(r.headers)
# print(r.text)

# payload = {'key1': 'value1'}
# r = requests.put('http://localhost:5000/put', params=payload)
# r = requests.delete('http://localhost:5000/delete')
# r = requests.head('http://localhost:5000/get')
# r = requests.options('http://localhost:5000/get')
