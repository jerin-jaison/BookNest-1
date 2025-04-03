"""
URL configuration for booknest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from user_authentication.views import custom_404_view
from django.views.static import serve
import os
import re

handler404 = custom_404_view

# Custom view for serving static and media files in case-insensitive way
def case_insensitive_serve(request, path, document_root=None):
    # Try the path as is first
    if os.path.exists(os.path.join(document_root, path)):
        return serve(request, path, document_root)
    
    # If not found, search case-insensitively
    path_parts = path.split('/')
    current_dir = document_root
    new_path = []
    
    for part in path_parts:
        if os.path.isdir(current_dir):
            # Case-insensitive match for directories/files
            found = False
            for item in os.listdir(current_dir):
                if item.lower() == part.lower():
                    new_path.append(item)
                    current_dir = os.path.join(current_dir, item)
                    found = True
                    break
            if not found:
                # If no match found, use original part
                new_path.append(part)
                current_dir = os.path.join(current_dir, part)
        else:
            new_path.append(part)
    
    return serve(request, '/'.join(new_path), document_root)

urlpatterns = [
    path('', include('user_authentication.urls')),
    path('admin_side/', include('admin_side.urls')),
    path('user_profile/', include('user_profile.urls', namespace='user_profile')),
    path('cart_section/', include('cart_section.urls')),
    path('wallet/', include('user_wallet.urls')),
    path('payment/', include('online_payment.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

# Add media files and static files serving
urlpatterns += [
    path('media/<path:path>', case_insensitive_serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', case_insensitive_serve, {'document_root': settings.STATIC_ROOT or os.path.join(settings.BASE_DIR, 'static')}),
]
