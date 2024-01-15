from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=255)
    cooking_time = models.PositiveIntegerField()
    ingredients = models.TextField()
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no-image.png')

    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})
