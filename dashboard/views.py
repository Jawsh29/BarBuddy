from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.db.models import Sum


# Views for different objects across site. Also establishes user to login before gaining full access to site data


@login_required
def index(request):
    orders = Order.objects.all()
    orders_count = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum'] or 0
    products = Product.objects.all()
    products_count = products.count()
    workers = User.objects.all()
    workers_count = workers.count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'products': products,
        'products_count': products_count,
        'orders': orders,
        'orders_count': orders_count,
        'workers_count': workers_count,
        'workers': workers,
    }
    return render(request, 'dashboard/index.html', context)


# Staff Views ------------------------------------------------------------------------------------------------------
@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum'] or 0
    products_count = Product.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/staff.html', context)


# Product Views ----------------------------------------------------------------------------------------------------
@login_required
def product(request):
    items = Product.objects.all()
    products_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum'] or 0
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'products_count': products_count,
        'workers_count': workers_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/product.html', context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')


@login_required
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)


# Order Views --------------------------------------------------------------------------------------------------------
@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum'] or 0
    workers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    context = {
        'orders': orders,
        'orders_count': orders_count,
        'workers_count': workers_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/order.html', context)



