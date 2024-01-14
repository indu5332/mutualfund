# Generated by Django 4.2.7 on 2023-12-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mutual_sip', '0012_remove_sip_users_sip_users'),
        ('account', '0019_remove_usersipdetails_sips_usersipdetails_sips'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersipdetails',
            name='sips',
        ),
        migrations.AddField(
            model_name='usersipdetails',
            name='sips',
            field=models.ManyToManyField(blank=True, related_name='sip_details', to='mutual_sip.sip'),
        ),
    ]
