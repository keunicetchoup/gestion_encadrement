from django.contrib import admin

# Register your models here.

from .models import Etudiant, Grade, Enseignant, Encadrement, Annee_Aca, Jury, Soutenance, Departement, Parcours, Niveau

admin.site.register(Etudiant)

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('noms', 'prenoms', 'grade')

admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Encadrement)
admin.site.register(Annee_Aca)
admin.site.register(Niveau)
admin.site.register(Parcours)
admin.site.register(Departement)
admin.site.register(Jury)
admin.site.register(Soutenance)
admin.site.register(Grade)

admin.site.site_header = "Gestion des encadrements"