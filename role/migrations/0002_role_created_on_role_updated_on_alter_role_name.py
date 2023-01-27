# Generated by Django 4.2 on 2023-01-12 04:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
