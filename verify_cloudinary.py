import os
import django
from django.conf import settings
import sys

# Add the project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booknest.settings")
django.setup()

def check_config():
    print(f"DEFAULT_FILE_STORAGE: {getattr(settings, 'DEFAULT_FILE_STORAGE', 'Not Set')}")
    print(f"MEDIA_URL: '{getattr(settings, 'MEDIA_URL', 'Not Set')}'")
    
    env_vars = ['CLOUDINARY_CLOUD_NAME', 'CLOUDINARY_API_KEY', 'CLOUDINARY_API_SECRET']
    for var in env_vars:
        value = os.environ.get(var)
        print(f"Env {var}: {'Set' if value else 'MISSING'}")

    try:
        from admin_side.models import Product
        product = Product.objects.last() # Get last added might be more relevant
        if product and product.cover_image:
            print(f"Sample Product Image Name: {product.cover_image.name}")
            try:
                print(f"Sample Product Image URL: {product.cover_image.url}")
            except Exception as e:
                print(f"Error getting URL: {e}")
        else:
            print("No products with images found.")
    except Exception as e:
        print(f"Error accessing models: {e}")

if __name__ == "__main__":
    check_config()
