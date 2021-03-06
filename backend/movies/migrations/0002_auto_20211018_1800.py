# Generated by Django 3.2.8 on 2021-10-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='watch_list',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='password',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Seen',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
