# Generated by Django 4.2 on 2023-05-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_header_titles_block_name10_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_titles',
            name='about_en',
            field=models.CharField(max_length=60, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='about_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='home_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Home'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='home_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Home'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='pages_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Pages'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='pages_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Pages'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='subtitle_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='subtitle_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='subtitle_text_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle text'),
        ),
        migrations.AddField(
            model_name='about_titles',
            name='subtitle_text_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle text'),
        ),
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
