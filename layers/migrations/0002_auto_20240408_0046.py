# Generated by Django 3.2.12 on 2024-04-08 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multilayerdimension',
            name='theme',
        ),
        migrations.AddField(
            model_name='multilayerdimension',
            name='layer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='layers.layer'),
            preserve_default=False,
        ),
    ]