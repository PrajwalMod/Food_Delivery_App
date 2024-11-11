# Food Delivery App

This is a microservice-based food delivery app built with Flask.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a `.env` file and add your environment variables.
5. Run the application:
    ```sh
    python -m app.app
    ```

## Architecture

The application is structured as a microservices-based architecture with the following components:

```plaintext
+---------------------+       +--------------------------------------+          +---------------------------+
|     User Service    |       |    Order Service                     |          |  Restaurant Service       |
|---------------------|       |--------------------------------------|          |---------------------------|
| - Register User     |       | - Create Order                       |          | - Add Restaurant          |
|   POST /register    |       |   POST /orders/                      |          |   POST /restaurants/      |
| - Login User        |       | - Update Order                       |          | - Update Restaurant       |
|   POST /login       |       |   PUT /orders/{id}                   |          |   PUT /restaurants/{id}   |
| - Get User Profile  |       | - Get Order                          |          | - Get Restaurant          |
|   GET /{user_id}    |       |   GET /orders/{id}                   |          |   GET /restaurants/{id}   |
| - Update User       |       | - Order Status                       |          | - Search Restaurants      |
|   PUT /{user_id}    |       |   GET /orders/user/{user_id}/status  |          |   GET /restaurants/search |
+---------------------+       | - Pickup Order                       |          +---------------------------+
         |                    |   PUT /orders/{id}/pickup            |
         |                    | - Deliver Order                      |
         |                    |   PUT /orders/{id}/deliver           |
         |                    +--------------------------------------+
         |                           |
         v                           v
+---------------------+       +---------------------+
| Authentication &    |       |     Database        |
| Authorization       |       |---------------------|
|---------------------|       | - User Data         |
| - JWT Tokens        |       | - Order Data        |
| - Role Middleware   |       | - Restaurant Data   |
+---------------------+       +---------------------+
```
### As you can see the application is structured into three main microservices:
  1. **User Service:** Handles user-related operations such as registration, login, profile retrieval, and profile updates.
  2. **Order Service:** Manages order-related operations such as creating orders, updating order statuses, and retrieving order details.
  3. **Restaurant Service:** Handles restaurant-related operations such as adding restaurants, updating restaurant details, and searching for restaurants.

### API Architecture Style
  The API follows the RESTful (Representational State Transfer) architecture style. This includes:
  1. **Resource-Based URLs:** The API endpoints are structured around resources such as users, orders, and restaurants.
  2. **HTTP Methods:** The API uses standard HTTP methods to perform CRUD (Create, Read, Update, Delete) operations.
  3. **Statelessness:** Each API request contains all the information needed to process the request, typically through the use of tokens for authentication and authorization.
  4. **Use of JSON:** The API uses JSON as the format for request and response bodies.
  5. **Clear Separation of Concerns:** The application is structured with separate services for users, orders, and restaurants, each with its own set of endpoints and responsibilities.

## Roles and Permissions
  ### Roles
  1. **User:** Can register, login, view and update their profile, place orders, and view order statuses.
  2. **Restaurant Owner:** Can add, update, and view restaurant details, and update order statuses to "Accepted" or "Rejected".
  3. **Delivery Agent:** Can update order statuses to "Picked Up" and "Delivered".
  ### Permissions
  1. **User:** Access to user-related endpoints.
  2. **Restaurant Owner:** Access to restaurant-related endpoints and order status updates.
  3. **Delivery Agent:** Access to order status updates for delivery.

## Order Statuses
  The following order statuses are used to track the progress of an order:
  1. **Pending:** The default status when an order is created.
  2. **Accepted:** The order has been accepted by the restaurant.
  3. **Rejected:** The order has been rejected by the restaurant.
  4. **Picked Up:** The order has been picked up by the delivery agent.
  5. **Delivered:** The order has been delivered to the customer.

### Data Validation
  The application includes basic data validation for email and password fields:
  1. The ``validate_email`` function ensures that the email format is valid using a regular expression.
  2. The ``validate_password`` function ensures that the password is strong by checking its length and the presence of digits.

## Endpoints

### User Endpoints
- **POST /api/users/register**: Register a new user.
  - **Request Body:**
    ```json
    {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "password",
      "role": "user"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "User registered successfully"
    }
    ```

- **POST /api/users/login**: User login.
  - **Request Body:**
    ```json
    {
      "username": "testuser",
      "password": "password"
    }
    ```
  - **Response:**
    ```json
    {
      "token": "jwt_token"
    }
    ```

