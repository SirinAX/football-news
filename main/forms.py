from django import forms
from django.forms import ModelForm
from main.models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category", "thumbnail", "is_featured"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "border rounded-md p-2 w-full"
            }),
            "content": forms.Textarea(attrs={
                "class": "border rounded-md p-2 w-full",
                "rows": 5
            }),
            "category": forms.Select(attrs={
                "class": "border rounded-md p-2 w-full"
            }),
            "thumbnail": forms.ClearableFileInput(attrs={
                "class": "border rounded-md p-2 w-full"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "mr-2"
            }),
        }
