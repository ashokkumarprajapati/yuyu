# Generated by Django 3.2.6 on 2021-09-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210831_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicefloatingip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='invoicevolume',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
