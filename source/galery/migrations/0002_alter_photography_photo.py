# Generated by Django 4.2 on 2023-04-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo', verbose_name='Фото'),
        ),
    ]