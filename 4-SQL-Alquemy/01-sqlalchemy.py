#import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func



Base = declarative_base()

#sqlA.Column
class User(Base):
    __tablename__ = "user_account"
    
    #atributo
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    address = relationship(
    "Address", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"
    

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_acocunt.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address (id={self.id}, email={self.email_address})"

print(User.__tablename__)
print(Address.__tablename__)

#conexão com banco de dados
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

#depreciado - sera removido em futuro release
#print(engine.table_names())


inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_accout"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    Luan = User(
        name = 'Luan',
        fullname = 'Luan Aquino',
        address = [Address(email_address='luan@email.com')]
        )
    Regina = User(
        name = 'Regina',
        fullname = 'Regina Garcia',
        address = [Address(email_address='regina@email.com'),
                   Address(email_address='rgarcia@email.com')]
        )
    
# enviando para o BD (persistencia de dados)
session.add_all([Luan, Regina])

session.commit()

stmt = select(User).where().where(User.name.in_(["Luan", "Brenda"]))
print('recuperando usuario a partir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('recuperando os endereços de email de regina')
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print("\nrecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nexeccutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count('*').select_from(User))
print('total')
for result in session.scalars(stmt_count):
    print(result)





    


