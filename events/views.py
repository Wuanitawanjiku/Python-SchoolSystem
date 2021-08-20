from .models import Events
from django.shortcuts import redirect, render
from.forms import EventRegistrationForm

# Create your views here.

def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_event')
        else:
            print(form.errors)
    else:
        form=EventRegistrationForm()
    return render(request,"register_event.htm", {"form":form})

def event_list(request):
    events = Events.objects.all()
    return render(request, "event_list.htm", {"events":events})