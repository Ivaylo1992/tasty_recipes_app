from TastyRecipesApp.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


class ProfileInContextMixin:
    extra_context = {
        "profile": get_profile()
    }


class ProfileInObjectMixin:
    def get_object(self, queryset=None):
        return get_profile()
