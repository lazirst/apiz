# API Testing with Randomized Test Data

A simple Python Flask REST API that generates randomized test data for API testing purposes. Perfect for testing API clients, load testing, and integration testing.

## Features

- **Random User Data** - Names, emails, phone numbers
- **Random Product Data** - Product names, prices, stock levels
- **Random Order Data** - Order numbers, customer names, totals, status
- **Random Blog Posts** - Titles, authors, content, view counts
- **Random Comments** - Post comments with ratings
- **Configurable Data Count** - Use query parameters to control how many items to generate

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lazirst/apiz.git
cd apiz
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Start the Flask development server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Get API Documentation
```
GET /
```

### Get Randomized Users
```
GET /api/users?count=5
```

Response:
```json
{
  "status": "success",
  "data": [
    {
      "id": 1234,
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "+1-234-567-8900",
      "age": 35
    }
  ]
}
```

### Get Randomized Products
```
GET /api/products?count=10
```

Response:
```json
{
  "status": "success",
  "data": [
    {
      "id": 5678,
      "name": "Quality Product",
      "price": 199.99,
      "stock": 450,
      "sku": "SKU-ABCD-1234"
    }
  ]
}
```

### Get Randomized Orders
```
GET /api/orders?count=5
```

Response:
```json
{
  "status": "success",
  "data": [
    {
      "id": 10001,
      "order_number": "ORD-12345678",
      "customer_name": "Jane Smith",
      "total": 1299.50,
      "status": "shipped",
      "created_at": "2026-07-01T10:06:19Z"
    }
  ]
}
```

### Get Randomized Posts
```
GET /api/posts?count=5
```

Response:
```json
{
  "status": "success",
  "data": [
    {
      "id": 8901,
      "title": "Amazing Technology Advances Today",
      "author": "Bob Johnson",
      "content": "Lorem ipsum dolor sit amet...",
      "views": 54321,
      "published_at": "2026-07-01T10:06:19Z"
    }
  ]
}
```

### Get Randomized Comments
```
GET /api/comments?count=10
```

Response:
```json
{
  "status": "success",
  "data": [
    {
      "id": 20001,
      "post_id": 8901,
      "author": "Alice Wonder",
      "text": "This is a great comment about the post.",
      "rating": 5,
      "created_at": "2026-07-01T10:06:19Z"
    }
  ]
}
```

### Health Check
```
GET /api/health
```

Response:
```json
{
  "status": "healthy",
  "message": "API is running"
}
```

## Query Parameters

All data endpoints support the `count` query parameter to control the number of items returned:

```
GET /api/users?count=20      # Returns 20 users
GET /api/products?count=50   # Returns 50 products
GET /api/orders?count=100    # Returns 100 orders
```

Default count is 5-10 depending on the endpoint.

## Testing Examples

Using `curl`:

```bash
# Get 10 users
curl "http://localhost:5000/api/users?count=10"

# Get 25 products
curl "http://localhost:5000/api/products?count=25"

# Get 50 orders
curl "http://localhost:5000/api/orders?count=50"
```

Using Python:

```python
import requests

response = requests.get('http://localhost:5000/api/users?count=5')
data = response.json()
print(data)
```

## Technologies

- **Flask** - Lightweight Python web framework
- **Faker** - Generate realistic fake data
- **Python 3.8+**

## License

MIT
