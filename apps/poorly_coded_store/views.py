from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkoutdata(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(Product.objects.get(id=request.POST["product_id"]).price)
    total_charge = quantity_from_form * price_from_form
    if 'total_quantity' in request.session:
        request.session['total_quantity'] += quantity_from_form
    else:
        request.session['total_quantity'] = price_from_form
    if 'total_price' in request.session:
        request.session['total_price'] += price_from_form
    else:
        request.session['total_price'] = price_from_form

    print("Charging credit card...")
    newOrder = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect(f"/checkout/{newOrder.id}")

def checkout(request, id):
    context = {
        "order": Order.objects.get(id=id)
    }
    return render(request, "store/checkout.html", context)

def reset(request):
    request.session['total_price'] = 0
    request.session['total_quantity'] = 0
    return redirect("/")
