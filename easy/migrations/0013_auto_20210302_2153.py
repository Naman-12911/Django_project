# Generated by Django 3.0.5 on 2021-03-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0012_sinup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinup',
            name='username',
            field=models.CharField(max_length=122),
        ),
    ]
