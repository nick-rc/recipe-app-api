# Generated by Django 2.1.15 on 2022-01-05 00:13

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220103_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='imapge',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]