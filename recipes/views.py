from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Recipe


def home(request):
    return render(request, "recipes/home.html")


def recipes_list(request):
    """
    Public page: shows all recipes, supports simple search.
    """
    q = request.GET.get("q", "").strip()

    recipes = Recipe.objects.select_related("category", "owner").all()
    if q:
        recipes = recipes.filter(
            Q(title__icontains=q)
            | Q(ingredients__icontains=q)
            | Q(method__icontains=q)
        )

    return render(request, "recipes/recipes.html", {"recipes": recipes, "q": q})


def recipes_by_category(request, category_slug):
    """
    Public page: shows recipes for a given category, supports search.
    """
    q = request.GET.get("q", "").strip()
    category = get_object_or_404(Category, slug=category_slug)

    recipes = (
        Recipe.objects.select_related("category", "owner")
        .filter(category=category)
    )
    if q:
        recipes = recipes.filter(
            Q(title__icontains=q)
            | Q(ingredients__icontains=q)
            | Q(method__icontains=q)
        )

    return render(
        request,
        "recipes/recipes.html",
        {"recipes": recipes, "category": category, "q": q},
    )


@login_required
def my_recipes(request):
    """
    Private page: shows recipes created by the logged-in user, supports search.
    """
    q = request.GET.get("q", "").strip()

    recipes = (
        Recipe.objects.select_related("category", "owner")
        .filter(owner=request.user)
    )
    if q:
        recipes = recipes.filter(
            Q(title__icontains=q)
            | Q(ingredients__icontains=q)
            | Q(method__icontains=q)
        )

    return render(request, "recipes/my_recipes.html", {"recipes": recipes, "q": q})


@login_required
def add_recipe(request):
    return render(request, "recipes/add_recipe.html")


def signup(request):
    return render(request, "recipes/signup.html")