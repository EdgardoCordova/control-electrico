# Generated by Django 5.1 on 2024-08-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crc_DES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circuit_id', models.PositiveSmallIntegerField()),
                ('circuit_description', models.CharField(max_length=100)),
                ('circuit_status', models.BooleanField(null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('num_cycles', models.PositiveSmallIntegerField()),
                ('events_per_cycle', models.PositiveSmallIntegerField()),
                ('event_duration', models.PositiveSmallIntegerField()),
                ('random', models.BooleanField(default=False)),
                ('circuit_mode', models.CharField(choices=[('#0', 'ON'), ('#1', 'OFF'), ('#2', 'PROG')], max_length=20)),
            ],
        ),
    ]
