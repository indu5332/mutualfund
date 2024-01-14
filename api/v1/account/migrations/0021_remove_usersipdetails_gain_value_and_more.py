# Generated by Django 4.2.7 on 2023-12-16 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mutual_sip', '0013_remove_sip_users_sip_users'),
        ('account', '0020_remove_usersipdetails_sips_usersipdetails_sips'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersipdetails',
            name='gain_value',
        ),
        migrations.RemoveField(
            model_name='usersipdetails',
            name='invested_amount',
        ),
        migrations.RemoveField(
            model_name='usersipdetails',
            name='member_status',
        ),
        migrations.RemoveField(
            model_name='usersipdetails',
            name='portfolio_no',
        ),
        migrations.RemoveField(
            model_name='usersipdetails',
            name='sips',
        ),
        migrations.RemoveField(
            model_name='usersipdetails',
            name='user',
        ),
        migrations.CreateModel(
            name='UserPurchaseOrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invested_amount', models.FloatField(default=0.0)),
                ('member_status', models.CharField(default='active', max_length=100)),
                ('portfolio_no', models.IntegerField(blank=True)),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('investment_type', models.CharField(max_length=100)),
                ('sips', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sip_details', to='mutual_sip.sip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usersipdetails',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='account.userpurchaseorderdetails'),
        ),
    ]
