# Generated by Django 2.2.5 on 2019-12-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
