# 📚 BookNest - E-Commerce Platform for Books

> A full-featured, production-ready e-commerce platform built with Django for book lovers and online bookstores.

[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Overview

**BookNest** is a comprehensive e-commerce solution designed specifically for online bookstores. It provides a complete ecosystem for managing book inventory, processing orders, handling payments, and delivering excellent customer experiences.

Perfect for entrepreneurs looking to launch their own online bookstore with minimal setup and maximum features.

---

## ✨ Key Features

### 🛒 Customer Features
- **User Authentication**
  - Email & password registration with verification
  - Google OAuth social login
  - Password reset functionality
  - Secure session management

- **Shopping Experience**
  - Advanced product browsing with filters (category, price, language, author)
  - Product search and sorting
  - Detailed product pages with multiple images
  - Shopping cart with quantity management
  - Wishlist functionality
  - Product reviews and ratings

- **Checkout & Payments**
  - Multi-address management
  - Razorpay payment gateway integration
  - Multiple payment methods (Credit/Debit cards, UPI, Net Banking, Wallets)
  - Order confirmation emails
  - Invoice generation (PDF)

- **User Dashboard**
  - Order history with tracking
  - Digital wallet for refunds and cashback
  - Profile management
  - Address book
  - Wishlist management

### 🎛️ Admin Features
- **Product Management**
  - Add, edit, delete products
  - Category management
  - Inventory tracking
  - Image uploads (Cloudinary integration)
  - ISBN management

- **Order Management**
  - Order processing workflow
  - Order status updates
  - Cancellation handling
  - Refund processing

- **User Management**
  - User accounts overview
  - Block/unblock users
  - User activity monitoring

- **Marketing Tools**
  - Discount offers (product/category level)
  - Coupon code system
  - Sales reports and analytics

### 🔧 Technical Features
- **Security**
  - CSRF protection
  - Secure password hashing
  - Session security
  - SQL injection prevention
  - XSS protection

- **Performance**
  - Optimized database queries
  - Static file compression (WhiteNoise)
  - Image optimization (Cloudinary)
  - Caching strategies

- **Scalability**
  - Cloud-ready architecture
  - PostgreSQL for robust data handling
  - CDN integration for media files
  - Production deployment ready

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 6.0
- **Database**: PostgreSQL 12+
- **Authentication**: Django Auth + Google OAuth (social-auth-app-django)
- **Payment**: Razorpay Integration

### Frontend
- **Templates**: Django Templates
- **Styling**: HTML5, CSS3, Bootstrap 5
- **JavaScript**: Vanilla JS, AJAX
- **Icons**: Font Awesome

### Cloud Services
- **Media Storage**: Cloudinary
- **Email**: SMTP (Gmail)
- **Deployment**: Gunicorn + WhiteNoise

### Libraries & Tools
- **PDF Generation**: ReportLab, xhtml2pdf
- **Image Processing**: Pillow
- **Environment**: python-dotenv
- **Database URL**: dj-database-url

---

## 📋 Prerequisites

Before installation, ensure you have:

- Python 3.10 or higher
- PostgreSQL 12 or higher
- Git

**Required Service Accounts** (Free tiers available):
- [Cloudinary](https://cloudinary.com/) - Media storage
- [Razorpay](https://razorpay.com/) - Payment gateway
- [Google Cloud Console](https://console.cloud.google.com/) - OAuth authentication
- Gmail account with App Password enabled

---

## 🚀 Quick Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd BookNest-1
```

### 2. Setup Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```sql
-- In PostgreSQL
CREATE DATABASE booknest;
CREATE USER booknest_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE booknest TO booknest_user;
```

### 5. Configure Environment
Create a `.env` file in the root directory:
```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=booknest
DB_USER=booknest_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_client_id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_client_secret

RAZORPAY_KEY_ID=rzp_test_xxxxxxxxxxxx
RAZORPAY_KEY_SECRET=your_razorpay_secret

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 6. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py runserver
```

### 7. Access the Application
- **Main Site**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin_side/

---

## 📖 Detailed Documentation

For comprehensive installation instructions, troubleshooting, and configuration:

- **[Installation Guide](INSTALLATION_GUIDE.md)** - Complete setup instructions with detailed explanations
- **[Quick Start Guide](QUICK_START.md)** - Condensed reference for experienced developers

---

## 📁 Project Structure

```
BookNest-1/
├── admin_side/              # Admin dashboard & management
│   ├── templates/           # Admin HTML templates
│   ├── views.py            # Admin logic
│   └── models.py           # Product, Category, Offer models
├── cart_section/           # Shopping cart functionality
├── online_payment/         # Razorpay payment integration
├── user_authentication/    # Login, signup, OAuth
├── user_profile/          # User profiles & order history
├── user_wallet/           # Wallet & refund system
├── booknest/              # Django project settings
├── static/                # CSS, JS, images
├── templates/             # Base templates
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables (create this)
```

---

## 🎯 Use Cases

### Perfect For:
- ✅ Entrepreneurs starting an online bookstore
- ✅ Existing bookstores moving online
- ✅ Educational institutions selling course materials
- ✅ Publishers selling directly to consumers
- ✅ Book clubs and literary communities

### Business Models Supported:
- B2C (Business to Consumer)
- Inventory-based e-commerce
- Digital invoice generation
- Wallet-based refund system

---

## 🔐 Security Features

- ✅ CSRF token protection on all forms
- ✅ SQL injection prevention (Django ORM)
- ✅ XSS attack mitigation
- ✅ Secure password storage (Django's PBKDF2 algorithm)
- ✅ Session security with expiration
- ✅ HTTPS ready for production
- ✅ Environment-based configuration (no hardcoded secrets)

---

## 🧪 Testing

### Manual Testing Checklist
- [ ] User registration with email verification
- [ ] Google OAuth login
- [ ] Product browsing and filtering
- [ ] Add to cart and wishlist
- [ ] Checkout process
- [ ] Payment with test cards (Razorpay test mode)
- [ ] Order confirmation email
- [ ] Admin product management
- [ ] Order status updates
- [ ] Wallet refund system

### Test Payment Cards (Razorpay Test Mode)
```
Card Number: 4111 1111 1111 1111
CVV: Any 3 digits
Expiry: Any future date
```

---

## 🌐 Deployment

BookNest is deployment-ready for:

- **Railway** - One-click deployment
- **Render** - Automated deployments
- **Heroku** - Git-based deployment
- **AWS/GCP/Azure** - Traditional cloud hosting
- **VPS** - Self-hosted with Nginx + Gunicorn

Includes:
- `Procfile` for web server configuration
- `build.sh` for automated build process
- WhiteNoise for static file serving
- Gunicorn for production WSGI server

---

## 📊 Database Schema

### Core Models
- **User** - Extended Django User model
- **Product** - Book inventory with details
- **Category** - Product categorization
- **Order** - Customer orders
- **OrderItem** - Individual order line items
- **Cart** - Shopping cart items
- **Wishlist** - User wishlists
- **Wallet** - User wallet transactions
- **Offer** - Discount management
- **Coupon** - Promotional codes

---

## 🎨 Customization

### Easy to Customize
- **Branding**: Update logos and colors in `static/` directory
- **Email Templates**: Modify templates in respective app directories
- **Product Fields**: Extend models in `admin_side/models.py`
- **Payment Gateway**: Swap Razorpay with other providers
- **Themes**: Update CSS in `static/` directory

---

## 🤝 Support & Maintenance

### What's Included
- ✅ Clean, well-documented code
- ✅ Modular Django app structure
- ✅ Comprehensive installation guide
- ✅ Troubleshooting documentation
- ✅ Environment-based configuration

### Post-Purchase Support
- Code is fully yours to modify and extend
- No licensing restrictions for commercial use
- Update dependencies as needed
- Scale as your business grows

---

## 📜 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

### What This Means for You:
- ✅ Use commercially without restrictions
- ✅ Modify and customize freely
- ✅ Deploy unlimited instances
- ✅ No royalties or recurring fees

---

## 🚦 Getting Started Roadmap

### Immediate Setup (Day 1)
1. Install and configure the application
2. Setup admin account
3. Configure payment gateway (test mode)
4. Add initial categories

### Content Setup (Week 1)
1. Add book inventory
2. Upload product images
3. Configure offers and coupons
4. Test complete purchase flow

### Launch Preparation (Week 2)
1. Switch to production payment keys
2. Configure custom domain
3. Setup SSL certificate
4. Final testing on production environment

### Go Live! 🎉
1. Deploy to production server
2. Monitor initial orders
3. Gather customer feedback
4. Iterate and improve

---

## 📞 Additional Resources

- **[Django Documentation](https://docs.djangoproject.com/)**
- **[Razorpay Integration Docs](https://razorpay.com/docs/)**
- **[Cloudinary Django Guide](https://cloudinary.com/documentation/django_integration)**
- **[PostgreSQL Guide](https://www.postgresql.org/docs/)**

---

## ⭐ Why Choose BookNest?

1. **Production-Ready**: Not a prototype, fully functional platform
2. **Modern Stack**: Latest Django 6.0 with best practices
3. **Secure**: Industry-standard security implementations
4. **Scalable**: Designed to grow with your business
5. **Well-Documented**: Comprehensive guides for easy setup
6. **Clean Code**: Modular, maintainable, and extensible
7. **Complete Features**: Everything needed to run an online bookstore
8. **Payment Integrated**: Ready to accept real payments
9. **Mobile-Responsive**: Works on all devices
10. **Cost-Effective**: One-time purchase, no recurring fees

---

<div align="center">

**Ready to launch your online bookstore?**

Download BookNest and start selling books online today! 📚

---

Made with ❤️ for book lovers and entrepreneurs

</div>