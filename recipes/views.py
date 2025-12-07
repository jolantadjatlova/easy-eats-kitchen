from django.shortcuts import render


# Create your views here.
def home(request):
    """
    Home page view for Easy Eats Kitchen.
    Renders the main landing page using the base template.
    
    """

    return render(request, 'recipes/base.html')