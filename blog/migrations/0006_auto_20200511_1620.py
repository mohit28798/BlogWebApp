# Generated by Django 2.2.5 on 2020-05-11 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comments_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]