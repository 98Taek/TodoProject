# Generated by Django 4.2.4 on 2023-08-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='important',
            field=models.CharField(choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High')], default='Normal', max_length=6),
        ),
    ]