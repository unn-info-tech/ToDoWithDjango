# Generated by Django 4.2 on 2023-08-05 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do_list', '0026_delete_uquvchimodel_alter_datebajarildimodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='datebajarildimodel',
            name='foydalanuvchi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
