from django import forms
from django.forms import fields
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"    #creating a form that contains attributes of all the models
