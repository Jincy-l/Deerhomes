# Generated by Django 3.2.25 on 2024-10-04 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deerhomesapp', '0012_alter_blogs_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_blog_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.TextField()),
                ('sub_title_content', models.TextField()),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('metatag', models.CharField(blank=True, max_length=500, null=True)),
                ('metakeyword', models.CharField(blank=True, max_length=500, null=True)),
                ('metadescription', models.TextField(blank=True, null=True)),
                ('blog_image', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='blogs',
        ),
        migrations.AddField(
            model_name='projectss',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tbl_blog_sub',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deerhomesapp.tbl_blogs'),
        ),
    ]