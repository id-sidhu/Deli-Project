# Generated by Django 5.0.7 on 2024-08-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page_deli', '0011_alter_pizza_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entertainmentend',
            options={'verbose_name': 'Entertainment End'},
        ),
        migrations.AlterField(
            model_name='entertainmentend',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
