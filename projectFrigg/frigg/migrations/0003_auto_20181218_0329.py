# Generated by Django 2.1 on 2018-12-18 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frigg', '0002_auto_20181206_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='amount_of_material',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='date_time_code',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frigg.Client'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='printer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frigg.PrinterType'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='referral_person',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='type_of_print',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frigg.User'),
        ),
    ]
