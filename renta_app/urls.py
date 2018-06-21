from django.urls import path
from django.views.generic import TemplateView
from .views import CityListView, RentView, ItemDetailView, change_city


app_name = 'renta_app'
urlpatterns = [
    # path('', TemplateView.as_view(template_name='renta_app/main.html')),
    path('', RentView.as_view(), name='rent-list'),
    path('city/', CityListView.as_view(), name='city'),
    path('delivery/', TemplateView.as_view(template_name='renta_app/delivery.html'), name='delivery'),
    path('contects/', TemplateView.as_view(template_name='renta_app/contacts.html'), name='contacts'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('city/<int:pk>/', change_city, name='change-city'),

]
