from django.shortcuts import render
from .forms import SignUpForm
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponsePermanentRedirect

# Create your views here.

# class SignUpView(generic.CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

def register(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ("Registration successful."))
            return HttpResponsePermanentRedirect(reverse('login'))
        else:
            messages.error(request, ("Unsuccessful registration. Invalid information.")) 
    else:
        form = SignUpForm()
    return render (request, "registration/signup.html", {"register_form":form})


    