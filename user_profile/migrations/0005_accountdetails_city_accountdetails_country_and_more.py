# Generated by Django 5.1.3 on 2025-03-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_accountdetails_pending_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdetails',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='country',
            field=models.CharField(default='India', max_length=100),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='house_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='landmark',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='accountdetails',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
