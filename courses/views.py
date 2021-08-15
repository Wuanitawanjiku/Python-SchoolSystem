from django.shortcuts import render
from.forms import CourseRegistrationForm

# Create your views here.

def register_courses(request):
    if request.method=="POST":
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = CourseRegistrationForm()

    return render(request, "register_courses.htm", {"form":form})

