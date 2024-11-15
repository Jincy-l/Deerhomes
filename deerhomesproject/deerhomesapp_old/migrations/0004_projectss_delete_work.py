# Generated by Django 5.0 on 2024-09-28 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deerhomesapp', '0003_alter_login_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='work',
        ),
    ]
