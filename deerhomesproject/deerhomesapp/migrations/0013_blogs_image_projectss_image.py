# Generated by Django 5.0 on 2024-10-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deerhomesapp', '0012_alter_blogs_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectss',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]