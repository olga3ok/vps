# Generated by Django 4.2.18 on 2025-01-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=255, unique=True)),
                ('cpu', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('hdd', models.IntegerField()),
                ('status', models.CharField(choices=[('started', 'Started'), ('blocked', 'Blocked'), ('stopped', 'Stopped')], max_length=10)),
            ],
        ),
    ]
