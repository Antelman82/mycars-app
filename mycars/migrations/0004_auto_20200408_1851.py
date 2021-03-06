# Generated by Django 3.0.5 on 2020-04-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycars', '0003_auto_20200408_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltype',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='modeltype',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='modeltype',
            name='image_url',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='modeltype',
            name='trim',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
