from flask_jwt_extended import jwt_required
from app import app
from flask import render_template
from model import Category  # only need Category here

@app.route('/admin_category')
@jwt_required()
def admin_category():
    # Query all categories
    categories = Category.query.all()

    # Pass categories directly to the template
    return render_template('/admin/admin_category.html', categories=categories)
