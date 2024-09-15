from django.views import generic as views

from TastyRecipesApp.common.app_helpers import ProfileInContextMixin
from TastyRecipesApp.profiles.models import Profile


class IndexView(ProfileInContextMixin, views.ListView):
    queryset = Profile.objects.all()
    template_name = "web/home-page.html"