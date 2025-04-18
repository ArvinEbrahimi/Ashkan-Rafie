# Generated by Django 5.1.6 on 2025-03-24 10:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('image', models.ImageField(upload_to='blog_img/')),
                ('status', models.BooleanField(choices=[(True, 'Publish'), (False, 'Draft')], default=False)),
            ],
        ),
    ]
