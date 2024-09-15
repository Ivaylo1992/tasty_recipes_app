
from django.urls import path, include
from TastyRecipesApp.recipes import views

urlpatterns = [
    path("catalogue/", views.CatalogueView.as_view(), name="catalogue"),
    path("create/", views.CreateRecipeView.as_view(), name="create_recipe"),
    path("<int:recipe_id>/", include([
        path("details/", views.DetailsRecipeView.as_view(), name="details_recipe"),
        path("edit/", views.EditRecipeView.as_view(), name="edit_recipe"),
        path("delete/", views.DeleteRecipeView.as_view(), name="delete_recipe"),
    ]))
]
