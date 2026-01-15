from app import app
from flask import render_template
# from products import product_list
from slide import slide_list
from model import Product

@app.route('/')
def home():
    products = Product.query.all()  # get the products from DB
    return render_template('home.html', products=products, slides=slide_list)