from django.shortcuts import render, HttpResponse
from .models import ShopItems
from django.views import generic


class ShopListView(generic.ListView):
    template_name = 'shop/shop.html'
    context_object_name = 'items'

    def get_queryset(self):
        return ShopItems.objects.all()

class ShopDetailView(generic.DetailView):
    model = ShopItems
    template_name = 'shop/single-item.html'


# def shop(request):
#     items = ShopItems.objects.all()
#     context = {
#         "items":items
#     }

#     return render(request, 'shop/shop.html', context)
