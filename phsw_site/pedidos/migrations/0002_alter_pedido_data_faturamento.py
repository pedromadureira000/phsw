# Generated by Django 3.2.6 on 2021-08-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_faturamento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]