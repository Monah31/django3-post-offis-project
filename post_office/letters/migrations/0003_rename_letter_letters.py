# Generated by Django 3.2.16 on 2023-10-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_rename_lettercategory_letterscategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Letter',
            new_name='Letters',
        ),
    ]