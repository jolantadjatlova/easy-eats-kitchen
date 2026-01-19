from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "category", "image", "ingredients", "method"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "ingredients": SummernoteWidget(attrs={
                'summernote': {
                    'width': '100%',
                    'height': '200px',
                    'placeholder': 'One ingredient per line',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline']],
                        ['para', ['ul', 'ol']],
                    ]
                }
            }),
            "method": SummernoteWidget(attrs={
                'summernote': {
                    'width': '100%',
                    'height': '250px',
                    'placeholder': 'One step per line',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline']],
                        ['para', ['ul', 'ol']],
                    ]
                }
            }),
        }