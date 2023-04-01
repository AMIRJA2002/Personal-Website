# Generated by Django 4.1.7 on 2023-03-31 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_ability_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatIOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyOfferHints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=500)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='home.whatioffer')),
            ],
        ),
    ]