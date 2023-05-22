# Generated by Django 4.2 on 2023-05-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_contact_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_adress',
            name='adress_link',
            field=models.URLField(default=1, verbose_name='Adress link'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact_adress',
            name='adress',
            field=models.CharField(max_length=100, verbose_name='Adress'),
        ),
    ]
