# Generated by Django 2.2 on 2022-09-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads//good_pics/%Y/%m/%d/', verbose_name='picture'),
        ),
    ]