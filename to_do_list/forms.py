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
   
        

    #===========================

    challenge = forms.ChoiceField(label='Challenge', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['input_date'].initial = timezone.localdate()
        
        self.fields['challenge'].choices = self.get_challenge_choices()

    def get_challenge_choices(self):
        # Retrieve choices dynamically from a data source
        # For example, from a database query or API call
        days_of_month = [(str(day), f"{day} kun challenge") for day in range(1, 32)]
        return days_of_month

    
    


    class Meta:
        model = VazifaModel
        fields = ["sarlavha", "tuliq_malumot", 'input_date', 'challenge', 'boshlanish_vaqti', "tugatish_muddati", 'bajarildi']
        widgets = {
            'boshlanish_vaqti': forms.TimeInput(attrs={'type': 'time'}),
            'tugatish_muddati': forms.TimeInput(attrs={'type': 'time'}),
            
        }




#=================================================================================




    