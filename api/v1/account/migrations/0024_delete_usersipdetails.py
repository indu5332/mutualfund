# Generated by Django 4.2.7 on 2023-12-16 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mutual_sip', '0013_remove_sip_users_sip_users'),
        ('account', '0023_userpurchaseorderdetails_current_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSipDetails',
        ),
    ]
