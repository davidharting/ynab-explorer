import requests

class YnabClient():

  def __init__(self, token):
    self._api_url = 'https://api.youneedabudget.com/v1/'
    self._headers = {
      'Authorization': 'Bearer ' + token
    }

  def _request(self, uri, resource):
    r = requests.get(uri, headers=self._headers)
    data = r.json()
    if (r.ok):
      return data['data'][resource]
    else:
      return data['error']
  
  def _getResource(self, resource, id = ''):
    uri = self._api_url + resource + id
    return self._request(uri, resource)
  
  def _getBudgetResource(self, budget_id, resource):
    uri = self._api_url + 'budgets/' + budget_id + '/' + resource
    return self._request(uri, resource)

  def getBudgets(self):
    return self._getResource('budgets')

  def getTransactions(self, budget_id):
    return self._getBudgetResource(budget_id, 'transactions')
