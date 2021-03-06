# Generated by Django 2.2.8 on 2019-12-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191208_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
