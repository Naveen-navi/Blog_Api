# Generated by Django 4.2.4 on 2023-08-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authetication', '0003_remove_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
