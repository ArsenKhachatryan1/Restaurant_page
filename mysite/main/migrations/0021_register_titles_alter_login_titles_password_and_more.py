# Generated by Django 4.2 on 2023-05-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_login_titles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register_Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('home', models.CharField(max_length=60, verbose_name='Home')),
                ('pages', models.CharField(max_length=60, verbose_name='Pages')),
                ('signup', models.CharField(max_length=60, verbose_name='Signup')),
                ('subtitle', models.CharField(max_length=60, verbose_name='Subtitle')),
                ('username', models.CharField(max_length=60, verbose_name='Username')),
                ('firstname', models.CharField(max_length=60, verbose_name='Firstname')),
                ('lasttname', models.CharField(max_length=60, verbose_name='Lasttname')),
                ('email', models.CharField(max_length=60, verbose_name='Your email')),
                ('password1', models.CharField(max_length=60, verbose_name='Password-1')),
                ('password2', models.CharField(max_length=60, verbose_name='Password-2')),
                ('btn', models.CharField(max_length=60, verbose_name='Button name')),
            ],
            options={
                'verbose_name': 'Register_Titles',
                'verbose_name_plural': 'Register_Titles',
            },
        ),
        migrations.AlterField(
            model_name='login_titles',
            name='password',
            field=models.CharField(max_length=60, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='login_titles',
            name='username',
            field=models.CharField(max_length=60, verbose_name='Username'),
        ),
    ]
