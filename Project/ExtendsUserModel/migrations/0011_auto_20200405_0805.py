# Generated by Django 3.0.3 on 2020-04-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtendsUserModel', '0010_auto_20200319_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]