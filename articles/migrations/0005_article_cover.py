# Generated by Django 3.2 on 2021-05-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210508_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
