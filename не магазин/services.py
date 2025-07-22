from sqlalchemy import select

from models import session_maker, User, Product, Order, Ticket


class BuyProductException(Exception):
    pass

def create_user (username, password) -> User:
    with session_maker() as session:
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def show_profile(user: User) -> str:
    return (
        f"Профиль пользователя:\n"
        f"Имя: {user.username}\n"
        f"Поинты: {user.points}\n"
    )


def get_user (username, password) -> User | None:
    with session_maker() as session:
        user = session.query(User).filter_by(username=username).first()
        return user

def get_all_products() -> list[Product]:
    with session_maker() as session:
        query = select(Product).order_by(Product.id.desc())
        result = session.execute(query)
        products = result.scalars().all()
        return list(products)

def apply_ticket(user : User, ticket_uuid: str) -> str:
    with session_maker() as session:
        ticket = session.query(Ticket).filter_by(uuid=ticket_uuid).first()
        if not ticket:
            return "Неверный UUID тикета!"
        if not ticket.available:
            return "Тикет уже использован!"
        ticket.available = False
        ticket.user_id = user.id
        user = session.get(User, user.id)
        user.points += 20


        session.refresh(user)
        session.commit()
        return "Тикет успешно использован! Вам начислены 20 поинтов!"


def buy_product(user_id: int, product_id: int, count: int) -> Order:
    with session_maker() as session:
        user = session.get(User, user_id)
        if user is None:
            raise BuyProductException("Пользователь с таким ID не найден!")

        product = session.get(Product, product_id)
        if product is None:
            raise BuyProductException("Продукт с таким ID не найден!")

        if product.count < count:
            raise BuyProductException("Недостаточно товара на складе!")

        total_price = product.cost * count
        if user.points < total_price:
            raise BuyProductException("Недостаточно поинтов для покупки!")

        user.points -= total_price
        product.count -= count
        order = Order(user_id=user_id, product_id=product_id, count=count)

        session.add(order)
        session.commit()
        session.refresh(order)

        return order