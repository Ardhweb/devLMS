# Generated by Django 5.1.4 on 2024-12-19 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_author'),
        ('brecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.book'),
        ),
    ]
