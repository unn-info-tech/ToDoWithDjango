# Generated by Django 4.2 on 2023-07-13 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0007_rename_foydalanuvchi_foydalanuvchimodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vazifamodel',
            name='foydalanuvchi',
        ),
    ]
