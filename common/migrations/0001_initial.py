# Generated by Django 4.0.4 on 2022-05-10 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'Owners',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.owner')),
            ],
            options={
                'db_table': 'Dogs',
            },
        ),
    ]
