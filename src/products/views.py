from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductFrom, RawProductForm
from django.http import Http404
# Create your views here.

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'obj': queryset
    }
    return render(request, "products/product_list_all.html", context)

def product_delete_view(request, id):
    obj = Product.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        "obj": obj
    }
    return render(request, "products/product_delete.html", context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "obj": obj
    }
    print(obj.title)
    return render(request, "products/product_details.html", context)

def render_initial_data(request):
    initial_data = {
        "title": "MY Intitial Title"
    }
    obj = Product.objects.get(id=1)
    form = ProductFrom(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # print(form.cleaned_data )
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context=context)


def product_detail_views(request):
    obj = Product.objects.get(id=1)
    context = {
        'obj':obj
    }
    return render(request, "product2/details.html", context=context)

def product_create_views(request):
    form = ProductFrom(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductFrom() #rerender

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context=context)

# def product_create_views(request):
#     print(request.GET)
#     print(request.POST)
#     if request.method=="POST":
#         my_new_title= request.POST.get('title')
#         print(my_new_title)

#     context = {}
#     return render(request, "products/product_create.html", context=context)

# def product_create_views(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data) #passing as kwargs
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context=context)
