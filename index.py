from client import YnabClient
from datetime import datetime
from models.transaction import Transaction
from secrets.token import token
from secrets.database import connection_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

def get_budget_id(client):
  budgets = client.getBudgets()
  first_budget = budgets[0]
  return first_budget['id']

def main():
  engine = create_engine(connection_url)
  Session = sessionmaker()
  Session.configure(bind=engine)
  session = Session()

  try:
    client = YnabClient(token)
    budget_id = get_budget_id(client)
    transactions = client.getTransactions(budget_id)

    for t in transactions:
      # TODO: Handle subtransactions
      # TODO: Add more date-related columns. Separate year, month, week of month, day of week etc. to allow for cool window functions
      # TODO: Change datetime column to just a dateonly
      amount = t['amount'] / 100
      transaction = Transaction(id=t['id'], date=t['date'], amount=amount, category=t['category_name'], payee=t['payee_name'], description=t['memo'])
      session.add(transaction)

    session.commit()
  except:
    session.rollback()
    raise
  finally:
    session.close()
   
if __name__ == '__main__':
  main()
