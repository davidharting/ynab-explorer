import requests

class YnabClient():

  def __init__(self, token):
    self._api_url = 'https://api.youneedabudget.com/v1/'
    self._headers = {
      'Authorization': 'Bearer ' + token
    }
  
  def _getResource(self, resource):
    uri = self._api_url + resource
    r = requests.get(uri, headers=self._headers)
    data = r.json()
    if (r.ok):
      return data['data'][resource]
    else:
      return data['error']

  def getBudgets(self):
    return self._getResource('budgets')

