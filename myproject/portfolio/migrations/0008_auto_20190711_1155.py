# Generated by Django 2.0.7 on 2019-07-11 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20190711_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractmodel',
            name='cname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]