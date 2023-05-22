# Generated by Django 4.2 on 2023-05-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_contact_titles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.CharField(max_length=60, verbose_name='Title booking')),
                ('booking_email', models.EmailField(max_length=254, verbose_name='Booking email page')),
                ('general', models.CharField(max_length=60, verbose_name='Title general')),
                ('general_email', models.EmailField(max_length=254, verbose_name='General email page')),
                ('technical', models.CharField(max_length=60, verbose_name='Title technical')),
                ('technical_email', models.EmailField(max_length=254, verbose_name='Technical email page')),
                ('map_link', models.URLField(verbose_name='Map adress link')),
                ('name', models.CharField(max_length=60, verbose_name='Your name')),
                ('email', models.CharField(max_length=60, verbose_name='Your email')),
                ('subject', models.CharField(max_length=60, verbose_name='Your subject')),
                ('message', models.CharField(max_length=60, verbose_name='Your message')),
                ('btn', models.CharField(max_length=60, verbose_name='Button name')),
            ],
            options={
                'verbose_name': 'Contact_Info',
                'verbose_name_plural': 'Contact_Info',
            },
        ),
    ]