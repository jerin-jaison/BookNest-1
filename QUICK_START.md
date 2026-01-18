# BookNest - Quick Start Guide

This is a condensed version of the installation guide for experienced developers. For detailed instructions, see [INSTALLATION_GUIDE.md](./INSTALLATION_GUIDE.md).

## Prerequisites Checklist

- [ ] Python 3.10+
- [ ] PostgreSQL 12+
- [ ] Cloudinary account (free tier)
- [ ] Razorpay account (test keys)
- [ ] Google Cloud project (OAuth credentials)
- [ ] Gmail with App Password

---

## Quick Installation

### 1. Setup Environment

```bash
# Clone and navigate
cd BookNest-1

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup

```sql
-- In PostgreSQL
CREATE DATABASE booknest;
CREATE USER booknest_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE booknest TO booknest_user;
```

### 3. Environment Configuration

Create `.env` file in root directory:

```env
# Django
DJANGO_SECRET_KEY=<generate-random-key>
DEBUG=True

# Database
DB_NAME=booknest
DB_USER=booknest_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Email (Gmail App Password)
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=xxxx-xxxx-xxxx-xxxx

# Google OAuth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=xxx.apps.googleusercontent.com
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=xxxxxx

# Razorpay (Test Keys)
RAZORPAY_KEY_ID=rzp_test_xxxxx
RAZORPAY_KEY_SECRET=xxxxx

# Cloudinary
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=xxxxx
CLOUDINARY_API_SECRET=xxxxx
```

### 4. Run Application

```bash
# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Start server
python manage.py runserver
```

### 5. Access Application

- **Main Site**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/

---

## Service Setup Quick Links

### Gmail App Password
1. [Google Account Security](https://myaccount.google.com/security)
2. Enable 2-Step Verification
3. App Passwords → Mail → Generate

### Google OAuth
1. [Google Cloud Console](https://console.cloud.google.com/)
2. Create project → Enable Google+ API
3. Credentials → OAuth 2.0 Client ID
4. Redirect URI: `http://localhost:8000/auth/complete/google-oauth2/`

### Razorpay
1. [Razorpay Dashboard](https://dashboard.razorpay.com/)
2. Settings → API Keys → Generate Test Keys

### Cloudinary
1. [Cloudinary Dashboard](https://cloudinary.com/console)
2. Copy: Cloud Name, API Key, API Secret

---

## Common Commands

```bash
# Generate Django secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Run on different port
python manage.py runserver 8080

# Re-apply migrations
python manage.py migrate --run-syncdb

# Create new superuser
python manage.py createsuperuser

# Check for issues
python manage.py check
```

---

## Troubleshooting Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| Database connection error | Check PostgreSQL is running & verify `.env` credentials |
| Cloudinary upload fails | Restart server after updating `.env` |
| Email not sending | Use Gmail App Password (16 chars, no spaces) |
| Google OAuth redirect error | Add exact redirect URI in Google Cloud Console |
| Static files missing | Run `python manage.py collectstatic` |
| Port in use | Kill process or use different port |

---

## Project Structure

```
BookNest-1/
├── admin_side/          # Admin dashboard & management
├── cart_section/        # Shopping cart functionality
├── online_payment/      # Payment integration (Razorpay)
├── user_authentication/ # Login, signup, Google OAuth
├── user_profile/        # User profiles & order history
├── user_wallet/         # Wallet & refund system
├── booknest/            # Django project settings
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── .env                 # Environment variables (create this)
```

---

## Next Steps After Installation

1. ✅ Login to admin panel (`/admin`)
2. ✅ Add book categories
3. ✅ Add products (books)
4. ✅ Test user registration
5. ✅ Test Google login
6. ✅ Test cart and checkout flow
7. ✅ Test payment (use Razorpay test cards)

---

For detailed explanations and troubleshooting, refer to **[INSTALLATION_GUIDE.md](./INSTALLATION_GUIDE.md)**
