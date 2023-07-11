from django import forms
from .models import Foydalanuvchi, Vazifalar

class TodoPostForm(forms.Form):
    sarlavhaF = forms.CharField(max_length=200)
    slugF = forms.SlugField()
    tuliq_malumotF = forms.CharField(widget=forms.Textarea)
