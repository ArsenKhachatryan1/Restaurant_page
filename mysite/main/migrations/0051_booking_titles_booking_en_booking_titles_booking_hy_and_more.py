# Generated by Django 4.2 on 2023-05-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_ourteam_titles_home_en_ourteam_titles_home_hy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_titles',
            name='booking_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Booking'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='booking_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Booking'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='btn_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Button name'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='btn_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Button name'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='date_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Date & Time'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='date_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Date & Time'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='email_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Your email'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='email_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Your email'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='home_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Home'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='home_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Home'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='name_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Your name'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='name_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Your name'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='pages_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Pages'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='pages_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Pages'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='people_en',
            field=models.CharField(max_length=60, null=True, verbose_name='No Of People'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='people_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='No Of People'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='request_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Special Request'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='request_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Special Request'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='subtitle_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='subtitle_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='subtitle_text_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle text'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='subtitle_text_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle text'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='title_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='booking_titles',
            name='title_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Title'),
        ),
    ]
