from flask import Flask
from flask_restful import Api

from backend.resources.pool_resources import PoolResources
from backend.resources.base_resources import BaseResource

app = Flask(__name__)

api_app = Api(app)

api_app.add_resource(PoolResources, '/api/pool/product',
                     endpoint='products_pool')
api_app.add_resource(PoolResources, '/api/pool/product/<int:id_>',
                     endpoint='product_pool')


@app.route('/')
def index():
    return 'Bem vindo a catálogo!'
