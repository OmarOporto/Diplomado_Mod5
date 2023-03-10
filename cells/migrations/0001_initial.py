# Generated by Django 4.1.7 on 2023-02-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='cells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_id', models.IntegerField()),
                ('number_beds', models.IntegerField()),
                ('revision', models.DateTimeField(auto_now_add=True)),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
