# Generated by Django 3.2.4 on 2021-06-24 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='url',
        ),
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.SlugField(default='liked_videos', max_length=255, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.collection'),
        ),
    ]
