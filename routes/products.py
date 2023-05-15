from flask import Blueprint
from sqlalchemy import select
from sqlalchemy.orm import Session
from db import get_connection
import json
from models import Product

products_bp = Blueprint('products', 'products_bp')

@products_bp.route('/all', methods=['GET'])
def get_products():
    engine = get_connection()
    with Session(engine) as session:
        query = select(Product)
        products = [x for x in session.scalars(query)]

        return [p.as_dict() for p in products]
