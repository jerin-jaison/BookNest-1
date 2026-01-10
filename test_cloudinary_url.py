import os
import django
from django.conf import settings
import sys

# Add the project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booknest.settings")
django.setup()

def test_storage():
    try:
        from cloudinary_storage.storage import MediaCloudinaryStorage
        storage = MediaCloudinaryStorage()
        print(f"Storage class: {storage}")
        
        test_name = "test_image.jpg"
        url = storage.url(test_name)
        print(f"Generated URL for '{test_name}': {url}")
        
        from admin_side.models import Product
        field = Product._meta.get_field('cover_image')
        print(f"Product.cover_image storage: {field.storage}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_storage()
