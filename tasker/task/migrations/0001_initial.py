# Generated by Django 4.1.7 on 2023-03-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsyncResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('n_rows', models.IntegerField()),
                ('finished_at', models.DateTimeField()),
                ('result', models.CharField(max_length=120)),
            ],
        ),
    ]
