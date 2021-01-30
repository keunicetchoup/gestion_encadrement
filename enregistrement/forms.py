from django import forms

from enregistrement.models import *


class EtudiantModelForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'

class EnseignantModelForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'

class EncadrementModelForm(forms.ModelForm):
    class Meta:
        model = Encadrement
        fields = '__all__'

class SoutenanceModelForm(forms.ModelForm):
    class Meta:
        model = Soutenance
        fields = '__all__'

class JuryModelForm(forms.ModelForm):
    class Meta:
        model = Jury
        fields = '__all__'