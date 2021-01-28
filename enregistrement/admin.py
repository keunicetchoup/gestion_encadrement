from django.contrib import admin

# Register your models here.

from .models import Etudiant, Grade, Enseignant, Encadrement, Annee_Aca, Cursus, Jury, Soutenance

admin.site.register(Etudiant)

class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('noms', 'prenoms', 'grade')

admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Encadrement)
admin.site.register(Annee_Aca)
admin.site.register(Cursus)
admin.site.register(Jury)
admin.site.register(Soutenance)
admin.site.register(Grade)

admin.site.site_header = "Gestion des encadrements"