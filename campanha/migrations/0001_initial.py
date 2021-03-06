# Generated by Django 3.2.7 on 2021-12-04 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('start', models.DateField(default=django.utils.timezone.now)),
                ('end', models.DateField()),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Enabled', 'Enabled'), ('Disabled', 'Disabled'), ('Pending Donee Confirmation', 'Pending Donee Confirmation')], default='Enabled', max_length=50, verbose_name='Status')),
                ('donee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='donee', to=settings.AUTH_USER_MODEL)),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='donor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoneeNeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need', models.CharField(blank=True, max_length=50, null=True)),
                ('donee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_donee_need', to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
