# Generated by Django 4.2 on 2023-05-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_about_titles_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_titles',
            name='title_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='title_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Title'),
        ),
    ]