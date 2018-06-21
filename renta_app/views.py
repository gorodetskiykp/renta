from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Category, City, Item


class RentView(ListView):
    template_name = 'renta_app/rent_list.html'

    def get_queryset(self):
        try:
            return Item.objects.filter(city__city=self.request.session['city_name'])
        except KeyError:
            return Item.objects.all()


class ItemDetailView(DetailView):
    template_name = 'renta_app/item_detail.html'
    model = Item


class CityListView(ListView):
    template_name = 'renta_app/city_list.html'

    def get_queryset(self):
        return City.objects.exclude(item__isnull=True)


def change_city(request, pk):
    request.session['city_name'] = City.objects.get(id=pk).city
    return HttpResponseRedirect('/')
