# Generated by Django 3.2.16 on 2023-01-23 13:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
