# Generated by Django 5.0.7 on 2024-08-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page_deli', '0004_alter_hotcase_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotcase',
            name='plu',
            field=models.IntegerField(default=0),
        ),
    ]
