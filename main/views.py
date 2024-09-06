from django.shortcuts import render

def show_main(request):
    context = {
        "name": "Samsung S9+",
        "price": 9599000,
        "description": "Produk Bagus ini"
    }

    return render(request, "main.html", context)