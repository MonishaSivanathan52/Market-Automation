# Generated by Django 4.1.5 on 2023-01-25 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userplatform', '0003_alter_platform_created_by_alter_platform_updated_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='platform',
            name='updated_by',
        ),
    ]
