# Generated by Django 3.2.18 on 2023-03-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]