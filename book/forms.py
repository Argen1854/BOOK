from django import forms
from . import models

class ListBook(forms.ModelForm):
    class Meta:
        model = models.BookList
        fields = "__all__"
