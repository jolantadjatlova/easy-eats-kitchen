from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "recipes/<slug:category_slug>/",
        views.recipes_by_category,
        name="recipes_by_category",
    ),
]