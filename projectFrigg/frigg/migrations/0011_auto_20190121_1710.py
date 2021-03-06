# Generated by Django 2.1.5 on 2019-01-21 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frigg', '0010_auto_20181227_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_time_code',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='quote_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frigg.Quote'),
        ),
        migrations.AlterField(
            model_name='job',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frigg.User'),
        ),
    ]
