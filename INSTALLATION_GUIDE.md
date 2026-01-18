# BookNest E-Commerce Platform - Installation Guide

Welcome to BookNest! This comprehensive guide will help you set up and run the BookNest e-commerce platform on your local machine or server.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Prerequisites](#prerequisites)
3. [Installation Steps](#installation-steps)
4. [Database Setup](#database-setup)
5. [Environment Configuration](#environment-configuration)
6. [Third-Party Services Setup](#third-party-services-setup)
7. [Running the Application](#running-the-application)
8. [Admin Panel Setup](#admin-panel-setup)
9. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **Python**: 3.10 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 5GB free disk space
- **Internet**: Required for third-party service integrations

### Software Requirements
- Python 3.10+
- PostgreSQL 12+ (Database)
- Git (for cloning the repository)
- pip (Python package manager)

---

## Prerequisites

Before you begin, ensure you have the following accounts and credentials:

### Required Accounts
1. **PostgreSQL Database** - Local or cloud-hosted
2. **Cloudinary Account** - For media/image storage (Free tier available)
3. **Razorpay Account** - For payment processing (Test/Live credentials)
4. **Google Cloud Console** - For Google OAuth authentication
5. **Gmail Account** - For sending emails (with App Password enabled)

### Optional
- Domain Name (for production deployment)
- SSL Certificate (for HTTPS in production)

---

## Installation Steps

### Step 1: Clone the Repository

```bash
# Navigate to your desired directory
cd /path/to/your/projects

# Clone the repository
git clone <your-repository-url>
cd BookNest-1
```

### Step 2: Create Virtual Environment

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install all required packages including:
- Django 6.0
- PostgreSQL adapter (psycopg2-binary)
- Cloudinary SDK
- Razorpay SDK
- Social Auth for Google OAuth
- PDF generation libraries
- And more...

⏱️ **Note**: Installation may take 3-5 minutes depending on your internet speed.

---

## Database Setup

### Step 1: Install PostgreSQL

**Windows:**
1. Download PostgreSQL from [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/)
2. Run the installer and follow the setup wizard
3. Remember the password you set for the `postgres` user

**macOS:**
```bash
brew install postgresql@14
brew services start postgresql@14
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### Step 2: Create Database

1. Open PostgreSQL command line (psql):

**Windows:**
```bash
psql -U postgres
```

**macOS/Linux:**
```bash
sudo -u postgres psql
```

2. Create the database and user:

```sql
-- Create database
CREATE DATABASE booknest;

-- Create user (optional, or use existing postgres user)
CREATE USER booknest_user WITH PASSWORD 'your_secure_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE booknest TO booknest_user;

-- Exit psql
\q
```

### Step 3: Verify Database Connection

Test your database connection:
```bash
psql -U booknest_user -d booknest -h localhost
```

If successful, you'll see the PostgreSQL prompt. Type `\q` to exit.

---

## Environment Configuration

### Step 1: Create .env File

In the root directory of the project (where `manage.py` is located), create a file named `.env`:

```bash
# Copy the example file
cp .env.example .env
```

### Step 2: Configure Environment Variables

Open the `.env` file and update all values:

```env
# Django Secret Key
# Generate using: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
DJANGO_SECRET_KEY=your-generated-secret-key-here

# Debug Mode (Set to False in production)
DEBUG=True

# Database Configuration
DB_NAME=booknest
DB_USER=booknest_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# For cloud deployment (Railway, Render, etc.), use DATABASE_URL instead:
# DATABASE_URL=postgresql://user:password@host:port/database

# Email Settings (Gmail)
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_16_character_app_password

# Google OAuth2 Settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_client_id.apps.googleusercontent.com
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_client_secret

# Razorpay Settings
RAZORPAY_KEY_ID=rzp_test_xxxxxxxxxxxx
RAZORPAY_KEY_SECRET=your_razorpay_secret_key

# Cloudinary Settings
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

---

## Third-Party Services Setup

### 1. Gmail App Password Setup

1. Go to your Google Account settings: [https://myaccount.google.com/](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification** (enable if not already enabled)
3. Scroll down to **App passwords**
4. Select app: **Mail**, Select device: **Other (Custom name)**
5. Enter "BookNest" and click **Generate**
6. Copy the 16-character password (without spaces)
7. Add to `.env` as `EMAIL_HOST_PASSWORD`

### 2. Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable **Google+ API**
4. Go to **Credentials** → **Create Credentials** → **OAuth 2.0 Client ID**
5. Configure OAuth consent screen:
   - User Type: External
   - App name: BookNest
   - Add scopes: email, profile
6. Create OAuth Client ID:
   - Application type: Web application
   - Authorized redirect URIs:
     - `http://localhost:8000/auth/complete/google-oauth2/`
     - `http://127.0.0.1:8000/auth/complete/google-oauth2/`
     - Add your production domain URL when deploying
7. Copy **Client ID** and **Client Secret** to `.env`

### 3. Razorpay Setup

1. Sign up at [https://razorpay.com/](https://razorpay.com/)
2. Go to **Settings** → **API Keys**
3. Generate **Test Keys** for development
4. Copy **Key ID** and **Key Secret** to `.env`
5. For production, generate **Live Keys** and update `.env`

**Important**: Test mode allows testing without real transactions.

### 4. Cloudinary Setup

1. Sign up at [https://cloudinary.com/](https://cloudinary.com/) (Free tier: 25GB storage)
2. Go to **Dashboard**
3. Find your credentials:
   - Cloud Name
   - API Key
   - API Secret
4. Copy all three values to `.env`

---

## Running the Application

### Step 1: Apply Database Migrations

```bash
python manage.py migrate
```

This will create all necessary database tables. You should see output like:
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

### Step 2: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts:
- Username: (your choice, e.g., `admin`)
- Email: (your email)
- Password: (choose a strong password)
- Password confirmation: (repeat password)

### Step 3: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

This gathers all static files (CSS, JavaScript, images) into one location.

### Step 4: Start Development Server

```bash
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 5: Access the Application

Open your browser and navigate to:
- **Main Site**: [http://localhost:8000/](http://localhost:8000/)
- **Admin Panel**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Admin Panel Setup

### Step 1: Access Admin Panel

1. Go to [http://localhost:8000/admin/](http://localhost:8000/admin/)
2. Login with the superuser credentials you created

### Step 2: Add Categories

1. Click on **Categories**
2. Add book categories (e.g., Fiction, Non-Fiction, Self-Help, Romance, Sci-Fi, Comics, etc.)
3. Each category should have:
   - Name
   - Slug (auto-generated)
   - Description (optional)

### Step 3: Add Products (Books)

1. Click on **Products**
2. Add books with details:
   - Title
   - Author
   - Category
   - Price
   - Stock quantity
   - ISBN
   - Description
   - Images (will be uploaded to Cloudinary automatically)

### Step 4: Configure Offers/Coupons (Optional)

1. Navigate to **Offers** or **Coupons** section
2. Create discount offers for products or categories
3. Set validity dates and discount percentages

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Database Connection Error

**Error**: `FATAL: password authentication failed for user "booknest_user"`

**Solution**:
- Verify database credentials in `.env`
- Ensure PostgreSQL is running: `pg_isready` (Linux/macOS) or check Services on Windows
- Reset database password if needed

#### 2. Cloudinary Upload Fails

**Error**: `AuthorizationRequired: Invalid cloud_name`

**Solution**:
- Verify Cloudinary credentials in `.env`
- Ensure no extra spaces in credentials
- Restart the Django server after updating `.env`

#### 3. Email Not Sending

**Error**: `SMTPAuthenticationError`

**Solution**:
- Verify Gmail App Password (16 characters, no spaces)
- Enable 2-Step Verification in Google Account
- Check EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in `.env`

#### 4. Google OAuth Not Working

**Error**: `redirect_uri_mismatch`

**Solution**:
- Add exact redirect URIs in Google Cloud Console:
  - `http://localhost:8000/auth/complete/google-oauth2/`
  - `http://127.0.0.1:8000/auth/complete/google-oauth2/`
- Clear browser cookies and try again

#### 5. Razorpay Payment Fails

**Error**: Payment modal doesn't open

**Solution**:
- Verify Razorpay keys in `.env`
- Check browser console for JavaScript errors
- Ensure using Test Mode keys for development
- Clear browser cache

#### 6. Static Files Not Loading

**Error**: CSS/JavaScript not applied

**Solution**:
```bash
python manage.py collectstatic --noinput
```
- Ensure `DEBUG=True` in `.env` for development
- Check Django settings for `STATIC_URL` and `STATIC_ROOT`

#### 7. Migration Errors

**Error**: `Migration conflicts detected`

**Solution**:
```bash
# Reset migrations (⚠️ This will delete all data!)
python manage.py migrate --fake-initial
# Or reset specific app
python manage.py migrate admin_side zero
python manage.py migrate admin_side
```

#### 8. Port Already in Use

**Error**: `Error: That port is already in use.`

**Solution**:
```bash
# Run on different port
python manage.py runserver 8080

# Or find and kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9
```

---

## Production Deployment Notes

When deploying to production, ensure you:

1. **Set DEBUG to False**
   ```env
   DEBUG=False
   ```

2. **Use Strong Secret Key**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Configure Allowed Hosts**
   Update `booknest/settings.py`:
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Use Production Database**
   - Cloud PostgreSQL (Railway, Render, AWS RDS, etc.)
   - Use `DATABASE_URL` environment variable

5. **Switch to Live Payment Keys**
   - Replace Razorpay test keys with live keys
   - Test thoroughly before going live

6. **Setup SSL Certificate**
   - Use Let's Encrypt for free SSL
   - Configure HTTPS

7. **Use Web Server**
   - Gunicorn (included in requirements.txt)
   - Nginx as reverse proxy

8. **Enable CSRF Protection**
   ```python
   CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com']
   ```

---

## Support

If you encounter any issues not covered in this guide:

1. Check the Django error logs in the terminal
2. Review the browser console for JavaScript errors
3. Ensure all third-party services are properly configured
4. Verify all environment variables are correctly set

For additional assistance, please contact the developer.

---

## Next Steps

After successful installation:

1. ✅ Customize the site branding (logo, colors, etc.)
2. ✅ Add your book inventory through the admin panel
3. ✅ Test the complete user flow (registration, browsing, cart, checkout)
4. ✅ Test payment integration with test cards
5. ✅ Configure email templates for better branding
6. ✅ Setup backup strategy for database
7. ✅ Plan your production deployment

---

**Congratulations! Your BookNest e-commerce platform is now ready to use! 🎉**
