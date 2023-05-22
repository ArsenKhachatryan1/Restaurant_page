# Generated by Django 4.2 on 2023-05-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_our_services_alter_service_titles_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='User name')),
                ('email', models.EmailField(max_length=254, verbose_name='User email')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='User message')),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUs',
            },
        ),
    ]