from .models import Trainer
from django.shortcuts import redirect, render
from.forms import TrainerRegistrationForm
# Create your views here.

def register_trainer(request):
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print(f'Welcome! You are now a member')
            # return redirect('register_trainer')
        else:
            print(form.errors)
    else:
        form = TrainerRegistrationForm()
    return render(request, "register_trainer.htm",{"form":form})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, "trainer_list.htm", {"trainers":trainers})
