# Generated by Django 2.2.3 on 2019-07-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pj_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('outline1', models.TextField()),
                ('deadline1', models.DateField(blank=True)),
                ('progress1', models.IntegerField(blank=True)),
                ('outline2', models.TextField(blank=True)),
                ('deadline2', models.DateField(blank=True)),
                ('progress2', models.IntegerField(blank=True)),
                ('outline3', models.TextField(blank=True)),
                ('deadline3', models.DateField(blank=True)),
                ('progress3', models.IntegerField(blank=True)),
                ('outline4', models.TextField(blank=True)),
                ('gp_title', models.CharField(blank=True, max_length=200)),
                ('gp_outline', models.TextField(blank=True)),
                ('gp_reason', models.TextField(blank=True)),
                ('bp_title', models.CharField(blank=True, max_length=200)),
                ('bp_outline', models.TextField(blank=True)),
                ('bp_reason', models.TextField(blank=True)),
                ('next_move', models.TextField(blank=True)),
                ('problem_outline', models.TextField(blank=True)),
                ('effort', models.TextField(blank=True)),
                ('consultation', models.TextField(blank=True)),
                ('weekly_pwh', models.FloatField()),
                ('total_pwh', models.FloatField()),
                ('weekly_poh', models.FloatField()),
                ('total_poh', models.FloatField()),
                ('weekly_iwh', models.FloatField()),
                ('total_iwh', models.FloatField()),
                ('pointed_matter', models.TextField(blank=True)),
                ('free_text', models.TextField(blank=True)),
            ],
        ),
    ]
