# Generated by Django 2.2.19 on 2021-03-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=260)),
                ('post_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='Images/')),
            ],
        ),
    ]