- **GET /api/users/<user_id>**: Get user profile.
  - **Response:**
    ```json
    {
      "username": "testuser",
      "email": "testuser@example.com",
      "phone": "1234567890",
      "delivery_address": "123 Test St",
      "payment_info": "Payment Info"
    }
    ```

- **PUT /api/users/<user_id>**: Update user details.
  - **Request Body:**
    ```json
    {
      "email": "newemail@example.com",
      "phone": "1234567890",
      "delivery_address": "123 New St",
      "payment_info": "New Payment Info"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "User details updated successfully"
    }
    ```

### Order Endpoints
- **POST /api/orders/**: Create a new order.
  - **Request Body:**
    ```json
    {
      "user_id": "testuser",
      "restaurant_id": "testrestaurant",
      "items": ["item1", "item2"],
      "total_price": 100.0
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Order created successfully"
    }
    ```

- **GET /api/orders/<order_id>**: Get order details.
  - **Response:**
    ```json
    {
      "user_id": "testuser",
      "restaurant_id": "testrestaurant",
      "items": ["item1", "item2"],
      "total_price": 100.0,
      "status": "Pending"
    }
    ```

- **GET /api/orders/user/<user_id>/status**: Get the status of orders for a user.
  - **Response:**
    ```json
    [
      {
        "user_id": "testuser",
        "restaurant_id": "testrestaurant",
        "items": ["item1", "item2"],
        "total_price": 100.0,
        "status": "Pending"
      }
    ]
    ```

- **PUT /api/orders/<order_id>/status**: Update order status (for restaurant owners).
  - **Request Body:**
    ```json
    {
      "status": "Accepted"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Order status updated successfully"
    }
    ```

- **PUT /api/orders/<order_id>/pickup**: Update order status to picked up (for delivery agents).
  - **Request Body:**
    ```json
    {
      "status": "Picked Up"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Order picked up successfully"
    }
    ```

- **PUT /api/orders/<order_id>/deliver**: Update order status to delivered (for delivery agents).
  - **Request Body:**
    ```json
    {
      "status": "Delivered"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Order delivered successfully"
    }
    ```

### Restaurant Endpoints
- **POST /api/restaurants/**: Add a new restaurant (for restaurant owners).
  - **Request Body:**
    ```json
    {
      "name": "Test Restaurant",
      "address": "123 Test St",
      "cuisine": "Test Cuisine",
      "menu": [
        {
          "name": "item1",
          "price": 10.0
        },
        {
          "name": "item2",
          "price": 15.0
        }
      ],
      "work_hours": "9 AM - 9 PM"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Restaurant added successfully"
    }
    ```

- **GET /api/restaurants/<restaurant_id>**: Get restaurant details.
  - **Response:**
    ```json
    {
      "name": "Test Restaurant",
      "address": "123 Test St",
      "cuisine": "Test Cuisine",
      "menu": [
        {
          "name": "item1",
          "price": 10.0
        },
        {
          "name": "item2",
          "price": 15.0
        }
      ],
      "work_hours": "9 AM - 9 PM"
    }
    ```

- **PUT /api/restaurants/<restaurant_id>**: Update restaurant details (for restaurant owners).
  - **Request Body:**
    ```json
    {
      "address": "123 New St",
      "cuisine": "New Cuisine",
      "menu": [
        {
          "name": "item1",
          "price": 12.0
        },
        {
          "name": "item2",
          "price": 18.0
        }
      ],
      "work_hours": "10 AM - 10 PM"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Restaurant details updated successfully"
    }
    ```

- **GET /api/restaurants/search**: Search for restaurants.
  - **Query Parameters:**
    - `cuisine` (optional): Filter by cuisine.
    - `max_price` (optional): Filter by maximum price.
  - **Response:**
    ```json
    [
      {
        "name": "Test Restaurant",
        "address": "123 Test St",
        "cuisine": "Test Cuisine",
        "menu": [
          {
            "name": "item1",
            "price": 10.0
          },
          {
            "name": "item2",
            "price": 15.0
          }
        ],
        "work_hours": "9 AM - 9 PM"
      }
    ]
    ```

# Running Tests

To ensure everything is working correctly, run your automated tests using `unittest`:

#### Using `unittest`
```sh
python -m unittest <test>
