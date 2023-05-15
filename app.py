from flask import Flask
from routes.products import products_bp

def create_app():
    app = Flask('pep1_backend')

    app.register_blueprint(products_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    # Only /products/all is working so far
    app.run(port=8080, debug=True)