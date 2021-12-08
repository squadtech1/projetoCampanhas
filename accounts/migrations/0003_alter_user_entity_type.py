# Generated by Django 3.2.7 on 2021-12-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='entity_type',
            field=models.CharField(choices=[('Física', 'Fisica'), ('Jurídica', 'Juridica')], default='Física', max_length=8, verbose_name='EntityType'),
        ),
    ]
