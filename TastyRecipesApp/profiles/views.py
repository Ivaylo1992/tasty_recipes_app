from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from TastyRecipesApp.common.app_helpers import ProfileInObjectMixin
from TastyRecipesApp.profiles.forms import CreateProfileForm, EditProfileForm
from TastyRecipesApp.profiles.models import Profile


class CreateProfileView(views.CreateView):
    queryset = Profile.objects.all()
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy("details_profile")
    form_class = CreateProfileForm


class DetailsProfileView(ProfileInObjectMixin, views.DetailView):
    queryset = Profile.objects.all() \
        .prefetch_related("recipe_set")
    template_name = "profiles/details-profile.html"


class EditProfileView(ProfileInObjectMixin, views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "profiles/edit-profile.html"
    form_class = EditProfileForm
    success_url = reverse_lazy("details_profile")


class DeleteProfileView(ProfileInObjectMixin, views.DeleteView):
    model = Profile
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")