from django.contrib import admin
from .models import Cook, DishType, Ingredient, Dish


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "years_of_experience")
    list_filter = ("years_of_experience",)
    search_fields = ("username", "first_name", "last_name")


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity_in_stock")
    list_filter = ("quantity_in_stock",)
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "cook")
    list_filter = ("dish_type",)
    search_fields = ("name",)
    autocomplete_fields = ("cook", "ingredients")
