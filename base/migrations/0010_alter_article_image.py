# Generated by Django 3.2.7 on 2023-03-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(upload_to='articlesImages/'),
        ),
    ]
