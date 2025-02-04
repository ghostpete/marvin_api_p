# Generated by Django 5.1.4 on 2025-01-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('amount', models.CharField(blank=True, max_length=200)),
                ('transaction', models.CharField(blank=True, max_length=200)),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('tmethod', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'User Complaint',
                'verbose_name_plural': 'User Complaints',
            },
        ),
    ]
