# Generated by Django 2.0.1 on 2018-02-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]