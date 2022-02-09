from flask import Flask
from controller.product import blueprint_product


def register_blueprints(app):
    app.register_blueprint(blueprint_product)


if __name__ == "__main__":
    app = Flask(__name__)
    register_blueprints(app)
    app.run(host='0.0.0.0', port=8585)

