from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# class UserProfileInfo(models.Model):


class Candidat(models.Model):
    SEXES = (
        ('MASCULIN', 'MASCULIN'),
        ('FEMININ', 'FEMININ'),
        ('AUTRES', 'AUTRES'),
    )
    noms = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    date_naiss = models.DateField()
    sexe = models.CharField(max_length=25, choices=SEXES, default="AUTRES")
    nationalite = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    moyenne_licence = models.FloatField()
    date_deb_licence = models.IntegerField()
    date_obt_licence = models.IntegerField()
    moyenne_master1 = models.FloatField()
    date_deb_M1 = models.IntegerField()
    date_obt_M1 = models.IntegerField()
    date_deb_M2 = models.IntegerField(blank=True, null=True)
    date_obt_M2 = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

class Etudiant(Candidat):
    matricule = models.CharField(unique=True, max_length=8)


    def __str__(self):
        return '{} {}'.format(self.noms, self.prenoms)

class Grade(models.Model):
    titre = models.CharField(max_length=100)
    abr_grade = models.CharField(max_length=8)

    def __str__(self):
        return '{} ({})'.format(self.titre, self.abr_grade)
        
class Enseignant(models.Model):
    noms = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

    def __str__(self):
        return self.noms + " " + self.prenoms

class Encadrement(models.Model):
    nbr_heures = models.IntegerField()
    sujet = models.TextField()
    enseignants = models.ManyToManyField(Enseignant)
    etudiants = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='encadrements')

class Annee_Aca(models.Model):
    annee_deb = models.IntegerField(unique=True, validators=(MinValueValidator(1990), MaxValueValidator(2021)))
    annee_fin = models.IntegerField(unique=True, validators=(MinValueValidator(1991), MaxValueValidator(2100)))

    def __str__(self):
        return '{} / {}'.format(self.annee_deb, self.annee_fin)

class Departement(models.Model):
    lib_departement = models.CharField(unique=True, max_length=50)
    abr_departement = models.CharField(max_length=8)

    def __str__(self):
        return '{} ({})'.format(self.lib_departement, self.abr_departement)

class Parcours(models.Model):
    lib_parcours = models.CharField(unique=True, max_length=50)
    abr_parcours = models.CharField(max_length=8)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.lib_parcours, self.abr_parcours)

class Niveau(models.Model):
    lib_niveau = models.CharField(unique=True, max_length=10)
    parcours = models.ManyToManyField(Parcours)
    annee_aca = models.ForeignKey(Annee_Aca, on_delete=models.CASCADE, related_name='niveau')

    def __str__(self):
        return self.lib_niveau

class Jury(models.Model):
    president = models.ForeignKey('Enseignant', on_delete=models.CASCADE, related_name='jury_from_president')
    rapporteur_1 = models.ForeignKey('Enseignant', on_delete=models.CASCADE, related_name='jury_from_rapporteur_1')
    rapporteur_2 = models.ForeignKey('Enseignant', on_delete=models.CASCADE, related_name='jury_from_rapporteur_2', null=True, blank=True)
    encadreur_1 = models.ForeignKey('Enseignant', on_delete=models.CASCADE, related_name='jury_from_encadreur_1')
    encadreur_2 = models.ForeignKey('Enseignant', on_delete=models.CASCADE, related_name='jury_from_encadreur_2', null=True, blank=True)
    encadreur_3 = models.ForeignKey('Enseignant', on_delete=models.CASCADE, related_name='jury_from_encadreur_3', null=True, blank=True)

    def __str__(self):
        return "Jury {}".format(self.pk)

class Soutenance(models.Model):
    date_stn = models.DateField(null=True)
    type_stn = models.CharField(max_length=30)
    note = models.IntegerField(blank=True, null=True)
    mention = models.CharField(max_length=20, blank=True)
    num_comm = models.CharField(max_length=20)
    etudiants = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    jury = models.ForeignKey(Jury, on_delete=models.CASCADE)






    
