# Generated by Django 3.2.5 on 2021-07-13 20:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sbs_debt', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sentinel_risk_score', models.CharField(choices=[(0, 'Bueno'), (1, 'Regular'), (2, 'Malo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CreditRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('status', models.CharField(choices=[[0, 'Pendiente'], [1, 'Rechazada'], [2, 'Aceptada']], max_length=10)),
                ('ai_score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credits.client')),
            ],
        ),
    ]
