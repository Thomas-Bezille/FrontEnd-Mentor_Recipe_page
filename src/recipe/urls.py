from django.urls import path
from .views import recipe

urlpatterns = [
    path("", recipe, name='recipe'),
]