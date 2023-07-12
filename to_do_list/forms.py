from django import forms
from .models import Vazifalar, UquvchiModel

class VazifaPostForm(forms.Form):
    sarlavhaF = forms.CharField(max_length=200)
    tuliq_malumotF = forms.CharField(widget=forms.Textarea)
    #dfhdfgjhfjfhj

class UquvchiForm(forms.ModelForm):
    email = forms.CharField(max_length=20)
    class Meta:
        model = UquvchiModel
        fields = "__all__"

    