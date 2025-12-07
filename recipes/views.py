from django.shortcuts import render


# Create your views here.
def home(request):
    """
    Home page view for Easy Eats Kitchen.
    Renders the main landing page using the base template.
    """
    return render(request, "recipes/base.html")


def recipes_by_category(request, category_slug):
    """
    Shows recipes for a given category.
    """
    context = {
        "category": category_slug,
    }
    return render(request, "recipes/recipe_list.html", context)