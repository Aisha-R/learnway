# Generated by Django 4.2.4 on 2023-08-27 18:29

from django.db import migrations, models


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
                ('stage', models.IntegerField(choices=[(0, 'Initial'), (1, 'Day 1'), (7, 'Day 7'), (16, 'Day 16'), (35, 'Day 35')], default=0, max_length=2)),
            ],
        ),
    ]