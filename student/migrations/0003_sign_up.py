# Generated by Django 4.2.6 on 2023-10-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_contactmodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('cpassword', models.CharField(max_length=255)),
            ],
        ),
    ]
