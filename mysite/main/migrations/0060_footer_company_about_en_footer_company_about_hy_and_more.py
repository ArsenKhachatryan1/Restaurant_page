# Generated by Django 4.2 on 2023-05-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_menu_list_text_en_menu_list_text_hy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer_company',
            name='about_en',
            field=models.CharField(max_length=60, null=True, verbose_name='About name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='about_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='About name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='contact_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Contact name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='contact_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Contact name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='privacy_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Privacy name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='privacy_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Privacy name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='reserv_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Reservation name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='reserv_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Reservation name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='terms_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Terms name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='terms_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Terms name'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='title_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Block title'),
        ),
        migrations.AddField(
            model_name='footer_company',
            name='title_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Block title'),
        ),
    ]