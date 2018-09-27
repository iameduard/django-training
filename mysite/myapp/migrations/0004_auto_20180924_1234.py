# Generated by Django 2.0.5 on 2018-09-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bookname', models.CharField(max_length=500)),
                ('Authorname', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Firstname',
        ),
        migrations.DeleteModel(
            name='section',
        ),
    ]