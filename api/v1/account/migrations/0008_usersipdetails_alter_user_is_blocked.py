# Generated by Django 4.2.7 on 2023-12-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_is_blocked'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSipDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invested_amount', models.FloatField(default=0.0)),
                ('member_status', models.CharField(default='active', max_length=100)),
                ('gain_value', models.FloatField(default=0.0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]