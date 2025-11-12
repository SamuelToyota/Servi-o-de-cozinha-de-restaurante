from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.DishListView.as_view(), name="dish_list"),
    path("dish/<int:pk>/", views.DishDetailView.as_view(), name="dish_detail"),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish_create"),

    path("cooks/", views.CookListView.as_view(), name="cook_list"),
    path("cook/<int:pk>/", views.CookDetailView.as_view(), name="cook_detail"),
    path("cooks/create/", views.CookCreateView.as_view(), name="cook_create"),

    path("dish-types/", views.DishTypeListView.as_view(), name="dish_type_list"),
    path("dish-types/create/", views.DishTypeCreateView.as_view(), name="dish_type_create"),

    path("ingredients/", views.IngredientListView.as_view(), name="ingredient_list"),
    path("ingredients/create/", views.IngredientCreateView.as_view(), name="ingredient_create"),
]
