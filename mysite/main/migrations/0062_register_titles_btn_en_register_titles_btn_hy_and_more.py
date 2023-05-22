# Generated by Django 4.2 on 2023-05-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_footer_opening_delivery_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_titles',
            name='btn_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Button name'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='btn_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Button name'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='email_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Your email'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='email_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Your email'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='firstname_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Firstname'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='firstname_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Firstname'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='home_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Home'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='home_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Home'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='lastname_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Lasttname'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='lastname_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Lasttname'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='pages_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Pages'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='pages_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Pages'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='password1_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Password-1'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='password1_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Password-1'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='password2_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Password-2'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='password2_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Password-2'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='signup_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Signup'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='signup_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Signup'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='subtitle_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='subtitle_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='title_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='title_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='username1_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='register_titles',
            name='username1_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Username'),
        ),
    ]
