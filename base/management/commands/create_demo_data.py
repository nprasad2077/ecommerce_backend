# Create this file at: base/management/commands/create_demo_data.py
# First create the directories: base/management/ and base/management/commands/
# Add __init__.py files in both directories

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from base.models import Product, Review, Order, OrderItem, ShippingAddress
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Creates demo data for the e-commerce application'

    def handle(self, *args, **options):
        self.stdout.write('Creating demo data...')
        
        # Create users
        users = self.create_users()
        
        # Create products
        products = self.create_products(users['admin'])
        
        # Create reviews
        self.create_reviews(products, users)
        
        # Create orders
        self.create_orders(products, users)
        
        self.stdout.write(self.style.SUCCESS('Demo data created successfully!'))

    def create_users(self):
        self.stdout.write('Creating users...')
        
        # Create admin user
        admin = User.objects.create_superuser(
            username='admin@example.com',
            email='admin@example.com',
            password='admin123',
            first_name='Admin'
        )
        
        # Create regular users
        user1 = User.objects.create_user(
            username='john@example.com',
            email='john@example.com',
            password='password123',
            first_name='John Doe'
        )
        
        user2 = User.objects.create_user(
            username='jane@example.com',
            email='jane@example.com',
            password='password123',
            first_name='Jane Smith'
        )
        
        user3 = User.objects.create_user(
            username='bob@example.com',
            email='bob@example.com',
            password='password123',
            first_name='Bob Wilson'
        )
        
        self.stdout.write(f'Created {User.objects.count()} users')
        
        return {
            'admin': admin,
            'users': [user1, user2, user3]
        }

    def create_products(self, admin_user):
        self.stdout.write('Creating products...')
        
        products_data = [
            {
                'name': 'AirPods Wireless Bluetooth Headphones',
                'brand': 'Apple',
                'category': 'Electronics',
                'description': 'Bluetooth technology lets you connect it with compatible devices wirelessly. High-quality AAC audio offers immersive listening experience. Built-in microphone allows you to take calls while working.',
                'price': 89.99,
                'countInStock': 10,
                'image': '/images/airpods.jpg'
            },
            {
                'name': 'iPhone 15 Pro Max 256GB',
                'brand': 'Apple',
                'category': 'Electronics',
                'description': 'Introducing the iPhone 15 Pro Max. A transformative triple-camera system that adds tons of capability without complexity. An unprecedented leap in battery life.',
                'price': 1199.99,
                'countInStock': 7,
                'image': '/images/iphone.jpg'
            },
            {
                'name': 'Cannon EOS 80D DSLR Camera',
                'brand': 'Cannon',
                'category': 'Electronics',
                'description': 'Characterized by versatile imaging specs, the Canon EOS 80D further clarifies itself using a pair of robust focusing systems and an intuitive design.',
                'price': 929.99,
                'countInStock': 5,
                'image': '/images/camera.jpg'
            },
            {
                'name': 'Sony Playstation 5',
                'brand': 'Sony',
                'category': 'Electronics',
                'description': 'The ultimate home entertainment center starts with PlayStation. Whether you are into gaming, HD movies, television, music.',
                'price': 499.99,
                'countInStock': 11,
                'image': '/images/playstation.jpg'
            },
            {
                'name': 'Logitech G-Series Gaming Mouse',
                'brand': 'Logitech',
                'category': 'Electronics',
                'description': 'Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse. The six programmable buttons allow customization for a smooth playing experience.',
                'price': 49.99,
                'countInStock': 25,
                'image': '/images/mouse.jpg'
            },
            {
                'name': 'Amazon Echo Dot 3rd Generation',
                'brand': 'Amazon',
                'category': 'Electronics',
                'description': 'Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small space.',
                'price': 29.99,
                'countInStock': 30,
                'image': '/images/alexa.jpg'
            },
            {
                'name': 'Nike Air Max 270',
                'brand': 'Nike',
                'category': 'Fashion',
                'description': 'The Nike Air Max 270 delivers visible cushioning under every step. Updated for modern comfort, it nods to the original with a large window and fresh colors.',
                'price': 150.00,
                'countInStock': 15,
                'image': '/images/nike-shoes.jpg'
            },
            {
                'name': 'Adidas Ultraboost 22',
                'brand': 'Adidas',
                'category': 'Fashion',
                'description': 'Experience incredible energy return with every stride. These running shoes combine comfort and responsiveness for your best run ever.',
                'price': 180.00,
                'countInStock': 12,
                'image': '/images/adidas-shoes.jpg'
            },
            {
                'name': 'Samsung 65" QLED 4K Smart TV',
                'brand': 'Samsung',
                'category': 'Electronics',
                'description': 'Experience stunning 4K resolution with Quantum Dot technology. Smart TV features let you stream your favorite content with ease.',
                'price': 1299.99,
                'countInStock': 4,
                'image': '/images/samsung-tv.jpg'
            },
            {
                'name': 'Apple MacBook Pro 16"',
                'brand': 'Apple',
                'category': 'Electronics',
                'description': 'The most powerful MacBook Pro ever is here. With the blazing-fast M3 Pro chip — a powerhouse for demanding workflows.',
                'price': 2499.99,
                'countInStock': 3,
                'image': '/images/macbook.jpg'
            },
            {
                'name': 'Bose QuietComfort 45',
                'brand': 'Bose',
                'category': 'Electronics',
                'description': 'Premium noise-cancelling headphones with superior comfort. Experience world-class noise cancellation and high-fidelity audio.',
                'price': 329.99,
                'countInStock': 8,
                'image': '/images/bose-headphones.jpg'
            },
            {
                'name': 'Fitbit Charge 5',
                'brand': 'Fitbit',
                'category': 'Electronics',
                'description': 'Advanced fitness tracker with built-in GPS, stress management tools, and sleep tracking. Stay motivated with Daily Readiness Score.',
                'price': 149.99,
                'countInStock': 20,
                'image': '/images/fitbit.jpg'
            }
        ]
        
        products = []
        for data in products_data:
            product = Product.objects.create(
                user=admin_user,
                name=data['name'],
                brand=data['brand'],
                category=data['category'],
                description=data['description'],
                price=data['price'],
                countInStock=data['countInStock'],
                image=data['image'],
                rating=0,
                numReviews=0
            )
            products.append(product)
        
        self.stdout.write(f'Created {len(products)} products')
        return products

    def create_reviews(self, products, users):
        self.stdout.write('Creating reviews...')
        
        review_comments = [
            "Excellent product! Highly recommended.",
            "Good value for money.",
            "Exactly as described. Very satisfied.",
            "Great quality, fast shipping.",
            "Works perfectly, couldn't be happier.",
            "Decent product but could be better.",
            "Not bad, but I expected more for the price.",
            "Amazing! Exceeded my expectations.",
            "Solid product, would buy again.",
            "Perfect for my needs!"
        ]
        
        review_count = 0
        for product in products[:8]:  # Add reviews to first 8 products
            num_reviews = random.randint(2, 5)
            reviewers = random.sample(users['users'], num_reviews)
            
            for reviewer in reviewers:
                rating = random.randint(3, 5)  # Ratings between 3-5
                Review.objects.create(
                    product=product,
                    user=reviewer,
                    name=reviewer.first_name,
                    rating=rating,
                    comment=random.choice(review_comments)
                )
                review_count += 1
            
            # Update product rating
            reviews = product.review_set.all()
            product.numReviews = len(reviews)
            total = sum([r.rating for r in reviews])
            product.rating = total / len(reviews)
            product.save()
        
        self.stdout.write(f'Created {review_count} reviews')

    def create_orders(self, products, users):
        self.stdout.write('Creating orders...')
        
        order_count = 0
        for user in users['users']:
            # Create 1-2 orders per user
            num_orders = random.randint(1, 2)
            
            for _ in range(num_orders):
                # Random order details
                num_items = random.randint(1, 3)
                order_products = random.sample(products, num_items)
                
                subtotal = 0
                order_items_data = []
                
                for product in order_products:
                    qty = random.randint(1, 3)
                    price = float(product.price)
                    subtotal += price * qty
                    order_items_data.append({
                        'product': product,
                        'qty': qty,
                        'price': price
                    })
                
                tax = round(subtotal * 0.1, 2)  # 10% tax
                shipping = 10.00 if subtotal < 100 else 0  # Free shipping over $100
                total = round(subtotal + tax + shipping, 2)
                
                # Create order
                order = Order.objects.create(
                    user=user,
                    paymentMethod='PayPal',
                    taxPrice=tax,
                    shippingPrice=shipping,
                    totalPrice=total,
                    isPaid=random.choice([True, True, False]),  # 66% paid
                    isDelivered=False
                )
                
                # Set paid date for paid orders
                if order.isPaid:
                    order.paidAt = timezone.now() - timedelta(days=random.randint(1, 7))
                    # Some paid orders are delivered
                    if random.choice([True, False]):
                        order.isDelivered = True
                        order.deliveredAt = order.paidAt + timedelta(days=random.randint(1, 3))
                    order.save()
                
                # Create order items
                for item_data in order_items_data:
                    OrderItem.objects.create(
                        product=item_data['product'],
                        order=order,
                        name=item_data['product'].name,
                        qty=item_data['qty'],
                        price=item_data['price'],
                        image=item_data['product'].image.url if item_data['product'].image else ''
                    )
                
                # Create shipping address
                ShippingAddress.objects.create(
                    order=order,
                    address=f'{random.randint(100, 999)} Main Street',
                    city=random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']),
                    postalCode=f'{random.randint(10000, 99999)}',
                    country='USA'
                )
                
                order_count += 1
        
        self.stdout.write(f'Created {order_count} orders')