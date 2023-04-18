# Generated by Django 4.0.6 on 2023-02-12 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0013_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='フォロー')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userowner', to=settings.AUTH_USER_MODEL, verbose_name='ユーザ')),
            ],
        ),
    ]