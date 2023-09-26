from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey


Base = declarative_base()


class Client(Base):

    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cpf = Column(String(9))
    address = Column(String(30))

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, address={self.address})"


class Account(Base):

    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(2))
    agency = Column(Integer)
    number = Column(Integer)
    balance = Column(Float)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    def __repr__(self):
        return f"Account(id={self.id}, tipo={self.tipo}, saldo={self.balance})"


engine = create_engine("sqlite://")


Base.metadata.create_all(engine)


with Session(engine) as session:
    luan = Client(name='Luan Aquino',
                  cpf='234.434.456-50',
                  address='Rua 1 , número 1'
                  )

    regina = Client(name='Regina Garcia',
                    cpf='125.652.970-80',
                    address='Rua 2, número 2'
                    )

    marcio = Client(name='Marcio Melo',
                    cpf='348.610.999-20',
                    address='Rua 3, número 3'
                    )

    acc1 = Account(client_id='1',
                   tipo='cc',
                   agency=1,
                   number=23000,
                   balance=1500
                   )
    acc2 = Account(client_id='2',
                   tipo='cp',
                   agency=1,
                   number=33000,
                   balance=3000
                   )
    acc3 = Account(client_id='3',
                   tipo='cc',
                   agency=1,
                   number=43000,
                   balance=4500
                   )

    session.add_all([luan, regina, marcio])
    session.add_all([acc1, acc2, acc3])
    session.commit()


print('Recuperando clientes a partir de uma condição de filtragem:')
stmt_clients = select(Client).where(Client.name.in_(
    ['Luan Aquino', 'Marcio Melo']))
for result in session.scalars(stmt_clients):
    print(result)


print("\nRecuperando clientes de maneira ordenada:")
stmt_order = select(Client).order_by(Client.name.desc())
for result in session.scalars(stmt_order):
    print(result)


print("\nRecuperando contas de maneira ordenada:")
stmt_accounts = select(Account).order_by(Account.tipo.desc())
for result in session.scalars(stmt_accounts):
    print(result)


print("\nRecuperando contas e clientes:")
stmt_join = select(Client.name, Account.tipo,
                   Account.balance).join_from(Client, Account)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

session.close()
