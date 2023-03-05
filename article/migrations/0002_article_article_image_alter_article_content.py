# Generated by Django 4.1.6 on 2023-03-05 09:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Add image to the article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
