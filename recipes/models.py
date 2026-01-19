from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Recipe category model for organizing recipes.
    
    Categories are used to group recipes (e.g., Meat, Fish, Vegetarian).
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Recipe model storing user-created recipes.
    
    Each recipe belongs to one user (owner) and optionally one category.
    Includes ingredients, method, and optional image.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recipes"
    )

    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    ingredients = models.TextField(help_text="One ingredient per line")
    method = models.TextField(help_text="Step-by-step method")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title