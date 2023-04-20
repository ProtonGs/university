# Generated by Django 4.1.7 on 2023-03-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30, verbose_name='nick')),
                ('login', models.CharField(max_length=30, verbose_name='login')),
                ('password', models.CharField(max_length=30, verbose_name='password')),
                ('password_confirmation', models.CharField(max_length=30, verbose_name='password_confirmation')),
            ],
            options={
                'verbose_name': 'Data_user',
                'verbose_name_plural': 'Data_users',
            },
        ),
    ]
