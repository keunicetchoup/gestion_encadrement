from django.db import models

# Create your models here.

class Candidat(models.Model):
    noms = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    date_naiss = models.DateField()
    sexe = models.CharField(max_length=8)
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

class Enseignant(models.Model):
    noms = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)

class Encadrement(models.Model):
    nbr_heures = models.IntegerField()
    sujet = models.TextField()
    enseignants = models.ManyToManyField(Enseignant)
    etudiants = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

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
    president = models.CharField(max_length=100)
    rapporteur_1 = models.CharField(max_length=100)
    rapporteur_2 = models.CharField(max_length=100, null=True)
    encadreur_1 = models.CharField(max_length=100)
    encadreur_2 = models.CharField(max_length=100, null=True)
    encadreur_3 = models.CharField(max_length=100, null=True)
    enseignants = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

class Soutenance(models.Model):
    date_stn = models.DateField(null=True)
    type_stn = models.CharField(max_length=30)
    note = models.IntegerField()
    mention = models.CharField(max_length=20)
    num_comm = models.CharField(max_length=20)
    etudiants = models.ForeignKey(Etudiant, on_delete=models.CASCADE)







    
