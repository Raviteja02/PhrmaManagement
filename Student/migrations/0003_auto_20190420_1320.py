# Generated by Django 2.1.7 on 2019-04-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
