# Generated by Django 4.1.7 on 2023-03-31 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_app_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileImage',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile'),
        ),
    ]
