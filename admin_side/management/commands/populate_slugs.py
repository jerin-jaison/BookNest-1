from django.core.management.base import BaseCommand
from django.utils.text import slugify
from admin_side.models import Product

class Command(BaseCommand):
    help = 'Populate slugs for existing products'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        count = 0

        for product in products:
            if not product.slug:
                base_slug = slugify(product.title)
                slug = base_slug
                num = 1

                # Handle duplicate slugs
                while Product.objects.filter(slug=slug).exclude(id=product.id).exists():
                    slug = f"{base_slug}-{num}"
                    num += 1

                product.slug = slug
                product.save()
                count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated {count} slugs')
        )
