from client import get

def main():
  budgets = get('budgets')
  print(budgets)


if __name__ == '__main__':
  main()
