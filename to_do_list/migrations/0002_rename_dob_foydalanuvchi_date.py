# Generated by Django 4.2.3 on 2023-07-11 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foydalanuvchi',
            old_name='dob',
            new_name='date',
        ),
    ]
