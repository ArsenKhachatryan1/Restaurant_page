# Generated by Django 4.2 on 2023-05-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_about_titles_title_en_about_titles_title_hy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_info',
            name='map_link',
            field=models.URLField(max_length=500, verbose_name='Map adress link'),
        ),
    ]
