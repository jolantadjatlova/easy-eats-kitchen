from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Category, Recipe


class RecipeViewsTest(TestCase):
    """
    Tests for the main views in the recipes app.
    These tests check that pages load correctly,
    permissions are enforced, and CRUD actions work as expected.
    """

    def setUp(self):
        # Create two users for permission testing
        self.user1 = User.objects.create_user(
            username="user1", password="pass12345"
        )
        self.user2 = User.objects.create_user(
            username="user2", password="pass12345"
        )

        # Create a category
        self.category = Category.objects.create(name="Meat")

        # Create one recipe for each user
        self.recipe_user1 = Recipe.objects.create(
            owner=self.user1,
            category=self.category,
            title="User1 Recipe",
            ingredients="Chicken\nSalt",
            method="Cook it"
        )

        self.recipe_user2 = Recipe.objects.create(
            owner=self.user2,
            category=self.category,
            title="User2 Recipe",
            ingredients="Fish\nLemon",
            method="Bake it"
        )

    # -------------------------
    # Public views
    # -------------------------

    def test_home_page_loads(self):
        """Check that the home page loads successfully"""
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/home.html")

    def test_recipes_list_page_loads(self):
        """Check that the recipes list page loads"""
        response = self.client.get(reverse("recipes:recipes_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes.html")

    def test_recipes_list_search_filters_results(self):
        """Check that searching filters recipes by keyword"""
        response = self.client.get(
            reverse("recipes:recipes_list"), {"q": "Chicken"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User1 Recipe")
        self.assertNotContains(response, "User2 Recipe")

    def test_recipes_by_category_page_loads(self):
        """Check that category pages load correctly"""
        response = self.client.get(
            reverse(
                "recipes:recipes_by_category",
                args=[self.category.slug]
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipes.html")
        self.assertContains(response, self.category.name)

    def test_recipes_by_category_search_filters_results(self):
        """Check that searching within a category filters results"""
        response = self.client.get(
            reverse(
                "recipes:recipes_by_category",
                args=[self.category.slug]
            ),
            {"q": "Lemon"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User2 Recipe")
        self.assertNotContains(response, "User1 Recipe")

    # -------------------------
    # Login-required views
    # -------------------------

    def test_my_recipes_redirects_when_logged_out(self):
        """Check that My Recipes redirects users who are not logged in"""
        response = self.client.get(reverse("recipes:my_recipes"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("account_login"), response.url)

    def test_my_recipes_shows_only_users_own_recipes(self):
        """Check that users only see their own recipes"""
        self.client.login(username="user1", password="pass12345")

        response = self.client.get(reverse("recipes:my_recipes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/my_recipes.html")

        self.assertContains(response, "User1 Recipe")
        self.assertNotContains(response, "User2 Recipe")

    def test_add_recipe_redirects_when_logged_out(self):
        """Check that add recipe page requires login"""
        response = self.client.get(reverse("recipes:add_recipe"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("account_login"), response.url)

    def test_add_recipe_creates_recipe_for_logged_in_user(self):
        """Check that a logged-in user can add a recipe"""
        self.client.login(username="user1", password="pass12345")

        response = self.client.post(
            reverse("recipes:add_recipe"),
            data={
                "title": "New Recipe",
                "category": self.category.id,
                "ingredients": "Ingredient 1",
                "method": "Step 1"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("recipes:my_recipes"))

        self.assertTrue(
            Recipe.objects.filter(
                owner=self.user1,
                title="New Recipe"
            ).exists()
        )

    def test_edit_recipe_redirects_when_logged_out(self):
        """Check that edit recipe requires login"""
        response = self.client.get(
            reverse("recipes:edit_recipe", args=[self.recipe_user1.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("account_login"), response.url)

    def test_owner_can_edit_their_recipe(self):
        """Check that recipe owners can edit their own recipes"""
        self.client.login(username="user1", password="pass12345")

        response = self.client.post(
            reverse("recipes:edit_recipe", args=[self.recipe_user1.id]),
            data={
                "title": "Updated Title",
                "category": self.category.id,
                "ingredients": "Updated ingredients",
                "method": "Updated method"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("recipes:my_recipes"))

        self.recipe_user1.refresh_from_db()
        self.assertEqual(self.recipe_user1.title, "Updated Title")

    def test_non_owner_cannot_edit_recipe(self):
        """Check that users cannot edit recipes they do not own"""
        self.client.login(username="user2", password="pass12345")

        response = self.client.get(
            reverse("recipes:edit_recipe", args=[self.recipe_user1.id])
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_recipe_redirects_when_logged_out(self):
        """Check that delete recipe requires login"""
        response = self.client.get(
            reverse("recipes:delete_recipe", args=[self.recipe_user1.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("account_login"), response.url)

    def test_owner_can_delete_their_recipe(self):
        """Check that recipe owners can delete their own recipes"""
        self.client.login(username="user1", password="pass12345")

        response_get = self.client.get(
            reverse("recipes:delete_recipe", args=[self.recipe_user1.id])
        )
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(
            response_get, "recipes/delete_recipe_confirm.html"
        )

        response_post = self.client.post(
            reverse("recipes:delete_recipe", args=[self.recipe_user1.id])
        )
        self.assertEqual(response_post.status_code, 302)
        self.assertEqual(response_post.url, reverse("recipes:my_recipes"))

        self.assertFalse(
            Recipe.objects.filter(id=self.recipe_user1.id).exists()
        )

    def test_non_owner_cannot_delete_recipe(self):
        """Check that users cannot delete recipes they do not own"""
        self.client.login(username="user2", password="pass12345")

        response = self.client.get(
            reverse("recipes:delete_recipe", args=[self.recipe_user1.id])
        )
        self.assertEqual(response.status_code, 404)