# Generated by Django 2.2.5 on 2020-05-06 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191221_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.users')),
            ],
        ),
    ]
