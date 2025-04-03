# BookNest

BookNest is an e-commerce platform for books where users can browse, purchase, and manage their book collection.

## Features

- User authentication with email verification and Google Sign-in
- Book browsing with filters by category, price, language
- Shopping cart and checkout functionality
- Payment integration with Razorpay
- User profiles with order history
- Wishlist functionality
- Wallet system for refunds and cashback
- Admin dashboard for product, order, and user management
- Discount offers and coupon system

## Tech Stack

- Backend: Django
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Authentication: Django Authentication, Google OAuth
- Payment Gateway: Razorpay

## Installation

1. Clone the repository
```bash
git clone https://github.com/jerin-jaison/BookNest-Final.git
cd BookNest-Final
```

2. Create a virtual environment and activate it
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a .env file with the following variables:
```
DJANGO_SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_oauth_key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_oauth_secret
RAZORPAY_KEY_ID=your_razorpay_key
RAZORPAY_KEY_SECRET=your_razorpay_secret
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

## License

This project is licensed under the MIT License. 