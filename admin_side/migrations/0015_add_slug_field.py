from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Product = apps.get_model('admin_side', 'Product')
    for product in Product.objects.all():
        if not product.slug:
            base = slugify(product.title)[:180]
            slug = base
            num = 1
            while Product.objects.filter(slug=slug).exclude(pk=product.pk).exists():
                slug = f"{base}-{num}"
                num += 1
            product.slug = slug
            product.save(update_fields=['slug'])


def reverse_populate(apps, schema_editor):
    Product = apps.get_model('admin_side', 'Product')
    for product in Product.objects.all():
        product.slug = None
        product.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0014_remove_product_category_remove_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, blank=True, null=True),
        ),
        migrations.RunPython(populate_slugs, reverse_populate),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]