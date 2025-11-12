from django import forms
from .models import Dish, DishType, Cook, Ingredient


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "dish_type", "cooks", "price"]


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["first_name", "last_name", "experience_years"]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "dishes"]
