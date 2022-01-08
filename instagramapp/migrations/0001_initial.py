# Generated by Django 2.2 on 2022-01-03 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='email address', max_length=254)),
                ('name', models.CharField(help_text='Full Name', max_length=100)),
                ('user_name', models.CharField(help_text='User Name', max_length=40, unique=True)),
                ('password', models.CharField(help_text='Password', max_length=40)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]