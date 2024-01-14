# Generated by Django 4.2.7 on 2023-12-01 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_usersipdetails_alter_user_is_blocked'),
        ('mutual_sip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersipdetails',
            name='sip_list',
            field=models.ManyToManyField(to='mutual_sip.sip'),
        ),
        migrations.AddField(
            model_name='usersipdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]