from django.urls import path
from django.shortcuts import reverse
from .views import RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('list', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail')
]