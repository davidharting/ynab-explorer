from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Numeric, String

Base = declarative_base()

class Transaction(Base):
  __tablename__ = 'transactions'

  id = Column(String, primary_key = True)
  date = Column(DateTime)
  amount = Column(Numeric)
  payee = Column(String)

  def __repr__(self):
    return '<Transaction date={} amount={} payee={}>'.format(self.date, self.amount, self.payee)
