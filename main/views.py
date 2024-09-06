from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165925',
        'name': 'Asyer Samuel Marpaung',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)