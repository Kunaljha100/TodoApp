# Generated by Django 4.1.3 on 2022-11-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo_task_remove_test_user_details_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
