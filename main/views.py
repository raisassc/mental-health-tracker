from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165755',
        'name': 'Raisa Sakila',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
