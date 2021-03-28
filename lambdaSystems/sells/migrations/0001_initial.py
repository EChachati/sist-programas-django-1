# Generated by Django 3.1.7 on 2021-03-26 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sells',
            fields=[
                ('invoice_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('income', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('products', models.JSONField()),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]