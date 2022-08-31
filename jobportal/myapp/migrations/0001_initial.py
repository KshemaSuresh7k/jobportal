# Generated by Django 4.0.2 on 2022-03-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobseeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(max_length=50, null=True)),
                ('qualification', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phonenumber', models.IntegerField(null=True)),
                ('applyfor', models.CharField(max_length=50, null=True)),
                ('workingmode', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
