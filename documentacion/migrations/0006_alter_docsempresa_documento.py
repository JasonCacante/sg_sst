# Generated by Django 3.2.7 on 2021-11-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0005_docsempresa_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsempresa',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='docsempresa', verbose_name='Documento'),
        ),
    ]