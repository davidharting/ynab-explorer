from client import YnabClient
from secrets.token import token

def main():
  client = YnabClient(token)
  budgets = client.getBudgets()
  print(budgets)

if __name__ == '__main__':
  main()
