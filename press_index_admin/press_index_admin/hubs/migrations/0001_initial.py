# Generated by Django 5.1 on 2024-09-02 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('time_delta_check', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
