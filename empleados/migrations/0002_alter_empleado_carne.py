# Generated by Django 3.2.7 on 2021-11-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='carne',
            field=models.FileField(blank=True, null=True, upload_to='documentos'),
        ),
    ]
