# Generated by Django 4.1.2 on 2022-10-21 16:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_setting_create_at_remove_setting_update_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='contact',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
