from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Etudiant, Enseignant, Encadrement, Annee_Aca, Niveau, Parcours, Departement, Jury, Soutenance
from .forms import *


class EtudiantCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    success_url = reverse_lazy('enregistrement:etudiant-list')
    success_message = 'Etudiant ajouté avec succès !'
    form_class = EtudiantModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Enregistrer un nouvel étudiant"
        return context

class EtudiantListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'enregistrement/etudiant-list.html'
    model = Etudiant
    
class EtudiantDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    template_name = 'enregistrement/delete.html'
    model = Etudiant
    success_url = reverse_lazy('enregistrement:etudiant-list')
    success_message = 'Etudiant supprimé !'

class EtudiantUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    form_class = EtudiantModelForm
    model = Etudiant
    success_url = reverse_lazy('enregistrement:etudiant-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Modifier un étudiant"
        return context

class EnseignantCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    success_url = reverse_lazy('enregistrement:enseignant-list')
    success_message = 'Enseignant ajouté avec succès !'
    form_class = EnseignantModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Enregistrer un nouvel enseignant"
        return context

class EnseignantListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'enregistrement/enseignant-list.html'
    model = Enseignant
    
class EnseignantDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    template_name = 'enregistrement/delete.html'
    model = Enseignant
    success_url = reverse_lazy('enregistrement:enseignant-list')
    success_message = 'Enseignant supprimé !'

class EnseignantUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    form_class = EnseignantModelForm
    model = Enseignant
    success_url = reverse_lazy('enregistrement:enseignant-list')
    success_message = 'Enseignant modifié !'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Modifier un enseignant"
        return context


class EncadrementCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    success_url = reverse_lazy('enregistrement:encadrement-list')
    success_message = 'Encadrement ajouté avec succès !'
    form_class = EncadrementModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Enregistrer un nouvel encadrement"
        return context

class EncadrementListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'enregistrement/encadrement-list.html'
    model = Encadrement
    
class EncadrementDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    template_name = 'enregistrement/delete.html'
    model = Encadrement
    success_url = reverse_lazy('enregistrement:encadrement-list')
    success_message = 'Encadrement supprimé !'

class EncadrementUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    form_class = EncadrementModelForm
    model = Encadrement
    success_url = reverse_lazy('enregistrement:encadrement-list')
    success_message = 'Encadrement modifié !'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Modifier un encadrement"
        return context

class SoutenanceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    success_url = reverse_lazy('enregistrement:soutenance-list')
    success_message = 'Soutenance ajouté avec succès !'
    form_class = SoutenanceModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Programmer une soutenance"
        return context

class SoutenanceListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'enregistrement/soutenance-list.html'
    model = Soutenance
    
class SoutenanceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/login/'
    template_name = 'enregistrement/delete.html'
    model = Soutenance
    success_url = reverse_lazy('enregistrement:soutenance-list')
    success_message = 'Soutenance supprimé !'

class SoutenanceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    form_class = SoutenanceModelForm
    model = Soutenance
    success_url = reverse_lazy('enregistrement:encadrement-list')
    success_message = 'Soutenance modifié !'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Modifier une soutenance"
        return context

class JuryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    template_name = 'enregistrement/form.html'
    success_url = reverse_lazy('enregistrement:jury-list')
    success_message = 'Jury ajouté avec succès !'
    form_class = JuryModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = "Constituer un jury"
        return context


class JuryListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'enregistrement/jury-list.html'
    model = Jury
    