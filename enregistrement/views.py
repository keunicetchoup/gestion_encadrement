from django.shortcuts import render, redirect
from django.htpp import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import Etudiant, Enseignant, Encadrement, Annee_Aca, Cursus, Jury, Soutenance
from .forms import OrderForm
from .filters import OrderFilter

def registerPage(request):
    form = 
    context = {}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
