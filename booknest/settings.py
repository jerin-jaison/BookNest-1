"""
CORRECTED Django settings for booknest project.
Issues found and fixed in your settings.py
"""

from pathlib import Path
from django.contrib.messages import constants as messages
import os 
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', '.onrender.com']

# ============================================
# INSTALLED_APPS - ORDER IS CORRECT ✅
# ============================================
INSTALLED_APPS = [ 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Cloudinary (MUST be in this order) ✅
    'cloudinary_storage',
    'cloudinary',
    
    # Your apps
    'user_authentication',
    'social_django',
    'admin_side',
    'user_profile',
    'user_wallet',
    'cart_section.apps.CartSectionConfig',
    'online_payment',
    'booknest.apps.BooknestConfig',
]

# Message settings
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom middleware
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'user_authentication.middleware.BlockedUserMiddleware',
    'user_authentication.middleware.PreventBackButtonMiddleware',
]

ROOT_URLCONF = 'booknest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Social auth context
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'booknest.wsgi.application'

# ============================================
# DATABASE ✅
# ============================================
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# ============================================
# PASSWORD VALIDATION ✅
# ============================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================
# INTERNATIONALIZATION ✅
# ============================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ============================================
# ⚠️ CRITICAL FIX 1: Cloudinary Configuration
# ============================================

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

# File storage configuration ✅
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# ============================================
# 🔍 ADD THIS FOR DEBUGGING (TEMPORARY)
# ============================================
# Add these lines TEMPORARILY to see if env vars are loading
print("=" * 50)
print("CLOUDINARY CONFIGURATION CHECK:")
print(f"CLOUD_NAME: {os.getenv('CLOUDINARY_CLOUD_NAME')}")
print(f"API_KEY: {os.getenv('CLOUDINARY_API_KEY')}")
print(f"API_SECRET: {'***' + os.getenv('CLOUDINARY_API_SECRET', '')[-4:] if os.getenv('CLOUDINARY_API_SECRET') else 'NOT SET'}")
print(f"DEFAULT_FILE_STORAGE: {DEFAULT_FILE_STORAGE}")
print("=" * 50)

# ============================================
# STATIC FILES ✅
# ============================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# ============================================
# ✅ CORRECT: Media settings commented out
# ============================================
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ============================================
# DEFAULT AUTO FIELD ✅
# ============================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================
# EMAIL CONFIGURATION ✅
# ============================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# ============================================
# GOOGLE OAUTH ✅
# ============================================
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',  
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

LOGIN_URL = 'login_page'
LOGIN_REDIRECT_URL = 'home_page'
LOGOUT_URL = 'signout_view'
LOGOUT_REDIRECT_URL = 'login_page'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

# ============================================
# RAZORPAY ✅
# ============================================
RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET')

# ============================================
# AWS S3 (CORRECTLY COMMENTED OUT) ✅
# ============================================
# You're using Cloudinary, not S3 - good!