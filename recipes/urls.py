from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipes_list, name="recipes_list"),
    path("my-recipes/", views.my_recipes, name="my_recipes"),
    path("add-recipe/", views.add_recipe, name="add_recipe"),
    path("signup/", views.signup, name="signup"),
    path("category/<slug:category_slug>/", views.recipes_by_category, name="recipes_by_category"),
    path("recipe/<int:pk>/edit/", views.edit_recipe, name="edit_recipe"),
    path("recipe/<int:pk>/delete/", views.delete_recipe, name="delete_recipe"),
]