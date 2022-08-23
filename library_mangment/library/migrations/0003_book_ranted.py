# Generated by Django 4.0.6 on 2022-07-24 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_ranted',
            fields=[
                ('Book_ranted_id', models.IntegerField(primary_key=True, serialize=False)),
                ('num_ranted_books', models.IntegerField()),
                ('Book_foreign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]