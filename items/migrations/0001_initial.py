# Generated by Django 4.2.4 on 2023-08-30 17:04

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('init_date', models.DateField(auto_now_add=True)),
                ('next_date', models.DateField(default=items.models.Item.calculate_next_date, editable=False)),
                ('stage', models.IntegerField(choices=[(0, 'Initial'), (1, 'Day 1'), (7, 'Day 7'), (16, 'Day 16'), (35, 'Day 35')], default=0, editable=False)),
            ],
        ),
    ]
