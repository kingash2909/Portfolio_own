# Generated by Django 3.0.6 on 2020-06-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_display', '0004_profile_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('pdf', models.FileField(upload_to='pdf')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]