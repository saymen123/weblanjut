# Generated by Django 3.2.8 on 2021-12-04 05:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_artikel_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
