# Generated by Django 3.1.7 on 2021-03-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_user',
            name='types',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
