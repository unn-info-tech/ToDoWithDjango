from django import forms
from .models import VazifaModel, DateBajarildiModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone



class VazifaPostForm(forms.ModelForm):
    input_date = forms.DateField(
        label='Select a Date',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['input_date'].initial = timezone.now().date()

    class Meta:
        model = VazifaModel
        fields = ["sarlavha", "tuliq_malumot", "tugatish_muddati", 'boshlanish_vaqti', 'bajarildi', 'input_date']
        widgets = {
            'boshlanish_vaqti': forms.TimeInput(attrs={'type': 'time'}),
            'tugatish_muddati': forms.TimeInput(attrs={'type': 'time'}),
            
        }




#=================================================================================




    