from django import forms
from .models import Breakfast, Bakery, Firstmeal, Mainhot, Snacks



class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = ('name', 'description', 'image', 'price')      

class BakeryForm(forms.ModelForm):
    class Meta:
        model = Bakery
        fields = ('name', 'description', 'image', 'price')  
        
class FirstmealForm(forms.ModelForm):
    class Meta:
        model = Firstmeal
        fields = ('name', 'description', 'image', 'price')  

class MainhotForm(forms.ModelForm):
    class Meta:
        model = Mainhot
        fields = ('name', 'description', 'image', 'price')  

class SnacksForm(forms.ModelForm):
    class Meta:
        model = Snacks
        fields = ('name', 'description', 'image', 'price')     