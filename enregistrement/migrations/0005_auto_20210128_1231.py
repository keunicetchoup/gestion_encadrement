# Generated by Django 3.1.4 on 2021-01-28 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enregistrement', '0004_auto_20210128_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jury',
            name='enseignants',
        ),
        migrations.AlterField(
            model_name='jury',
            name='encadreur_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jury_from_encadreur_1', to='enregistrement.enseignant'),
        ),
        migrations.AlterField(
            model_name='jury',
            name='encadreur_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jury_from_encadreur_2', to='enregistrement.enseignant'),
        ),
        migrations.AlterField(
            model_name='jury',
            name='encadreur_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jury_from_encadreur_3', to='enregistrement.enseignant'),
        ),
        migrations.AlterField(
            model_name='jury',
            name='president',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jury_from_president', to='enregistrement.enseignant'),
        ),
        migrations.AlterField(
            model_name='jury',
            name='rapporteur_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jury_from_rapporteur_1', to='enregistrement.enseignant'),
        ),
        migrations.AlterField(
            model_name='jury',
            name='rapporteur_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jury_from_rapporteur_2', to='enregistrement.enseignant'),
        ),
    ]