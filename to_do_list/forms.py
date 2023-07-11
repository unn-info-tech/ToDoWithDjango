from django import forms
from .models import Foydalanuvchi, Vazifalar

class TodoPostForm(forms.Form):
    sarlavhaF = forms.CharField(max_length=200)
    tuliq_malumotF = forms.CharField(widget=forms.Textarea)
    #dfhdfgjhfjfhj

    class Meta:
        model = Vazifalar()
        fields = ['sarlavha', 'tuliq_malumot']