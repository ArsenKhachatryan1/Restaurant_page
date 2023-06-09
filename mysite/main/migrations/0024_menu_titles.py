# Generated by Django 4.2 on 2023-05-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_rename_lasttname_register_titles_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('home', models.CharField(max_length=60, verbose_name='Home')),
                ('pages', models.CharField(max_length=60, verbose_name='Pages')),
                ('menu', models.CharField(max_length=60, verbose_name='Menu')),
                ('subtitle', models.CharField(max_length=60, verbose_name='Subtitle')),
                ('subtitle_text', models.CharField(max_length=60, verbose_name='Subtitle text')),
            ],
            options={
                'verbose_name': 'Menu_Titles',
                'verbose_name_plural': 'Menu_Titles',
            },
        ),
    ]
