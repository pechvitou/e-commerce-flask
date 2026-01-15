from app import app
from flask import render_template
# from products import product_list
from slide import slide_list
from model import Product

@app.route('/')
def home():
    products = Product.query.all()  # get the products from DB
    print(products[1].category_id)
    return render_template('home.html', products=products, slides=slide_list)