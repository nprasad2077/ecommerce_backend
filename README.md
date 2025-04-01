# E-Commerce Backend Documentation

This documentation provides a comprehensive guide to using the Django-based e-commerce backend API. The backend is built with Django REST Framework and includes JWT authentication for secure API access.

## Table of Contents

1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [API Endpoints](#api-endpoints)
   - [User Endpoints](#user-endpoints)
   - [Product Endpoints](#product-endpoints)
   - [Order Endpoints](#order-endpoints)
5. [Authentication](#authentication)
6. [Models](#models)
7. [Frontend Requirements](#frontend-requirements)
8. [API Usage Examples](#api-usage-examples)

## Overview

This e-commerce backend provides a complete RESTful API for an online store. Key features include:

- **User Management**: Registration, authentication, and profile management
- **Product Management**: Create, read, update, and delete products with image upload capability
- **Review System**: Product ratings and reviews
- **Order Processing**: Create orders, update payment and delivery status
- **Admin Panel**: Manage products, users, and orders

## System Requirements

- Python 3.8+
- Django 5.1.7
- Django REST Framework 3.15.2
- JWT Authentication
- Pillow for image processing

## Installation

1. Clone the repository
2. Install required packages:

   ```
   pip install -r requirements.txt
   ```

3. Run migrations:

   ```
   python manage.py migrate
   ```

4. Create a superuser:

   ```
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```
   python manage.py runserver
   ```

## API Endpoints

### User Endpoints

| Endpoint | Method | Description | Access |
|----------|--------|-------------|--------|
| `/api/users/login/` | POST | Obtain JWT token | Public |
| `/api/users/register/` | POST | Register a new user | Public |
| `/api/users/profile/` | GET | Get user profile | Authenticated |
| `/api/users/profile/update/` | PUT | Update user profile | Authenticated |
| `/api/users/` | GET | Get all users | Admin |
| `/api/users/<id>/` | GET | Get user by ID | Admin |
| `/api/users/update/<id>/` | PUT | Update user | Admin |
| `/api/users/delete/<id>/` | DELETE | Delete user | Admin |

### Product Endpoints

| Endpoint | Method | Description | Access |
|----------|--------|-------------|--------|
| `/api/products/` | GET | Get all products (with pagination) | Public |
| `/api/products/?keyword=` | GET | Search for specific product by keyword | Public |
| `/api/products/?category=` | GET | Search all products by Category | Public |
| `/api/products/<id>/` | GET | Get product details | Public |
| `/api/products/create/` | POST | Create new product | Admin |
| `/api/products/update/<id>/` | PUT | Update product | Admin |
| `/api/products/delete/<id>/` | DELETE | Delete product | Admin |
| `/api/products/upload/` | POST | Upload product image | Admin |
| `/api/products/<id>/reviews/` | POST | Create product review | Authenticated |
| `/api/products/top/` | GET | Get top rated products | Public |
| `/api/products/categories/` | GET | Get list of categories | Public |

### Order Endpoints

| Endpoint | Method | Description | Access |
|----------|--------|-------------|--------|
| `/api/orders/` | GET | Get all orders | Admin |
| `/api/orders/add/` | POST | Create new order | Authenticated |
| `/api/orders/myorders/` | GET | Get user's orders | Authenticated |
| `/api/orders/<id>/` | GET | Get order by ID | Authenticated/Admin |
| `/api/orders/<id>/pay/` | PUT | Update order to paid | Authenticated |
| `/api/orders/<id>/deliver/` | PUT | Update order to delivered | Admin |

## Authentication

The API uses JWT (JSON Web Token) authentication through `djangorestframework_simplejwt`.

### JWT Token

To authenticate requests, include the JWT token in the request header:

```
Authorization: Bearer <token>
```

### Obtaining a Token

Send a POST request to `/api/users/login/` with user credentials:

```json
{
  "username": "user@example.com",
  "password": "yourpassword"
}
```

The response includes:

- User information
- Access token

### Token Lifetime

- Access Token: 1 day
- Refresh Token: 7 days

## Models

### User

The system uses Django's built-in `User` model with additional serialized fields for the API:

- `_id`: User ID
- `username`: Automatically set to email
- `email`: User's email address
- `name`: User's name
- `isAdmin`: Admin status

### Product

Products are stored in the `Product` model:

- `_id`: Product ID (primary key)
- `user`: Creator of the product (admin user)
- `name`: Product name
- `image`: Product image path
- `brand`: Product brand
- `category`: Product category
- `description`: Detailed description
- `rating`: Average rating from reviews
- `numReviews`: Number of reviews
- `price`: Product price
- `countInStock`: Available quantity
- `createdAt`: Timestamp of creation

### Review

Product reviews are stored in the `Review` model:

- `_id`: Review ID (primary key)
- `product`: Related product
- `user`: User who created the review
- `name`: User's name
- `rating`: Rating (1-5)
- `comment`: Review text
- `createdAt`: Timestamp of creation

### Order

Orders are managed through the following models:

- `Order`: Main order data
  - `_id`: Order ID (primary key)
  - `user`: User who placed the order
  - `paymentMethod`: Method of payment
  - `taxPrice`: Tax amount
  - `shippingPrice`: Shipping cost
  - `totalPrice`: Total order amount
  - `isPaid`: Payment status
  - `paidAt`: Payment timestamp
  - `isDelivered`: Delivery status
  - `deliveredAt`: Delivery timestamp
  - `createdAt`: Order creation timestamp

- `OrderItem`: Individual items in an order
  - `_id`: Item ID (primary key)
  - `product`: Related product
  - `order`: Parent order
  - `name`: Product name
  - `qty`: Quantity ordered
  - `price`: Item price
  - `image`: Product image path

- `ShippingAddress`: Delivery information
  - `_id`: Address ID (primary key)
  - `order`: Related order
  - `address`: Street address
  - `city`: City
  - `postalCode`: Postal code
  - `country`: Country
  - `shippingPrice`: Shipping cost

## Frontend Requirements

To build a complete e-commerce application, the frontend needs to implement:

### User Interface Components

1. **Authentication Pages**
   - Login page
   - Registration page
   - Profile page with update capability
   - Password update form

2. **Product Pages**
   - Product listing with pagination
   - Product detail page
   - Product search functionality
   - Product reviews and ratings
   - Featured/top products section

3. **Shopping Cart**
   - Add to cart functionality
   - Cart management (update quantity, remove items)
   - Cart persistence (local storage)

4. **Checkout Process**
   - Shipping information form
   - Payment method selection
   - Order summary
   - Order confirmation

5. **User Dashboard**
   - Order history
   - Profile management

6. **Admin Dashboard**
   - User management section
   - Product management (CRUD operations)
   - Order management
   - Delivery status updates

### API Integration

The frontend needs to implement proper API calls using:

1. **Authentication**
   - Store JWT token securely
   - Include JWT token in request headers
   - Handle expired tokens and authentication errors

2. **State Management**
   - User state (authentication status)
   - Cart state
   - Product state
   - Order state

3. **Form Handling**
   - Form validation
   - Error message display
   - Success notifications

4. **Image Handling**
   - Product image display
   - Image upload for admin product creation/edit

## API Usage Examples

### User Registration

**Request:**

```http
POST /api/users/register/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

**Response:**

```json
{
  "id": 3,
  "_id": 3,
  "username": "john@example.com",
  "email": "john@example.com",
  "name": "John Doe",
  "isAdmin": false,
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### User Login

**Request:**

```http
POST /api/users/login/
Content-Type: application/json

{
  "username": "john@example.com",
  "password": "securepassword"
}
```

**Response:**

```json
{
  "id": 3,
  "_id": 3,
  "username": "john@example.com",
  "email": "john@example.com",
  "name": "John Doe",
  "isAdmin": false,
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Get Product List

**Request:**

```http
GET /api/products/
```

**Response:**

```json
{
  "products": [
    {
      "_id": 1,
      "name": "Airpods Wireless",
      "image": "/images/airpods.jpg",
      "description": "Bluetooth technology...",
      "brand": "Apple",
      "category": "Electronics",
      "price": 89.99,
      "countInStock": 10,
      "rating": 4.5,
      "numReviews": 12,
      "reviews": []
    },
    /* More products */
  ],
  "page": 1,
  "pages": 3
}
```

### Create Product Review

**Request:**

```http
POST /api/products/5/reviews/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
Content-Type: application/json

{
  "rating": 5,
  "comment": "Excellent product, highly recommended!"
}
```

**Response:**

```
"Review Added"
```

### Create Order

**Request:**

```http
POST /api/orders/add/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
Content-Type: application/json

{
  "orderItems": [
    {
      "product": 1,
      "name": "Airpods Wireless",
      "qty": 2,
      "price": 89.99,
      "image": "/images/airpods.jpg"
    }
  ],
  "shippingAddress": {
    "address": "123 Main St",
    "city": "Boston",
    "postalCode": "02108",
    "country": "USA"
  },
  "paymentMethod": "PayPal",
  "taxPrice": 13.50,
  "shippingPrice": 10.00,
  "totalPrice": 203.48
}
```

**Response:**

```json
{
  "_id": 3,
  "orderItems": [
    {
      "_id": 4,
      "name": "Airpods Wireless",
      "qty": 2,
      "price": 89.99,
      "image": "/images/airpods.jpg",
      "product": 1,
      "order": 3
    }
  ],
  "shippingAddress": {
    "_id": 2,
    "address": "123 Main St",
    "city": "Boston",
    "postalCode": "02108",
    "country": "USA",
    "shippingPrice": null,
    "order": 3
  },
  "user": {
    "id": 3,
    "_id": 3,
    "username": "john@example.com",
    "email": "john@example.com",
    "name": "John Doe",
    "isAdmin": false
  },
  "paymentMethod": "PayPal",
  "taxPrice": 13.50,
  "shippingPrice": 10.00,
  "totalPrice": 203.48,
  "isPaid": false,
  "paidAt": null,
  "isDelivered": false,
  "deliveredAt": null,
  "createdAt": "2025-03-27T21:45:23.872243Z"
}
```

### Update Order to Paid

**Request:**

```http
PUT /api/orders/3/pay/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

**Response:**

```
"Order was paid"
```

### Upload Product Image

**Request:**

```http
POST /api/products/upload/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
Content-Type: multipart/form-data

{
  "product_id": 1,
  "image": <file>
}
```

**Response:**

```
"Image was uploaded"
```
