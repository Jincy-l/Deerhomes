# Generated by Django 5.0 on 2024-10-04 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deerhomesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_sub_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subimage', models.TextField(blank=True, null=True)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='deerhomesapp.projectss')),
            ],
        ),
    ]
