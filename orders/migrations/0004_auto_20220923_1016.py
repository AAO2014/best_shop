# Generated by Django 2.2 on 2022-09-23 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20220923_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpart',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Good', verbose_name='good'),
        ),
    ]
