from django import forms
from django.forms import fields
from django.forms.widgets import DateInput, EmailInput, FileInput, NumberInput, Select, TextInput
from.models import Trainer

class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
        widgets={
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'FirstName'
                }),

            'last_name':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'LastName'
                }),

            'gender':Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Gender',
                'multiple':True,
                }),

            'profile_pic':FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Profile',
                'multiple':True,
                }),

            'resume':FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'PhoneNumber',
                'multiple':True,
                }),

            'joining_date':DateInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Joined'
                }),

            'nationality':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Country'
                }),

             'email_address': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),

            'salary':NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Salary'
                }),

            'company':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Company'
                }),

            'course':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'CourseName'
                }),
        }
       
        