# Generated by Django 4.1.5 on 2023-01-25 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_created_by_user_updated_by'),
        ('post', '0007_alter_attachment_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_attachment', to='user.user'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_attachment', to='user.user'),
        ),
    ]
