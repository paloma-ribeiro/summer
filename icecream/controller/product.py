from flask import Blueprint
from service.product import ProductService

blueprint_product = Blueprint('product_api', __name__, url_prefix='/api')


@blueprint_product.route('/product', methods=['GET'])
def get_product():
    service = ProductService()
    found_product = service.get_product()
    return found_product
