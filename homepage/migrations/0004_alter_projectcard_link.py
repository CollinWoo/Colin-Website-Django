# Generated by Django 4.0.1 on 2022-01-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_rename_projectcards_projectcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcard',
            name='link',
            field=models.URLField(blank=True, help_text='Enter where this card links to', null=True),
        ),
    ]
