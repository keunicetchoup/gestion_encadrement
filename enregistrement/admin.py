from django.contrib import admin

# Register your models here.

from .models import Etudiant, Enseignant, Encadrement, Annee_Aca, Cursus, Jury, Soutenance

admin.site.register(Etudiant)
admin.site.register(Enseignant)
admin.site.register(Encadrement)
admin.site.register(Annee_Aca)
admin.site.register(Cursus)
admin.site.register(Jury)
admin.site.register(Soutenance)