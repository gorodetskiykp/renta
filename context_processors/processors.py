from django.db.models import Sum
from renta_app.models import Category


def menu(request):
    if request.session.get('city_name', ''):
        categories_query = Category.objects.filter(item__city__city=request.session.get('city_name', '')).annotate(Sum('item__quantity'))
    else:
        categories_query = Category.objects.all().annotate(Sum('item__quantity'))
    context = {
        'categories': categories_query,
    }
    return context


def city(request):
    context = {
        'city_name': request.session.get('city_name', ''),
    }
    return context
