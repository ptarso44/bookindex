# Generated by Django 4.2.6 on 2023-10-17 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_release_year_book_release_date_book_publisher'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('name', 'author', 'publisher', 'release_date')},
        ),
    ]
