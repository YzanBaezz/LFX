# Generated by Django 4.1.3 on 2022-11-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_hora_numero_alter_hora_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hora',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]