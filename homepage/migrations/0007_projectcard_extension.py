# Generated by Django 4.0.1 on 2022-01-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_remove_projectcard_media_url_projectcard_is_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcard',
            name='extension',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
