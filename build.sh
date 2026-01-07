#!/usr/bin/env bash
# set -o errexit

# pip install -r requirements.txt
# python manage.py makemigrations
# python manage.py migrate --noinput
# python manage.py collectstatic --noinput
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py populate_slugs || echo "Slug population skipped"
python manage.py collectstatic --noinput