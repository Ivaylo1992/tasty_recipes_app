from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from TastyRecipesApp.common.app_helpers import get_profile, ProfileInContextMixin
from TastyRecipesApp.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from TastyRecipesApp.recipes.models import Recipe


class CatalogueView(ProfileInContextMixin, views.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/catalogue.html"


class CreateRecipeView(ProfileInContextMixin, views.CreateView):
    queryset = Recipe.objects.all()
    template_name = "recipes/create-recipe.html"
    form_class = CreateRecipeForm
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        form.instance.author = get_profile()
        return super().form_valid(form)


class DetailsRecipeView(ProfileInContextMixin, views.DetailView):
    queryset = Recipe.objects.all()
    template_name = "recipes/details-recipe.html"
    pk_url_kwarg = "recipe_id"

    def get_object(self, queryset=None):
        return Recipe.objects.get(id=self.kwargs.get("recipe_id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredients = self.object.ingredients.split(", ")
        context["ingredients"] = ingredients
        return context


class EditRecipeView(ProfileInContextMixin, views.UpdateView):
    queryset = Recipe.objects.all()
    form_class = EditRecipeForm
    template_name = "recipes/edit-recipe.html"
    success_url = reverse_lazy("catalogue")

    pk_url_kwarg = "recipe_id"


class DeleteRecipeView(ProfileInContextMixin, views.DeleteView):
    queryset = Recipe.objects.all()
    template_name = "recipes/delete-recipe.html"
    success_url = reverse_lazy("catalogue")
    form_class = DeleteRecipeForm

    pk_url_kwarg = "recipe_id"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs