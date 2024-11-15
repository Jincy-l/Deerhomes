# Generated by Django 5.0 on 2024-10-05 06:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deerhomesapp', '0002_tbl_sub_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_blog_sub',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tbl_blog_sub',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tbl_blog_sub',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
