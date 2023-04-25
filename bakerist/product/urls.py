from django.urls import path
from . import views


from django.urls import path
from .views import add_breakfast, add_bakery, add_firstmeal, add_mainhot, add_snacks, add_product, product

urlpatterns = [
    path('add_breakfast/', add_breakfast, name='add_breakfast'),

    path('add_bakery/', add_bakery, name='add_bakery'),

    path('add_firstmeal/', add_firstmeal, name='add_firstmeal'),

    path('add_mainhot/', add_mainhot, name='add_mainhot'),

    path('add_snacks/', add_snacks, name='add_snacks'),        

    path('add_product/', add_product, name='add_product'),     

    path('product/', product, name='product'),        
]