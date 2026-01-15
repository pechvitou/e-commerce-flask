from app import app
from flask import render_template
from model import Product

# Product page
@app.route('/products/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    # product = next((p for p in product_list if p['id'] == product_id), None)
    # if not product:
    #     return "Product not found", 404
    print(product.image)
    return render_template('product.html', product=product)