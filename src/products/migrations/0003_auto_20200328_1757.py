# Generated by Django 3.0.4 on 2020-03-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200328_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=False),
        ),
    ]
