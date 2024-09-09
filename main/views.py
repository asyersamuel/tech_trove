from django.shortcuts import render

def show_main(request):
    products = [
        {
            "name": "Samsung S9+",
            "price": 9599000,
            "description": "Produk Bagus ini"
        },
        {
            "name": "Samsung S8",
            "price": 8999000,
            "description": "Produk Murah ini"
        },
        {
            "name": "Samsung S7",
            "price": 7999000,
            "description": "Produk Murah ini"
        }
    ]

    context = {
        "products": products
    }

    return render(request, "main.html", context)