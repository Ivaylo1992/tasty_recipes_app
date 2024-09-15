from django import forms

from TastyRecipesApp.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = ("nickname", "first_name", "last_name", "chef")


class EditProfileForm(BaseProfileForm):
    ...