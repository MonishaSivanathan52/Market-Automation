# Generated by Django 4.1.5 on 2023-01-25 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_attachment_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_by',
        ),
    ]
