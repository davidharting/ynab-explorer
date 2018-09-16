from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Numeric, String

Base = declarative_base()

class Transaction(Base):
  __tablename__ = 'transactions'

  id = Column(String, primary_key = True)
  date = Column(DateTime)
  amount = Column(Numeric)
  category = Column(String)
  payee = Column(String)
  description=Column(String)

  def __repr__(self):
    return '<Transaction date={} amount={} category={} payee={}>'.format(self.date, self.amount, self.category, self.payee)
