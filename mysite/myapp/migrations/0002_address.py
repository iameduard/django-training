# Generated by Django 2.0.5 on 2018-09-18 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]
