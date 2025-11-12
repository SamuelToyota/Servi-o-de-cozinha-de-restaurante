from django.contrib import admin
from .models import Cook, DishType, Dish, Ingredient


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "experience_years")


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price")
    list_filter = ("dish_type",)
    search_fields = ("name",)
    filter_horizontal = ("cooks",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
