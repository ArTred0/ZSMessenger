# Generated by Django 4.2 on 2024-10-13 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_czaty_alter_user_grupa_alter_user_imie_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pryjaciole',
            new_name='przyjaciole',
        ),
    ]
