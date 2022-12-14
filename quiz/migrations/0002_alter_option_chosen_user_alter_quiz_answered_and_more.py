# Generated by Django 4.0.2 on 2022-07-17 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='chosen_user',
            field=models.ManyToManyField(blank=True, related_name='chosen_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answered',
            field=models.ManyToManyField(blank=True, related_name='answered', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='score',
            name='answerer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answerer', to=settings.AUTH_USER_MODEL),
        ),
    ]
