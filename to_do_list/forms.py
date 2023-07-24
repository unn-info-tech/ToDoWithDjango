from django import forms
from .models import VazifaModel, UquvchiModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CoolDateTimeWidget(forms.DateTimeInput):
    def __init__(self, attrs=None):
        default_attrs = {'type': 'datetime-local', 'class': 'cool-datetime-widget'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

class VazifaPostForm(forms.ModelForm):
    class Meta:
        model = VazifaModel
        fields = ["sarlavha", "tuliq_malumot", "tugatish_muddati", "bajarildi"]
        widgets = {
            'tugatish_muddati': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }





#=================================================================================
class UquvchiForm(forms.ModelForm):
    email = forms.CharField(max_length=20)
    class Meta:
        model = UquvchiModel
        fields = "__all__"




    