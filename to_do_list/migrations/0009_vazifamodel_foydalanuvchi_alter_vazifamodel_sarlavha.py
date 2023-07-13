# Generated by Django 4.2 on 2023-07-13 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0008_remove_vazifamodel_foydalanuvchi'),
    ]

    operations = [
        migrations.AddField(
            model_name='vazifamodel',
            name='foydalanuvchi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='to_do_list.foydalanuvchimodel'),
        ),
        migrations.AlterField(
            model_name='vazifamodel',
            name='sarlavha',
            field=models.CharField(max_length=200, verbose_name='vazifa'),
        ),
    ]
