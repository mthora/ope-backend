from src.infra.config import *
from src.infra.db_entities import *
from src.main.utils import hash_password
from flask import Flask
from flask_restx import Api
from src.main.routes import user_namespace, product_namespace, product_order_namespace, order_namespace

app = Flask(__name__)
app.config['SECRET_KEY'] = '00fe747c35'
app.config['UPLOAD_FOLDER'] = 'src\img'

api = Api(
    title="Talos RMS",
    version='1.0',
    description="Restaurant Management System"
)

api.add_namespace(user_namespace, path='/users')
api.add_namespace(product_namespace, path='/products')
api.add_namespace(product_order_namespace, path='/products_orders')
api.add_namespace(order_namespace, path='/orders')

if __name__ == "__main__":
    api.init_app(app)
    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)

    with DBConnectionHandler() as db:
        try:
            new_user = Users(name='admin', role=1, email='admin@suzy.com', password=hash_password('admin'))
            db.session.add(new_user)
            db.session.commit()
        except Exception as ex:
            print(ex)
            db.session.rollback()
        finally:
            db.session.close()
            
    app.run()