from django.db import migrations
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    Category = apps.get_model('admin_side', 'Category')
    Product = apps.get_model('admin_side', 'Product')

    for category in Category.objects.all():
        if not category.slug:
            category.slug = slugify(category.name)
            category.save()

    for product in Product.objects.all():
        if not product.slug:
            product.slug = slugify(product.title)
            product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0017_product_isbn_alter_category_slug'),
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
