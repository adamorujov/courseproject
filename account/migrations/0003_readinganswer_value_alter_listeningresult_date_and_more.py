# Generated by Django 4.1.5 on 2023-02-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_listeningresult_account_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='readinganswer',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listeningresult',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='readingresult',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
