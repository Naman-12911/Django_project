# Generated by Django 3.0.5 on 2021-02-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0003_auto_20210224_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.IntegerField(max_length=10)),
                ('text', models.TextField()),
            ],
        ),
    ]
