from flask import render_template, jsonify, request
from flask_jwt_extended import jwt_required
from app import db, app
from model.order import Order
from model.order_item import OrderItem

@app.route('/admin_order')
@jwt_required()
def admin_order():
    orders = (
        Order.query
        .order_by(Order.date_time.desc())
        .all()
    )

    return render_template(
        '/admin/admin_order.html',
        orders=orders
    )

@app.route('/admin/order/update-status/<int:order_id>', methods=['PUT'])
@jwt_required()
def update_status(order_id):
    order = Order.query.get_or_404(order_id)

    data = request.get_json()
    status = data.get('status')

    if status not in ['pending', 'completed', 'cancelled']:
        return jsonify({'error': 'Invalid status'}), 400

    order.status = status
    db.session.commit()

    return jsonify({'message': 'Status updated'})


@app.route('/admin/order/delete/<int:order_id>', methods=['DELETE'])
@jwt_required()
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)

    # delete order items first (important)
    OrderItem.query.filter_by(order_id=order.id).delete()

    db.session.delete(order)
    db.session.commit()

    return jsonify({'message': 'Order deleted'})
