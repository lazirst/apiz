# Test API for REST Endpoint Testing

A lightweight Python Flask REST API designed to generate randomized test data for API testing purposes.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/lazirst/apiz.git
cd apiz

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API
python app.py

# In another terminal, run tests
pip install pytest
pytest test_app.py -v
```

## Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation |
| `/api/health` | GET | Health check |
| `/api/users?count=5` | GET | Randomized users |
| `/api/products?count=10` | GET | Randomized products |
| `/api/orders?count=5` | GET | Randomized orders |
| `/api/posts?count=5` | GET | Randomized blog posts |
| `/api/comments?count=10` | GET | Randomized comments |

## Example Usage

```bash
# Get 10 random users
curl "http://localhost:5000/api/users?count=10"

# Get 25 random products
curl "http://localhost:5000/api/products?count=25"

# Get 50 random orders
curl "http://localhost:5000/api/orders?count=50"
```

## Testing

Run the test suite:

```bash
pytest test_app.py -v
```

Tests cover:
- Endpoint availability
- Response format validation
- Data randomization
- Query parameter handling
- Status codes

## Stack

- **Flask 3.0.0** - Lightweight web framework
- **Faker 22.0.0** - Realistic randomized data generation
- **Python 3.8+** - Runtime

Perfect for testing, load testing, and integration testing!
