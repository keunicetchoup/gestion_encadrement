# Generated by Django 3.1.5 on 2021-01-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enregistrement', '0007_soutenance_jury'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soutenance',
            name='mention',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='soutenance',
            name='note',
            field=models.IntegerField(blank=True),
        ),
    ]