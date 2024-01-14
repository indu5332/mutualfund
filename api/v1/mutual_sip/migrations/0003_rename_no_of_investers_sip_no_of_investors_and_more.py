# Generated by Django 4.2.7 on 2023-12-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_usersipdetails_sips'),
        ('mutual_sip', '0002_alter_sip_min_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sip',
            old_name='no_of_investers',
            new_name='no_of_investors',
        ),
        migrations.RemoveField(
            model_name='sip',
            name='user',
        ),
        migrations.AddField(
            model_name='sip',
            name='users',
            field=models.ManyToManyField(related_name='sip_list', to='account.usersipdetails'),
        ),
    ]
