# Generated by Django 2.2 on 2022-01-12 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0012_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date_created']},
        ),
    ]
