from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name="Macaroni and Cheese", 
cooking_time=12, ingredients="Noodles, Butter, Cheese", 
description="A simple Mac and Cheese recipe that will bring you back to your childhood.")
        
    def test_recipe_name(self):
        recipe = Recipe.objects.get(recipe_id=1)

        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):

        recipe = Recipe.objects.get(recipe_id=1)

        max_length = recipe._meta.get_field('name').max_length

        self.assertEqual(max_length, 255)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')

