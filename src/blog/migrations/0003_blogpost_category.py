# Generated by Django 3.1.6 on 2024-01-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]