# Generated by Django 3.2.5 on 2021-07-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactbook', '0002_rename_todo_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.IntegerField(),
        ),
    ]
