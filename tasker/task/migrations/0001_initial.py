# Generated by Django 4.1.7 on 2023-03-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumbersSum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_one', models.IntegerField()),
                ('number_two', models.IntegerField()),
                ('number_sum', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]