# Generated by Django 5.0 on 2023-12-07 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_aurhor_book_aurthor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='aurthor',
            new_name='author',
        ),
    ]
