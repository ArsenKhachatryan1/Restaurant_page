# Generated by Django 4.2 on 2023-05-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('home', models.CharField(max_length=60, verbose_name='Home')),
                ('pages', models.CharField(max_length=60, verbose_name='Pages')),
                ('contact', models.CharField(max_length=60, verbose_name='Contact')),
                ('subtitle', models.CharField(max_length=60, verbose_name='Subtitle')),
                ('subtitle_text', models.CharField(max_length=60, verbose_name='Subtitle text')),
            ],
            options={
                'verbose_name': 'Contact_Titles',
                'verbose_name_plural': 'Contact_Titles',
            },
        ),
    ]
