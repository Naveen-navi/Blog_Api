# Generated by Django 4.2.4 on 2023-08-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authetication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]
