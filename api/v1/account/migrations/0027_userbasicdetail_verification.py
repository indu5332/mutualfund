# Generated by Django 4.2.7 on 2023-12-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_userpurchaseorderdetails_installment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbasicdetail',
            name='verification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
