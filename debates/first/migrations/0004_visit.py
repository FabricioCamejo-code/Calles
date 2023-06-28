# Generated by Django 4.1.7 on 2023-04-19 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('operating_system', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=100)),
            ],
        ),
    ]
