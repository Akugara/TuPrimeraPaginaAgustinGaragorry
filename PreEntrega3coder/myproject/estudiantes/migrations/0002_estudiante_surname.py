# Generated by Django 4.2.6 on 2023-11-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='surname',
            field=models.CharField(default='Default surname', max_length=100),
            preserve_default=False,
        ),
    ]