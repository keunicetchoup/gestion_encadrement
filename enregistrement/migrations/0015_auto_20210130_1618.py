# Generated by Django 3.1.5 on 2021-01-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enregistrement', '0014_auto_20210130_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='abr_grade',
            field=models.CharField(choices=[('CC', 'CC'), ('MC', 'MC'), ('Pr', 'Pr'), ('Autre', 'Autre')], default='Autre', max_length=250),
        ),
        migrations.AlterField(
            model_name='grade',
            name='titre',
            field=models.CharField(choices=[('Chargé de cours', 'Chargé de cours'), ('Maitre de conférence', 'Maitre de conférence'), ('Professeur', 'Professeur'), ('Autre', 'Autre')], default='Autres', max_length=250),
        ),
    ]
