# Generated by Django 5.0.4 on 2024-05-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AadhaarCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PANCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='ExtractedText',
        ),
    ]
