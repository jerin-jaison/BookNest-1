````md
# 📚 BookNest

BookNest is a full-featured Django-based e-commerce platform for books, built with real-world business logic and production-style architecture. The project supports multiple payment methods, wallet management, returns and refunds, offers, coupons, OTP security, and a powerful admin panel.

---

## 🚀 Features

### 👤 User Features
- User registration and authentication
- Email verification
- Google Sign-In using OAuth2
- Browse books with category, price, and language filters
- Product detail pages
- Shopping cart and wishlist
- Secure checkout flow
- Multiple payment methods:
  - Razorpay (Online Payment)
  - Wallet payment
  - Cash on Delivery (COD)
- Order history and order tracking
- Wallet system for refunds and cashback
- Coupon and discount application
- Reviews and ratings
- OTP-based verification for enhanced security

---

### 🛠️ Admin Features
- Admin dashboard
- Customer management
- Product management (add, edit, delete books)
- Category management
- Order management (online & COD)
- Return and refund handling
- Wallet management and wallet history
- Offers and discount management
- Coupon creation and validation
- Referral history tracking
- Transaction history (Razorpay, wallet, COD)
- Review moderation

---

## 🧰 Tech Stack
- Backend: Django
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Authentication: Django Authentication, Google OAuth2
- Payment Gateway: Razorpay
- Security: OTP verification, CSRF protection, environment-based secrets

---

## 📦 Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/jerin-jaison/BookNest-Final.git
cd BookNest-Final
````

---

### Create and Activate Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Environment Variables

Create a `.env` file in the root directory using the structure below:

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port

EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_client_id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_client_secret

RAZORPAY_KEY_ID=your_razorpay_key
RAZORPAY_KEY_SECRET=your_razorpay_secret
```

---

### Generate Django Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Paste the generated key into the `.env` file as `DJANGO_SECRET_KEY`.

---

## 🔑 Google OAuth2 Configuration

### Authorized Origins

```
http://localhost:8000
```

### Authorized Redirect URI

```
http://localhost:8000/accounts/google/login/callback/
```

Add the generated Client ID and Client Secret to the `.env` file.

---

## 💳 Razorpay Configuration

* Create a Razorpay account
* Use test keys for development
* Add Razorpay credentials to the `.env` file

---

## 🗄️ Database Migration

```bash
python manage.py migrate
```

---

## 👤 Create Admin User

```bash
python manage.py createsuperuser
```

---

## ▶️ Run Development Server

```bash
python manage.py runserver
```

Access the application at:

```
http://127.0.0.1:8000/
```

---

## 🎯 Ideal For

* Final year or mini project submissions
* Learning Django e-commerce architecture
* Freelancers building client-ready stores
* Small businesses and startup MVPs

---

## 🔒 Security Notes

* The `.env` file is excluded from version control
* Each installation requires unique credentials
* Secret keys and API keys must never be shared

---

## 📜 License

This project is provided for personal and commercial use.
Redistribution or resale of the source code without permission is prohibited.

---

## 📞 Support

Basic setup support is provided after purchase.

---

## ✅ Summary

BookNest demonstrates a real-world Django e-commerce implementation with secure authentication, multiple payment methods, wallet accounting, return and refund workflows, and a production-style admin panel.

```
```
