from django import forms
from.models import Courses
from django.forms import fields

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"
        