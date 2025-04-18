# Generated by Django 5.1.3 on 2025-03-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_section', '0003_order_notes_order_payment_id_order_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled'), ('RETURNED', 'Returned'), ('RETURN_REQUESTED', 'Return Requested'), ('RETURN_REJECTED', 'Return Rejected')], default='PENDING', max_length=20),
        ),
    ]
