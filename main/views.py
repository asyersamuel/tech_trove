from django.shortcuts import render

def show_main(request):
    context = {
        "store_name" : "Tech Trove",
        "name" : "Asyer Samuel Marpaung",
        "class" : "PBP A"
    }

    return render(request, "main.html", context)