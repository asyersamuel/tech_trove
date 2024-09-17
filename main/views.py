from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()

    context = {
        "store_name" : "Tech Trove",
        "name" : "Asyer Samuel Marpaung",
        "class" : "PBP A",
        "products" : products,
    }

    return render(request, "main.html", context)

def product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")