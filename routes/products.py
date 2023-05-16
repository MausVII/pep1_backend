from flask import Blueprint, request
from sqlalchemy import select
from sqlalchemy.orm import Session
from db import get_connection
from models import Product

products_bp = Blueprint('products', 'products_bp', url_prefix='products')

@products_bp.route('/all', methods=['GET'])
def get_products():
    engine = get_connection()
    with Session(engine) as session:
        query = select(Product)
        products = [x for x in session.scalars(query)]

        return [p.as_dict() for p in products]

@products_bp.route('/in', methods=['POST'])
def insert_product():
    engine = get_connection()

    product_id = request.json.get('product_id')
    name = request.json.get('name')
    category = request.json.get('category')
    price = request.json.get('price')
    image = request.json.get('image')
    other_colors = request.json.get('other_colors')
    short_description = request.json.get('short_description')
    designer = request.json.get('designer')
    depth = request.json.get('depth')
    height = request.json.get('height')
    width = request.json.get('width')



    with Session(engine) as session:

        product = Product(
            id = product_id,
            name = name,
            category = category,
            price = price,
            image = image,
            other_colors = other_colors, 
            short_description = short_description,
            designer = designer,
            depth = depth,
            height = height,
            width = width
        )

        session.add(product)
        session.commit()
        
        return "Success"