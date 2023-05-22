# Generated by Django 4.2 on 2023-05-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_review_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('home', models.CharField(max_length=60, verbose_name='Home')),
                ('pages', models.CharField(max_length=60, verbose_name='Pages')),
                ('login', models.CharField(max_length=60, verbose_name='Login')),
                ('subtitle', models.CharField(max_length=60, verbose_name='Subtitle')),
                ('username', models.CharField(max_length=60, verbose_name='Your name')),
                ('password', models.CharField(max_length=60, verbose_name='Your email')),
                ('btn', models.CharField(max_length=60, verbose_name='Button name')),
            ],
            options={
                'verbose_name': 'Login_Titles',
                'verbose_name_plural': 'Login_Titles',
            },
        ),
    ]
