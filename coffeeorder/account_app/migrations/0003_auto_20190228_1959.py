# Generated by Django 2.1.7 on 2019-02-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_auto_20190228_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='group_pic',
            field=models.ImageField(blank=True, default='group_pics/coffee.png', null=True, upload_to='group_pics/'),
        ),
    ]
