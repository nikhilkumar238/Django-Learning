# Generated by Django 3.1.6 on 2021-02-07 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='data',
            new_name='date',
        ),
    ]
