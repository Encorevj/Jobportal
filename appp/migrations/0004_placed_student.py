# Generated by Django 3.1.7 on 2021-03-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appp', '0003_auto_20210328_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placed_student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='')),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
