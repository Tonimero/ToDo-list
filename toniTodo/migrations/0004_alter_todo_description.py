# Generated by Django 4.1 on 2022-08-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toniTodo', '0003_alter_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(default=False, max_length=1000),
        ),
    ]