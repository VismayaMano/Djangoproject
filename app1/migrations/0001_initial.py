# Generated by Django 4.1.3 on 2022-11-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Brand', models.CharField(max_length=20)),
                ('Model', models.CharField(max_length=20)),
                ('Price', models.IntegerField(default=0)),
                ('Engine', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Place', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=8)),
            ],
        ),
    ]
