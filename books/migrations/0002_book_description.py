# Generated by Django 4.2.2 on 2023-06-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
