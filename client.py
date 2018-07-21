import requests
from secrets.token import token

api_url = 'https://api.youneedabudget.com/v1/'
headers = {
  'Authorization': 'Bearer ' + token
}

def get(resource):
  uri = api_url + resource
  r = requests.get(uri, headers=headers)
  data = r.json()
  if (r.ok):
    return data['data'][resource]
  else:
    return data['error']
