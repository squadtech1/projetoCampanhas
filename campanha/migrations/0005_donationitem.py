# Generated by Django 3.2.7 on 2021-11-07 09:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('campanha', '0004_alter_campanha_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('volume', models.IntegerField()),
                ('campanha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campanha', to='campanha.campanha')),
            ],
        ),
    ]
