from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ("ingredients", "method")

admin.site.register(Category)