# Generated by Django 3.1.4 on 2021-01-02 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0012_auto_20210103_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmesection',
            name='who_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='homesection',
            name='cv_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='storysection',
            name='story_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='weblogoname',
            name='web_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='worksection',
            name='work_article_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='worksection',
            name='work_index_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
