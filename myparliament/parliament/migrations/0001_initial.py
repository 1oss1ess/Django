# Generated by Django 3.1 on 2020-09-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParliamentMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_birth', models.CharField(blank=True, max_length=10, null=True)),
                ('place_birth', models.CharField(blank=True, max_length=250, null=True)),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('languages', models.CharField(blank=True, max_length=250, null=True)),
                ('selected_with', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.CharField(blank=True, max_length=250, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
