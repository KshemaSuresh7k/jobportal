# Generated by Django 4.0.2 on 2022-03-28 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
