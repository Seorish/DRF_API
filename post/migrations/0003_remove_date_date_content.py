# Generated by Django 3.2.14 on 2022-07-22 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='date_content',
        ),
    ]
