# Generated by Django 3.1.3 on 2020-12-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=500)),
                ('shorten_url', models.CharField(max_length=200)),
                ('Time_url_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
