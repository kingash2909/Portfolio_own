# Generated by Django 3.0.6 on 2020-06-07 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('p_display', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pdf',
            field=models.FileField(default=django.utils.timezone.now, upload_to='pdf/'),
            preserve_default=False,
        ),
    ]
