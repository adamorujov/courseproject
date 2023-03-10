# Generated by Django 4.1.5 on 2023-02-23 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_readinganswer_value_alter_listeningresult_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=528)),
                ('resource', models.FileField(upload_to='resources/')),
                ('status', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='account.course')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.FileField(upload_to='certificates/')),
                ('score', models.FloatField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_certificates', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_certificates', to='account.course')),
            ],
        ),
    ]
