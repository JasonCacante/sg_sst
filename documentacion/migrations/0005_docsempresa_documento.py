# Generated by Django 3.2.7 on 2021-11-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0004_alter_tipodoc_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='docsempresa',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='docempresa', verbose_name='Documento'),
        ),
    ]