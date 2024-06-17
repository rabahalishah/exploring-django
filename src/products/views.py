from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm

# Create your views here.


def product_update_view(request):
    context = {}
    return render(request, "product/product_update.html", context)
# Getting all instances of the objects from the database


def product_list_view(request):
    objects_list = Product.objects.all()
    context = {
        "object_list": objects_list
    }
    return render(request, "product/product_list.html", context)


# Dynamic urls in django


# <-- this my_id argument is coming from dynamic url
def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "product/product_detail.html", context)

# Deleting the product


def dynamic_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        # confirming post request then deleting the object
        obj.delete()
        return redirect('../')

    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)

# Django pure forms


# def product_create_view(request):
#     my_form = RawProductFrom()
#     if request.method == 'POST':
#         my_form = RawProductFrom(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)

#         # Product.objects.create(**my_form.cleaned_data)

#     context = {"form": my_form}

#     return render(request, "product/product_create.html", context)


# RAW HTML data
# def product_create_view(request):
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)

#     context = {}

#     return render(request, "product/product_create.html", context)


# storing data into models using model forms

def product_create_view(request):
    initial_data = {
        'title': "This is my initial title"
    }
    # obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form,

    }

    return render(request, "product/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    context = {
        'objects': obj

    }

    return render(request, "product/detail.html", context)
