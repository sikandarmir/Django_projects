# Generated by Django 4.0.6 on 2022-07-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_Name', models.CharField(max_length=50)),
                ('Book_description', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('num_books', models.IntegerField()),
                ('Book_types', models.CharField(max_length=10)),
            ],
        ),
    ]