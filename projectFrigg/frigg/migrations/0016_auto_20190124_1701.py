# Generated by Django 2.1.5 on 2019-01-24 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frigg', '0015_quote_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='client_id',
        ),
        migrations.AddField(
            model_name='job',
            name='client',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
