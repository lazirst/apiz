import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'


def test_api_index(client):
    """Test API documentation endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'endpoints' in data
    assert 'name' in data


def test_get_users(client):
    """Test users endpoint"""
    response = client.get('/api/users?count=5')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert len(data['data']) == 5
    assert 'name' in data['data'][0]
    assert 'email' in data['data'][0]


def test_get_users_default(client):
    """Test users endpoint with default count"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['data']) == 5


def test_get_products(client):
    """Test products endpoint"""
    response = client.get('/api/products?count=10')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert len(data['data']) == 10
    assert 'name' in data['data'][0]
    assert 'price' in data['data'][0]
    assert 'stock' in data['data'][0]


def test_get_orders(client):
    """Test orders endpoint"""
    response = client.get('/api/orders?count=3')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert len(data['data']) == 3
    assert 'order_number' in data['data'][0]
    assert 'total' in data['data'][0]
    assert data['data'][0]['status'] in ['pending', 'processing', 'shipped', 'delivered']


def test_get_posts(client):
    """Test posts endpoint"""
    response = client.get('/api/posts?count=2')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert len(data['data']) == 2
    assert 'title' in data['data'][0]
    assert 'author' in data['data'][0]


def test_get_comments(client):
    """Test comments endpoint"""
    response = client.get('/api/comments?count=7')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert len(data['data']) == 7
    assert 'author' in data['data'][0]
    assert 'rating' in data['data'][0]


def test_data_randomization(client):
    """Test that data is randomized between requests"""
    response1 = client.get('/api/users?count=1')
    data1 = json.loads(response1.data)
    
    response2 = client.get('/api/users?count=1')
    data2 = json.loads(response2.data)
    
    # Names should be different (extremely high probability)
    assert data1['data'][0]['name'] != data2['data'][0]['name']


def test_large_count(client):
    """Test with large count parameter"""
    response = client.get('/api/users?count=100')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['data']) == 100
