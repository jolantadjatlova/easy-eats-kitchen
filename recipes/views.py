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
    Public page: shows all recipes (temporary hardcoded data for now).
    """
    recipes = [
        {
            "id": 1,
            "title": "Grilled Chicken Skewers",
            "image": "images/category-meat.png",
            "ingredients": [
                "2 chicken breasts, cut into chunks",
                "2 tbsp olive oil",
                "1 tbsp lemon juice",
                "1 tsp dried oregano",
            ],
            "method": [
                "In a bowl, combine olive oil, lemon juice, oregano, and seasonings.",
                "Thread chicken onto skewers and grill 10–12 minutes.",
            ],
        },
        {
            "id": 2,
            "title": "Beef Stir-Fry",
            "image": "images/category-meat.png",
            "ingredients": [
                "Beef strips",
                "Mixed vegetables",
                "Soy sauce",
                "Garlic",
            ],
            "method": [
                "Sear beef.",
                "Add vegetables.",
                "Stir in sauce and serve.",
            ],
        },
        {
            "id": 3,
            "title": "Herb-Crusted Pork Chops",
            "image": "images/category-meat.png",
            "ingredients": [
                "Pork chops",
                "Herbs",
                "Salt & pepper",
                "Oil",
            ],
            "method": [
                "Coat chops with herbs.",
                "Pan-fry until cooked through.",
            ],
        },
    ]

    return render(request, "recipes/recipes.html", {"recipes": recipes})


@login_required
def my_recipes(request):
    """
    Private page: shows recipes created by the logged-in user (temporary hardcoded data for now).
    """
    my_recipes = [
        {
            "id": 1,
            "title": "Grilled Chicken Skewers",
            "image": "images/category-meat.png",
            "ingredients": [
                "2 chicken breasts, cut into chunks",
                "2 tbsp olive oil",
                "1 tbsp lemon juice",
                "1 tsp dried oregano",
            ],
            "method": [
                "In a bowl, combine olive oil, lemon juice, oregano, and seasonings.",
                "Thread chicken onto skewers and grill 10–12 minutes.",
            ],
        },
        {
            "id": 2,
            "title": "Beef Stir-Fry",
            "image": "images/category-meat.png",
            "ingredients": ["Beef strips", "Mixed vegetables", "Soy sauce", "Garlic"],
            "method": ["Sear beef.", "Add veg.", "Stir in sauce and serve."],
        },
    ]

    return render(request, "recipes/my_recipes.html", {"recipes": my_recipes})


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