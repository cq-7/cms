# Generated by Django 3.1 on 2020-08-27 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img_url',
            field=models.ImageField(null=True, upload_to='', verbose_name='图片地址'),
        ),
    ]