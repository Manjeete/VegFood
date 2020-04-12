from django.shortcuts import render, HttpResponse


def shop(request):
    return render(request, 'shop/shop.html')
