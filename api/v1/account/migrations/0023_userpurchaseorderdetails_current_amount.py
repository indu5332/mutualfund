# Generated by Django 4.2.7 on 2023-12-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_alter_userpurchaseorderdetails_portfolio_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpurchaseorderdetails',
            name='current_amount',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
