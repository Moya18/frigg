# Generated by Django 2.1 on 2018-12-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frigg', '0008_auto_20181227_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='rfc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
