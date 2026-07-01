from flask import Flask, jsonify, request
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()


@app.route('/api/users', methods=['GET'])
def get_users():
    """Return a list of randomized test users"""
    count = request.args.get('count', 5, type=int)
    users = [
        {
            'id': fake.random_int(min=1, max=10000),
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'age': fake.random_int(min=18, max=80),
        }
        for _ in range(count)
    ]
    return jsonify({'status': 'success', 'data': users})


@app.route('/api/products', methods=['GET'])
def get_products():
    """Return a list of randomized test products"""
    count = request.args.get('count', 10, type=int)
    products = [
        {
            'id': fake.random_int(min=1, max=50000),
            'name': fake.word().capitalize() + ' ' + fake.word().capitalize(),
            'price': round(random.uniform(10, 500), 2),
            'stock': fake.random_int(min=0, max=1000),
            'sku': fake.bothify(text='SKU-????-####'),
        }
        for _ in range(count)
    ]
    return jsonify({'status': 'success', 'data': products})


@app.route('/api/orders', methods=['GET'])
def get_orders():
    """Return a list of randomized test orders"""
    count = request.args.get('count', 5, type=int)
    orders = [
        {
            'id': fake.random_int(min=1, max=100000),
            'order_number': fake.bothify(text='ORD-########'),
            'customer_name': fake.name(),
            'total': round(random.uniform(50, 5000), 2),
            'status': random.choice(['pending', 'processing', 'shipped', 'delivered']),
            'created_at': fake.iso8601(),
        }
        for _ in range(count)
    ]
    return jsonify({'status': 'success', 'data': orders})


@app.route('/api/posts', methods=['GET'])
def get_posts():
    """Return a list of randomized test blog posts"""
    count = request.args.get('count', 5, type=int)
    posts = [
        {
            'id': fake.random_int(min=1, max=10000),
            'title': fake.sentence(nb_words=6),
            'author': fake.name(),
            'content': fake.paragraph(nb_sentences=5),
            'views': fake.random_int(min=0, max=100000),
            'published_at': fake.iso8601(),
        }
        for _ in range(count)
    ]
    return jsonify({'status': 'success', 'data': posts})


@app.route('/api/comments', methods=['GET'])
def get_comments():
    """Return a list of randomized test comments"""
    count = request.args.get('count', 10, type=int)
    comments = [
        {
            'id': fake.random_int(min=1, max=50000),
            'post_id': fake.random_int(min=1, max=10000),
            'author': fake.name(),
            'text': fake.sentence(nb_words=20),
            'rating': fake.random_int(min=1, max=5),
            'created_at': fake.iso8601(),
        }
        for _ in range(count)
    ]
    return jsonify({'status': 'success', 'data': comments})


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'API is running'}), 200


@app.route('/', methods=['GET'])
def index():
    """API documentation"""
    return jsonify({
        'name': 'Test Data API',
        'version': '1.0.0',
        'description': 'REST API for generating randomized test data',
        'endpoints': {
            'GET /api/users': 'Get randomized user data (query param: count)',
            'GET /api/products': 'Get randomized product data (query param: count)',
            'GET /api/orders': 'Get randomized order data (query param: count)',
            'GET /api/posts': 'Get randomized blog post data (query param: count)',
            'GET /api/comments': 'Get randomized comment data (query param: count)',
            'GET /api/health': 'Health check endpoint',
        }
    }), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
