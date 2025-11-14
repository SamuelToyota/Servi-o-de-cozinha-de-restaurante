from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dish, Cook, DishType, Ingredient
from .forms import DishForm, CookForm, DishTypeForm, IngredientForm


# LISTAGENS
class DishListView(ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(DetailView):
    model = Dish


class CookListView(ListView):
    model = Cook


class CookDetailView(DetailView):
    model = Cook


class DishTypeListView(ListView):
    model = DishType


class IngredientListView(ListView):
    model = Ingredient


# CRUDS
class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("menu:dish_list")


class CookCreateView(CreateView):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("menu:cook_list")


class DishTypeCreateView(CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("menu:dish_type_list")


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("menu:ingredient_list")
