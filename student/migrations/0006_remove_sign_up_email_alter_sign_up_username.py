# Generated by Django 4.2.6 on 2023-11-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_sign_up_options_rename_name_sign_up_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sign_up',
            name='email',
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='username',
            field=models.EmailField(max_length=50),
        ),
    ]
