# Generated by Django 2.1.5 on 2019-01-24 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frigg', '0011_auto_20190121_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='amount_of_material',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='company',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='material',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='model_orientation_path',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='model_path',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='printer',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='referral_person',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='time',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='type_of_print',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='user_id',
        ),
        migrations.AddField(
            model_name='job',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frigg.Client'),
        ),
        migrations.AddField(
            model_name='job',
            name='date_due',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='infill',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='layers',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='material',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='model_orientation_path',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='model_path',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='number_copies',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='print_time',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='speed',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='supports',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='weight',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='date_approved',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='date_due',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='job_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='jobs_completed',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_time_code',
            field=models.DateField(null=True),
        ),
    ]
