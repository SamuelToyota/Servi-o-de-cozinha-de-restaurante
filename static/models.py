from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("menu:cook_detail", args=[self.id])


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("menu:dish_detail", args=[self.id])


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    dishes = models.ManyToManyField(Dish, related_name="ingredients", blank=True)

    def __str__(self):
        return self.name
