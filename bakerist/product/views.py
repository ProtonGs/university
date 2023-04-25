from django.shortcuts import render, redirect

# Create your views here.


from .forms import BreakfastForm, BakeryForm, MainhotForm, FirstmealForm, SnacksForm



def add_breakfast(request):
    if request.method == 'POST':
        form = BreakfastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BreakfastForm()
    return render(request, 'product/add_breakfast.html', {'form': form})


def add_bakery(request):
    if request.method == 'POST':
        form = BakeryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BakeryForm()
    return render(request, 'product/add_bakery.html', {'form': form})


def add_firstmeal(request):
    if request.method == 'POST':
        form = FirstmealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FirstmealForm()
    return render(request, 'product/add_firstmeal.html', {'form': form})


def add_mainhot(request):
    if request.method == 'POST':
        form = MainhotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MainhotForm()
    return render(request, 'product/add_mainhot.html', {'form': form})


def add_snacks(request):
    if request.method == 'POST':
        form = SnacksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SnacksForm()
    return render(request, 'product/add_snacks.html', {'form': form})


def add_product(request):
    return render(request, 'product/add_product.html')


def product(request):
    return render(request, 'product/product.html')