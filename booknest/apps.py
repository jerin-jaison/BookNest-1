from django.apps import AppConfig
import os
import sys


class BooknestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "booknest"

    def ready(self):
        # Avoid database access during management commands like makemigrations/migrate
        # which run during app initialization. Only run superuser creation during
        # normal runtime (e.g., runserver, uwsgi, gunicorn).
        if any(cmd in sys.argv for cmd in [
            'makemigrations', 'migrate', 'collectstatic', 'shell', 'test'
        ]):
            return

        from django.contrib.auth import get_user_model

        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            return

        User = get_user_model()

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
