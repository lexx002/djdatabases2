# Generated by Django 2.0.5 on 2019-08-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190821_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_main',
        ),
        migrations.AddField(
            model_name='articlebycategory',
            name='is_main_category',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]