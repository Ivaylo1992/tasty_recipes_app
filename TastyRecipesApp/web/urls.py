
from django.urls import path
from TastyRecipesApp.web import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
