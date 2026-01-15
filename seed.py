from app import app, db
from model import User, Customer, Product, Category, Order, OrderItem
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- Seed Users ---
    users = [
        User(username="admin", email="admin@gmail.com", password=generate_password_hash("admin123"), role="admin"),
        User(username="staff", email="staff@gmail.com", password=generate_password_hash("staff123"), role="admin")
    ]
    db.session.add_all(users)
    db.session.flush()

    # --- Seed Customers ---
    customers = [
        Customer(username="Pen Pichvitou", email="penpichvitou@gmail.com", password=generate_password_hash("pass123")),
        Customer(username="Sok Dara", email="sokdara@gmail.com", password=generate_password_hash("pass123")),
        Customer(username="Chan Sreyleak", email="chansreyleak@gmail.com", password=generate_password_hash("pass123"))
    ]
    db.session.add_all(customers)
    db.session.flush()

    # --- Seed Categories ---
    # --- Seed Categories ---
    categories = [
        Category(name="Electronics")
    ]
    db.session.add_all(categories)
    db.session.flush()  # so categories[0].id is available

    # --- Seed Products ---
    product_list = [
        {
            'name': 'Macbook Pro M3',
            'price': 1499,
            'cost': 25,  # you can set some cost
            'stock': 50,
            'image': '/static/images/products/macbook.png',
            'description': 'Powerful MacBook Pro with M3 chip, sleek design, and long battery life.'
        },
        {
            'name': 'ATH M60X',
            'price': 199,
            'cost': 10,
            'stock': 70,
            'image': '/static/images/products/ath-m60x-product.png',
            'description': 'High-quality over-ear headphones with rich sound and comfortable fit.'
        },
        {
            'name': 'Pixel Watch',
            'price': 299,
            'cost': 15,
            'stock': 40,
            'image': '/static/images/products/pixel-watch.png',
            'description': 'Smartwatch with fitness tracking, heart rate monitor, and stylish design.'
        },
        {
            'name': 'iPhone 17 Pro',
            'price': 999,
            'cost': 35,
            'stock': 60,
            'image': '/static/images/products/iPhone-17-Pro.png',
            'description': 'Latest iPhone with advanced camera, fast processor, and sleek display.'
        },
        {
            'name': 'Samsung Galaxy S25 Ultra',
            'price': 999,
            'cost': 50,
            'stock': 30,
            'image': '/static/images/products/samsung-galaxy-s25-ultra.png',
            'description': 'Premium Samsung smartphone with large screen, high-resolution camera, and fast performance.'
        },
        {
            'name': 'iPhone 15',
            'price': 799,
            'cost': 20,
            'stock': 50,
            'image': '/static/images/products/iPhone-15.png',
            'description': 'Compact and powerful iPhone with excellent performance and camera quality.'
        },
        {
            'name': 'iPad Air 5th Gen',
            'price': 599,
            'cost': 60,
            'stock': 25,
            'image': '/static/images/products/iPad-Air-5th-Gen.png',
            'description': 'Lightweight iPad with powerful chip, high-resolution display, and perfect for work or play.'
        },
        {
            'name': 'Huawei Mate Air',
            'price': 299,
            'cost': 30,
            'stock': 40,
            'image': '/static/images/products/Huawei-Matepad-Air.png',
            'description': 'Versatile tablet with crisp display, long battery life, and solid performance.'
        },
        {
            'name': 'ASUS ROG Strix G18',
            'price': 1799,
            'cost': 25,
            'stock': 20,
            'image': '/static/images/products/ASUS-ROG-Strix-G18.png',
            'description': 'Gaming laptop with high refresh rate display, powerful GPU, and fast processor.'
        },
        {
            'name': 'Apple Vision Pro',
            'price': 3499,
            'cost': 40,
            'stock': 15,
            'image': '/static/images/products/Apple-Vision-Pro.png',
            'description': 'Cutting-edge AR headset with immersive display and intuitive controls for next-level experiences.'
        }
    ]

    products = [
        Product(
            name=p['name'],
            category_id=categories[0].id,
            price=p['price'],
            cost=p['cost'],
            stock=p['stock'],
            image=p['image'],
            description=p['description']
        )
        for p in product_list
    ]

    db.session.add_all(products)
    db.session.commit()

    print("Seeded 10 Electronics products successfully!")

    # --- Seed Orders (for the whole month) ---
    # start_date = datetime(2025, 11, 1)
    # end_date = datetime(2025, 11, 30)
    # total_days = (end_date - start_date).days + 1
    #
    # for i in range(total_days):
    #     date = start_date + timedelta(days=i)
    #     daily_orders = random.randint(2, 6)  # 2–6 orders per day
    #
    #     for _ in range(daily_orders):
    #         user = users[0] if random.random() < 0.6 else users[1]
    #         customer = random.choice(customers)
    #         order = Order(
    #             user_id=user.id,
    #             customer_id=customer.id,
    #             date_time=date,
    #             status=random.choice(["completed", "pending"])
    #         )
    #         db.session.add(order)
    #         db.session.flush()
    #
    #         # Each order has 1–4 items
    #         for _ in range(random.randint(1, 4)):
    #             product = random.choice(products)
    #             qty = random.randint(1, 5)
    #             order_item = OrderItem(
    #                 order_id=order.id,
    #                 product_id=product.id,
    #                 qty=qty,
    #                 price=product.price,
    #                 total = product.price * qty
    #             )
    #             db.session.add(order_item)

    db.session.commit()
    print("Seeding complete with users, customers, categories, products, orders & order_items!")
