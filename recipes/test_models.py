from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Recipe


class CategoryModelTest(TestCase):
    """Test the Category model"""
    
    def test_category_creation(self):
        """Test that we can create a category"""
        category = Category.objects.create(name="Meat")
        self.assertEqual(category.name, "Meat")
        
    def test_category_has_string_representation(self):
        """Test that category shows its name when printed"""
        category = Category.objects.create(name="Fish")
        self.assertEqual(str(category), "Fish")
    
    def test_category_slug_is_auto_generated(self):
        """Test that slug is automatically created from name"""
        category = Category.objects.create(name="15 min meals")
        self.assertEqual(category.slug, "15-min-meals")


class RecipeModelTest(TestCase):
    """Test the Recipe model"""
    
    def test_recipe_creation(self):
        """Test that we can create a recipe"""
        # Create a user (recipes need an owner)
        user = User.objects.create_user(username="testuser", password="testpass")
        
        # Create a recipe
        recipe = Recipe.objects.create(
            owner=user,
            title="Test Recipe",
            ingredients="Ingredient 1",
            method="Step 1"
        )
        
        # Check it worked
        self.assertEqual(recipe.title, "Test Recipe")
        self.assertEqual(recipe.owner, user)