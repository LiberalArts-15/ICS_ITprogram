# Generated by Django 3.2.22 on 2023-10-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideaboard', '0002_idea_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea_post',
            name='image1',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='idea_post',
            name='image2',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='idea_post',
            name='image3',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
    ]