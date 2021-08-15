from .models import Student
from django.shortcuts import redirect, render
from .models import Student

# Create your views here.
#Views handle http requests

from django.shortcuts import render
from .forms import StudentRegistrationForm

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_student')
        else:
            print(form.errors)
    else:
        form = StudentRegistrationForm()
    return render(request, "register_student.htm", {"form":form})

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.htm", {"students":students})