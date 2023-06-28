# Generated by Django 4.1.7 on 2023-04-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_calle_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
