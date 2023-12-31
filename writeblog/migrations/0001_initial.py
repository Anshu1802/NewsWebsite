# Generated by Django 4.1.5 on 2023-12-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogimage', models.ImageField(upload_to='image')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
