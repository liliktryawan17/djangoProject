from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'header': 'halaman utama'
    }
    return render(request, 'index.html', context)
