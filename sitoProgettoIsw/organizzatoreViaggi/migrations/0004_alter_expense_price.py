# Generated by Django 4.2.5 on 2023-09-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizzatoreViaggi', '0003_alter_stage_description_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='price',
            field=models.FloatField(),
        ),
    ]
