from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria o Banco De Dados
db = create_engine("sqlite:///mydatabase.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# As Tabelas
class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String)
    password = Column("password", String)
    active = Column("active", Boolean)

    def __init__(self, name, email, password, active=True):
        self.name = name
        self.email = email
        self.password = password
        self.active = active

class Book(Base):
    __tablename__ = "books"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("titulo", String)
    qnty_pages = Column("qnty_pages", Integer)
    owner = Column("owner", ForeignKey("users.id"))

    def __init__(self, title, qnty_pages, owner):
        self.title = title
        self.qnty_pages = qnty_pages
        self.owner = owner

Base.metadata.create_all(bind=db)

# CRUD (Create, Read, Update and Delete)

# Instanciando a classe User
# C - Create
# user = User(name="Ruan2", email="Ruan2@gmail.com", password="12345")
# session.add(user)
# session.commit()

# R - READ
# list_users = session.query(User).all()
ruan_user2 = session.query(User).filter_by(email="Ruan2@gmail.com").first()
print(ruan_user2)
print(ruan_user2.name)
print(ruan_user2.email)
print(ruan_user2.password)

# book = Book(title="A sutil arte de ligar o f*da-se", qnty_pages=224, owner=ruan_user.id)
# session.add(book)
# session.commit()

# U - Update
# ruan_user.name = "Ruan Cruz"
# session.add(ruan_user)
# session.commit(# )

# D - Delete
# session.delete(ruan_user2)
# session.commit()