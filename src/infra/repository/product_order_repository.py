from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Products_Orders as Product_Order
from src.infra.db_entities import Products


class Product_OrderRepository:

    @classmethod
    def create_product_order(cls, product_id: int, order_id: int, price: float, amount: int):
        with DBConnectionHandler() as db:
            try:
                product = db.session.query(Products).filter_by(id=product_id).first()
                new_product_order = Product_Order(product_id=product_id, name=product.name, order_id=order_id, price=price, amount=amount)
                db.session.add(new_product_order)
                db.session.commit()
                return {
                    "data": new_product_order.to_dict(),
                    "status": 201,
                    "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {
                    "data": None,
                    "status": 409,
                    "errors": ["Erro na requisição"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {
                    "data": None,
                    "status": 500,
                    "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    @classmethod
    def list_products_orders(cls):
        with DBConnectionHandler() as db:
            try:
                products_orders = []
                raw_products_orders: list[Product_Order] = db.session.query(Product_Order).all()
                for product_order in raw_products_orders:
                    products_orders.append(product_order.to_dict())
                return {"data": products_orders, "status": 200, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": [], "status": 409, "errors": ["Integrity Error"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": [], "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    @classmethod
    def update_product_order(cls, product_order_id: int, product_id: int, order_id: int, price: float, amount: int):
        with DBConnectionHandler() as db:
            try:
                product_order = db.session.query(Product_Order).filter_by(id=product_order_id).first()
                if product_order:
                    print(product_order)
                    product_order.product_id=product_id
                    product_order.order_id=order_id
                    product_order.price = price
                    product_order.amount = amount
                    db.session.commit()
                    return {"data": None, "status": 200, "errors": []}
                return {"data": None, "status": 404, "errors": [f"Pedido de produtos não encontrado."]}
            except IntegrityError:
                return {"data": None, "status": 409, "errors": [f"Pedido de produto já existe."]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    @classmethod
    def delete_product_order(cls, product_order_id: int):
        with DBConnectionHandler() as db:
            try:
                product_order = db.session.query(Product_Order).filter_by(id=product_order_id).first()
                if product_order:
                    db.session.delete(product_order)
                    db.session.commit()
                    return {"data": None, "status": 200, "errors": []}
                return {"data": None, "status": 404, "errors": [f"Pedido de produto de id {product_order_id} não existe"]}
            except MultipleResultsFound:
                return {"data": None, "status": 409, "errors": [f"Conflito de pedido de produto com id {product_order_id}"]}
            except Exception as ex:
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    @classmethod
    def get_product_order_by_id(cls, product_order_id:int):
        with DBConnectionHandler() as db:
            try:
                products_orders = []
                raw_products_orders: list[Product_Order] = db.session.query(Product_Order).filter_by(order_id=product_order_id)
                for product_order in raw_products_orders:
                    products_orders.append(product_order.to_dict())
                return {"data": products_orders, "status": 200, "errors": []}
            except NoResultFound:
                return {"data": None, "status": 404, "errors": [f"Pedido de produto de id {product_order_id} não existe"]}
            except Exception as ex:
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}