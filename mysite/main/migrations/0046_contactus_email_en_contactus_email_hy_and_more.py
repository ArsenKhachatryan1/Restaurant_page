# Generated by Django 4.2 on 2023-05-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_our_services_text_en_our_services_text_hy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email_en',
            field=models.EmailField(max_length=254, null=True, verbose_name='User email'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='email_hy',
            field=models.EmailField(max_length=254, null=True, verbose_name='User email'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message_en',
            field=models.TextField(null=True, verbose_name='User message'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message_hy',
            field=models.TextField(null=True, verbose_name='User message'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='User name'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='User name'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject_hy',
            field=models.CharField(max_length=50, null=True, verbose_name='Subject'),
        ),
    ]