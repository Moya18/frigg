# Generated by Django 2.1.5 on 2019-01-31 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frigg', '0019_auto_20190129_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='key',
            field=models.CharField(max_length=300, null=True),
        ),
    ]