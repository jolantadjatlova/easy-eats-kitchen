from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    """
    Home page view for Easy Eats Kitchen.
    Renders the main landing page using the base template.
    """
    return render(request, "recipes/home.html")


def recipes_by_category(request, category_slug):
    """
    Shows recipes for a given category.
    """
    context = {
        "category": category_slug,
    }
    return render(request, "recipes/recipe_list.html", context)

def recipes_list(request):
    """
    Public page: shows all recipes (placeholder for now).
    """
    return render(request, "recipes/recipes.html")


@login_required
def my_recipes(request):
    """
    Private page: shows recipes created by the logged-in user (placeholder for now).
    """
    return render(request, "recipes/my_recipes.html")


@login_required
def add_recipe(request):
    """
    Private page: add a recipe (placeholder for now).
    """
    return render(request, "recipes/add_recipe.html")


def signup(request):
    """
    Registration page placeholder.
    (Later you'll replace with Django allauth or your own form.)
    """
    return render(request, "recipes/signup.html")