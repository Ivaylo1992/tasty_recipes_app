from django import forms

from TastyRecipesApp.recipes.models import Recipe


class BaseRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        exclude = ("author",)


class CreateRecipeForm(BaseRecipeForm):
    class Meta(BaseRecipeForm.Meta):
        widgets = {
            "ingredients": forms.Textarea(
                attrs={
                    "placeholder": "ingredient1, ingredient2, ..."
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "placeholder": "Enter detailed instructions here..."
                }
            ),
            "cooking_time": forms.TextInput(
                attrs={
                    "placeholder": "Provide the cooking time in minutes."
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "placeholder": "Optional image URL here..."
                }
            ),
        }


class EditRecipeForm(BaseRecipeForm):
    class Meta(BaseRecipeForm.Meta):
        ...


class DeleteRecipeForm(BaseRecipeForm):
    def __init__(self, *args, **kwargs):
        super(DeleteRecipeForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance