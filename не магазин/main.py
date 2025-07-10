from menu import Menu
from models import Base, engine


def create_tables():
    Base.metadata.create_all(engine)



create_tables()
menu = Menu()
menu.run()