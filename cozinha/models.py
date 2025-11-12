from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    photo = models.ImageField(upload_to="cooks/", blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Cozinheiro"
        verbose_name_plural = "Cozinheiros"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo de prato"
        verbose_name_plural = "Tipos de prato"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    class Meta:
        verbose_name = "Prato"
        verbose_name_plural = "Pratos"

    def __str__(self):
        return self.name
