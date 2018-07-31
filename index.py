from client import YnabClient
from datetime import datetime
from models.transaction import Transaction
from secrets.token import token
from secrets.database import connection_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

def main():
  # client = YnabClient(token)
  # budgets = client.getBudgets()
  # print(budgets)
  engine = create_engine(connection_url)
  Session = sessionmaker()
  Session.configure(bind=engine)
  session = Session()
  transaction = Transaction(id=uuid4(), date=datetime.today(), amount=37.87, payee='Target')
  session.add(transaction)
  session.commit()
   
if __name__ == '__main__':
  main()
