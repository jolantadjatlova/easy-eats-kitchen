from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect

from .forms import RecipeForm
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
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = request.user
            recipe.save()
            messages.success(request, "Recipe added successfully!")
            return redirect("recipes:my_recipes")
        messages.error(request, "Please fix the errors below.")
    else:
        form = RecipeForm()

    return render(request, "recipes/add_recipe.html", {"form": form})


def signup(request):
    return render(request, "recipes/signup.html")

@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, owner=request.user)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully!")
            return redirect("recipes:my_recipes")
        messages.error(request, "Please fix the errors below.")
    else:
        form = RecipeForm(instance=recipe)

    return render(request, "recipes/edit_recipe.html", {"form": form, "recipe": recipe})


@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, owner=request.user)

    if request.method == "POST":
        recipe.delete()
        messages.success(request, "Recipe deleted successfully!")
        return redirect("recipes:my_recipes")

    return render(request, "recipes/delete_recipe_confirm.html", {"recipe": recipe})