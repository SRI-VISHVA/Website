# Generated by Django 3.0.4 on 2020-03-10 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artist_name',
            new_name='album_name',
        ),
    ]