# Generated by Django 5.0.7 on 2024-08-14 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_page_deli', '0009_pizzameat_pizza_meat'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_size', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='first_page_deli.pizzasize'),
        ),
    ]
