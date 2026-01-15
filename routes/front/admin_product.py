from flask_jwt_extended import jwt_required

from app import app
from flask import render_template
from model import Product, Category  # assuming you have a Category model


@app.route('/admin_product')
@jwt_required()
def admin_product():
    # Get all products
    products = Product.query.all()
    category = Category.query.all()
    # Optional: Build a dict of category_id -> category_name
    categories = {c.id: c.name for c in Category.query.all()}

    # Map category names for each product
    for product in products:
        product.category_name = categories.get(product.category_id, "Unknown")  # add attribute dynamically

    return render_template('/admin/admin_product.html', products=products, category=category)
