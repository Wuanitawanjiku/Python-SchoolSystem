from .models import Courses
from django.shortcuts import redirect, render
from.forms import CourseRegistrationForm

# Create your views here.

def register_courses(request):
    if request.method=="POST":
        form = CourseRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_courses')
        else:
            print(form.errors)
    else:
        form = CourseRegistrationForm()

    return render(request, "register_courses.htm", {"form":form})

def course_list(request):
    courses = Courses.objects.all()
    return render(request, "course_list.htm", {"courses":courses})

def edit_course(request, id):
    course = Courses.objects.get(id=id)
    if request.method == "POST":
        form = CourseRegistrationForm(request.POST, instance=Courses)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = CourseRegistrationForm(instance=Courses)     
    return render(request, "edit_course.htm", {"form":form})       

def course_profile(request, id):
    course = Courses.objects.get(id=id)
    return render(request, "course_profile.htm", {"course":course})

def delete_course(request, id):
    course = Courses.objects.get(id=id)
    course.delete()
    return redirect("course_list")
    