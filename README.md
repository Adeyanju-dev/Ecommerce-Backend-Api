# Ecommerce Backend API

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Django REST Framework](https://img.shields.io/badge/DRF-REST%20API-red)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

A production-style **Ecommerce Backend API** built with **Django REST Framework**.

This project demonstrates how modern ecommerce backends work by implementing authentication, product management, cart functionality, checkout, payments, reviews, and shipping.

The API is fully documented using **Swagger/OpenAPI** and includes **automated API tests**.

---

# Features

- JWT Authentication (Register / Login / Token Refresh)
- Product & Category management
- Product search, filtering, ordering and pagination
- Shopping cart system
- Checkout system
- Order creation and order history
- Shipping address handling
- Inventory (stock) control
- Mock payment system
- Product reviews and ratings
- Role-based permissions (Admin vs User)
- API rate limiting
- Swagger API documentation
- Automated API tests

---

# Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT Authentication
- drf-spectacular (Swagger / OpenAPI)
- SQLite (development)
- PostgreSQL (production ready)

---

# Project Structure
```
Ecommerce-Backend-Api/
├── accounts/
├── products/
├── cart/
├── orders/
├── payments/
├── reviews/
├── core/
├── config/
└── manage.py
```

---

# Authentication

The API uses **JWT Authentication**.

### Login
POST /api/auth/login/


Response:
{
"access": "token",
"refresh": "token"
}


Use the access token in requests:
Authorization: Bearer <access_token>


---

# API Documentation

Swagger UI:
/api/docs/


OpenAPI schema:
/api/schema/


---

# Main API Endpoints

## Authentication
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/token/refresh/

---

## Products
GET /api/products/
GET /api/products/{slug}/

Supports:
- pagination
- filtering
- ordering
- search

---

## Cart
GET /api/cart/
POST /api/cart/add/
DELETE /api/cart/remove/{id}/

---

## Orders
POST /api/orders/checkout/
GET /api/orders/
GET /api/orders/{order_number}/

---

## Payments
POST /api/payments/initiate/{order_number}/
POST /api/payments/verify/{payment_reference}/

---

## Reviews
GET /api/products/{slug}/reviews/
POST /api/products/{slug}/reviews/

---

# Running the Project Locally
Clone the repository:
git clone https://github.com/Adeyanju-dev/Ecommerce-Backend-Api.git

Create a virtual environment:
python -m venv venv

Activate the environment:

Windows: 
venv\Scripts\activate

Mac/Linux: 
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Create superuser:
python manage.py createsuperuser

Run the server:
python manage.py runserver

API will run at:
http://127.0.0.1:8000

---

# Running Tests

python manage.py test

---

# Future Improvements

- Payment gateway integration (Paystack / Stripe)
- Email notifications for orders
- Wishlist system
- Discount & coupon system
- Docker containerization
- CI/CD pipeline
- Redis caching
- Background tasks with Celery

---

# License

MIT License

This project is built for **educational and portfolio purposes**.

---

# Links

- Live API: https://ecommerce-backend-api-k8c8.onrender.com

-Swagger Docs: https://ecommerce-backend-api-k8c8.onrender.com/api/docs/


Frontend: https://bespoke-biscotti-880746.netlify.app

