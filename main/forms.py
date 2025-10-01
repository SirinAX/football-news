from django import forms
from django.forms import ModelForm
from main.models import News
from django.utils.html import strip_tags

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
            "thumbnail": forms.TextInput(attrs={
                "class": "border rounded-md p-2 w-full"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "mr-2"
            }),
        }
    def clean_title(self):
        title = self.cleaned_data["title"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["content"]
        return strip_tags(content)
