# Generated by Django 3.1 on 2020-08-27 03:47

from django.db import migrations, models
import utils.common


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200827_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img_url',
            field=models.ImageField(null=True, storage=utils.common.MyStorage(), upload_to='', verbose_name='图片地址'),
        ),
    ]