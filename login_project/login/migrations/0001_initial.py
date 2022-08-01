# Generated by Django 4.0.4 on 2022-07-26 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('password2', models.CharField(max_length=40)),
            ],
        ),
    ]
