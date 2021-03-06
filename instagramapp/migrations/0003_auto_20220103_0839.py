# Generated by Django 2.2 on 2022-01-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0002_auto_20220103_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
