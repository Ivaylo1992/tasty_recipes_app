from django.urls import path

from TastyRecipesApp.profiles import views

urlpatterns = [
    path("create/", views.CreateProfileView.as_view(), name="create_profile"),
    path("details/", views.DetailsProfileView.as_view(), name="details_profile"),
    path("edit/", views.EditProfileView.as_view(), name="edit_profile"),
    path("delete/", views.DeleteProfileView.as_view(), name="delete_profile"),
]
