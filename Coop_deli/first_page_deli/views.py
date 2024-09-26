from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import *

# Create your views here.

def index(request):
    return render(request, "first_page_deli/index.html")
    
def shelf_detail_view(request, shelf_name):
    # Fetch all items from the HotCase model

    model_map = {
        "HotCase": HotCase,
        "SandwichEndI": SandwichEndI,
        "SandwichEndII": SandwichEndII,
        "ServiceCaseMeats": ServiceCaseMeats,
        "ServiceCaseSalads": ServiceCaseSalads,
        "PackedMeatI": PackedMeatI,
        "PackedMeatII": PackedMeatII,
        "SaladsEnd": SaladsEnd,
        "PizzaAndSalads": PizzaAndSalads,
        "SoupsAndMeals": SoupsAndMeals,
        "EntertainmentEnd": EntertainmentEnd,
        "Pasta": Pasta,
        "Dips": Dips,
        "CheeseBoard": CheeseBoard,
        "Pizzas": Pizza,
    }

    model = model_map.get(shelf_name)
    if not model:
        return render(request, 'first_page_deli/404.html')

    items = model.objects.all().order_by('item_name')

    # Render the template with the items
    return render(request, 'first_page_deli/shelf_detail.html', {
        'items': items,
        'shelf_name': shelf_name
    })

def on_sale_view(request, shelf_name):
    model_map = {
        "OnSaleMeats": OnSaleMeats,
        "OnSaleSalads": OnSaleSalads,
    }

    model = model_map.get(shelf_name)
    if not model:
        return render(request, 'first_page_deli/404.html')

    items = model.objects.all().first()  # Get the first (and probably only) instance
    if shelf_name == "OnSaleMeats":
        items = items.on_sale_meats.all().order_by('item_name')
    elif shelf_name == "OnSaleSalads":
        items = items.on_sale_salads.all().order_by('item_name')

    return render(request, 'first_page_deli/OnSale.html', {
        'items': items,
        'shelf_name': shelf_name
    })

def place_order(request, product_id):
    product = get_object_or_404(Pizza, id = product_id)
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        total_price = product.price * quantity
        order = OrderPizza.objects.create(product_ordered = product, quantity_ordered=quantity, total_price=total_price)
        return redirect('payment_placeholder', order_id = order.id)
    return render(request, 'place_order.html', {
        'product': product
    })

# views.py

def payment_placeholder(request, order_id):
    order = get_object_or_404(OrderPizza, id=order_id)
    
    # For now, just confirm the order without processing payment
    context = {
        'order': order,
        'message': 'Payment functionality will be added soon. Your order has been placed successfully!',
    }
    return render(request, 'first_page_deli/payment_placeholder.html', context)

# views.py

# views.py

def build_your_own_pizza(request):
    crusts = PizzaCrust.objects.all()
    sizes = PizzaSize.objects.all()
    sauces = PizzaSauce.objects.all()
    meats = PizzaMeat.objects.all()
    cheeses = PizzaCheese.objects.all()
    toppings = PizzaToppings.objects.all()

    context = {
        'crusts': crusts,
        'sizes': sizes,
        'sauces': sauces,
        'meats': meats,
        'cheeses': cheeses,
        'toppings': toppings,
    }

    if request.method == "POST":
        crust = get_object_or_404(PizzaCrust, id=request.POST.get('crust'))
        size = get_object_or_404(PizzaSize, id=request.POST.get('size'))
        sauce = get_object_or_404(PizzaSauce, id=request.POST.get('sauce'))
        meats = request.POST.getlist('meats')
        cheeses = request.POST.getlist('cheese')
        toppings = request.POST.getlist('toppings')
        quantity = int(request.POST.get('quantity', 1))

        # Create a new Pizza instance (or fetch an existing one)
        pizza = Pizza.objects.create(
            crust=crust,
            size=size,
            sauce=sauce,
            price=10
        )
        pizza.meat.set(meats)
        pizza.cheese.set(cheeses)
        pizza.toppings.set(toppings)
        
        # Create a new order
        total_price = pizza.price * quantity
        order = OrderPizza.objects.create(
            product_ordered=pizza,
            quantity_ordered=quantity,
            total_price=total_price
        )
        return redirect('payment_placeholder', order_id=order.id)

    return render(request, 'first_page_deli/BYOPizza.html', context)
