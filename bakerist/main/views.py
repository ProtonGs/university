from django.shortcuts import render
from product.models import Breakfast, Bakery, Firstmeal, Mainhot, Snacks
# Create your views here.
def index(request):
    snacks = Snacks.objects.all()
    mainhot = Mainhot.objects.all()
    firstmeal = Firstmeal.objects.all()
    bakery = Bakery.objects.all()
    breakfast = Breakfast.objects.all()
    return render(request, 'main/index.html', {'title': 'PRISMAIL', 'breakfast': breakfast, 'bakery': bakery, 'firstmeal': firstmeal, 'mainhot': mainhot, 'snacks': snacks})