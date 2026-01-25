from django.test import TestCase
from django.contrib.auth.models import User

from .forms import RecipeForm
from .models import Category

class RecipeFormTest(TestCase):
    """
    Tests for the RecipeForm
    """

    def setUp(self):
        """
        Create test data used across form tests
        """
        self.category = Category.objects.create(name="Meat")

    def test_recipe_form_is_valid(self):
        """
        Test that the form is valid with all required fields provided
        """
        form = RecipeForm(data={
            "title": "Test Recipe",
            "category": self.category.id,
            "ingredients": "Ingredient 1\nIngredient 2",
            "method": "Step 1\nStep 2"
        })

        self.assertTrue(
            form.is_valid(),
            msg="RecipeForm should be valid when all required fields are provided"
        )

    def test_recipe_form_is_invalid_without_title(self):
        """
        Test that the form is invalid when title is missing
        """
        form = RecipeForm(data={
            "title": "",
            "category": self.category.id,
            "ingredients": "Ingredient 1",
            "method": "Step 1"
        })

        self.assertFalse(
            form.is_valid(),
            msg="RecipeForm should be invalid when title is missing"
        )
        self.assertIn("title", form.errors)

    def test_recipe_form_is_invalid_without_ingredients(self):
        """
        Test that the form is invalid when ingredients are missing
        """
        form = RecipeForm(data={
            "title": "Test Recipe",
            "category": self.category.id,
            "ingredients": "",
            "method": "Step 1"
        })

        self.assertFalse(
            form.is_valid(),
            msg="RecipeForm should be invalid when ingredients are missing"
        )
        self.assertIn("ingredients", form.errors)

    def test_recipe_form_is_invalid_without_method(self):
        """
        Test that the form is invalid when method is missing
        """
        form = RecipeForm(data={
            "title": "Test Recipe",
            "category": self.category.id,
            "ingredients": "Ingredient 1",
            "method": ""
        })

        self.assertFalse(
            form.is_valid(),
            msg="RecipeForm should be invalid when method is missing"
        )
        self.assertIn("method", form.errors)