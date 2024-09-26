from django.db import models
from django import forms

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class HotCase(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    plu = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Hot Case Item"  # Custom name for the model
        verbose_name_plural = "Hot Case Items"

    def __str__(self):
        return self.item_name

class SandwichEndI(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sandwich End - I'
        verbose_name_plural = 'Sandwich End - I'

    def __str__(self):
        return self.item_name

class SandwichEndII(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sandwich End - II'
        verbose_name_plural = 'Sandwich End - II'

    def __str__(self):
        return self.item_name

class ServiceCaseMeats(models.Model):
    item_name = models.CharField(max_length=64, unique=True)
    category = models.ManyToManyField(Category, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='service_case_meats',
                              null = True, blank = True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank = True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    plu = models.IntegerField(blank=True, null = True)

    class Meta:
        verbose_name = "Service Case Meat"
        verbose_name_plural = "Service Case Meats"

    def __str__(self):
        return self.item_name

class ServiceCaseSalads(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class PackedMeatI(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class PackedMeatII(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class SaladsEnd(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class PizzaAndSalads(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class SoupsAndMeals(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class EntertainmentEnd(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
    
    class Meta:
        verbose_name = "Entertainment End"
        verbose_name_plural = "Entertainment End"

class Pasta(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class Dips(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

class CheeseBoard(models.Model):
    item_name = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
    
class PizzaSize(models.Model):
    pizza_size = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.pizza_size) + ' "'

class PizzaMeat(models.Model):
    meat_name = models.CharField(max_length=128)

    def __str__(self):
        return self.meat_name

class PizzaToppings(models.Model):
    topping_name = models.CharField(max_length=128)

    def __str__(self):
        return self.topping_name

class PizzaSauce(models.Model):
    sauce_name = models.CharField(max_length=128)

    def __str__(self):
        return self.sauce_name

class PizzaCheese(models.Model):
    cheese_name = models.CharField(max_length=128)

    def __str__(self):
        return self.cheese_name

class PizzaCrust(models.Model):
    crust_type = models.CharField(max_length=128)

    def __str__(self):
        return self.crust_type

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=128)
    category = models.ManyToManyField(Category, blank=True)
    crust = models.ForeignKey(PizzaCrust, on_delete=models.CASCADE)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, blank=False, default=13)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)
    meat = models.ManyToManyField(PizzaMeat, blank=True)
    cheese = models.ManyToManyField(PizzaCheese, blank=False)
    toppings = models.ManyToManyField(PizzaToppings, blank=False)

    def __str__(self):
        return self.pizza_name

class BYOPizza(models.Model):
    crust = forms.ModelChoiceField(queryset=PizzaCrust.objects.all(), label = 'Choose Crust')
    size = forms.ModelChoiceField(queryset=PizzaSize.objects.all(), label="Choose Size")
    sauce = forms.ModelChoiceField(queryset=PizzaSauce.objects.all(), label="Choose Sauce")
    meats = forms.ModelMultipleChoiceField(queryset=PizzaMeat.objects.all(), widget=forms.CheckboxSelectMultiple, required=False, label="Select Meats")
    cheese = forms.ModelMultipleChoiceField(queryset=PizzaCheese.objects.all(), widget=forms.CheckboxSelectMultiple, label="Select Cheese")
    toppings = forms.ModelMultipleChoiceField(queryset=PizzaToppings.objects.all(), widget=forms.CheckboxSelectMultiple, label="Select Toppings")





class OnSaleMeats(models.Model):
    on_sale_meats = models.ManyToManyField(ServiceCaseMeats, blank=True)

    def __str__(self):
        return "On Sale Meats"

class OnSaleSalads(models.Model):
    on_sale_salads = models.ManyToManyField(ServiceCaseSalads, blank=True)

    def __str__(self):
        return "On Sale Salads"
    



    #  Online Ordering

class OrderPizza(models.Model):
    product_ordered = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    quantity_ordered = models.PositiveIntegerField(default = 1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.product_ordered.name}"