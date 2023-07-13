from django import forms
from .models import VazifaModel, UquvchiModel

class VazifaPostForm(forms.ModelForm):
    class Meta:
        model = VazifaModel
        fields = ["sarlavha", "tuliq_malumot", "tugatish_muddati"]
        widgets = {
            'tugatish_muddati': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
        }

class UquvchiForm(forms.ModelForm):
    email = forms.CharField(max_length=20)
    class Meta:
        model = UquvchiModel
        fields = "__all__"




    