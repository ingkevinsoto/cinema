# Generated by Django 4.2.4 on 2023-08-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
