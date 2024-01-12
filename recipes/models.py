from django.db import models

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=255)
    cooking_time = models.PositiveIntegerField()
    ingredients = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.description}"
