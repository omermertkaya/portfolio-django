# Generated by Django 3.1.4 on 2021-01-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0003_auto_20210101_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posthome2',
            name='cv_fotograf_1',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='posthome4',
            name='who_fotograf',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='story_bolumu',
            name='story_fotograf',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='work_bolumu',
            name='work_fotograf',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='work_bolumu',
            name='work_fotograf_3',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
    ]