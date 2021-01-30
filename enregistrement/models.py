from django.db import models
from django.contrib.auth.models import User

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
    moyenne = models.FloatField()
    date_licence = models.IntegerField()
    date_obt_licence = models.IntegerField()
    date_M1 = models.IntegerField()
    date_obt_M1 = models.IntegerField()
    date_M2 = models.IntegerField(blank=True, null=True)
    date_obt_M2 = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

class Etudiant(Candidat):
    matricule = models.CharField(max_length=8)


    def __str__(self):
        return '{} {}'.format(self.noms, self.prenoms)

class Grade(models.Model):
    titre = models.CharField(max_length=250)

    def __str__(self):
        return self.titre

class Enseignant(models.Model):
    noms = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

    def __str__(self):
        return self.grade.titre + " " + self.noms

class Encadrement(models.Model):
    nbr_heures = models.IntegerField()
    sujet = models.TextField()
    enseignants = models.ManyToManyField(Enseignant)
    etudiants = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='encadrements')

class Annee_Aca(models.Model):
    annee_deb = models.IntegerField()
    annee_fin = models.IntegerField()

class Cursus(models.Model):
    nom_dep = models.CharField(max_length=50)
    parcours = models.CharField(max_length=50)
    niveau = models.CharField(max_length=30)
    etudiants = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    annee_aca = models.ForeignKey(Annee_Aca, on_delete=models.CASCADE)

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






    
