# Generated by Django 4.1.7 on 2023-02-18 00:44

import cells.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='guards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('section', models.CharField(choices=[('BA', 'Bloque A'), ('BB', 'Bloque B'), ('BC', 'Bloque C')], default='BA', max_length=100)),
                ('schedule', models.CharField(choices=[('Mañanas', '06:00-14:00'), ('Tardes', '14:00-22:00'), ('Noches', '22:00-06:00')], default='Noches', max_length=100)),
                ('salary', models.IntegerField(validators=[cells.validators.sueldo_minimo])),
                ('job_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu', models.CharField(max_length=100)),
                ('Carne', models.IntegerField()),
                ('Numb_Guards_Assigned', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='prisoner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('judgment', models.IntegerField()),
                ('id_prisoner', models.IntegerField()),
                ('solitary_punishment', models.BooleanField(default=False, validators=[cells.validators.validar_Castigo])),
                ('cell_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cells.cells')),
            ],
        ),
    ]