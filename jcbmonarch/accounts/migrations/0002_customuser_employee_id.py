# Generated by Django 5.2.3 on 2025-06-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='employee_id',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='Табельный номер'),
            preserve_default=False,
        ),
    ]
