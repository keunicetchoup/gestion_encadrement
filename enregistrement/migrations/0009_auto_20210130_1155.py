# Generated by Django 3.1.5 on 2021-01-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enregistrement', '0008_auto_20210130_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soutenance',
            name='note',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
